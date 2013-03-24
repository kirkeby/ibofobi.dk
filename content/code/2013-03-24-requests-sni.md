Title: SNI-support for requests
Tags: python, requests, http, ssl, sni

The `ssl` module in Python 2's standard library does not support the SNI
TLS-extension, and it probably never will, which means that the brilliant
`requests` HTTP library is also missing SNI-support on Python 2.

Now that `urllib3` has a contrib-module for SNI-support on Python 2 this might
change, but if you don't want to wait for the updated `urllib3` to be included
in a `requests` release, you can monkey-patch `requests` yourself:

1. Install the required packages:

        :::sh
        pip install pyOpenSSL ndg-httpsclient pyasn1

2. Download
   <a href='|filename|/files/requests_pyopenssl.py'>`requests_pyopenssl.py`</a>
   and put it somewhere on your `PYTHONPATH`.

3. Monkey-patch `requests` somewhere early in your application (possibly in a
   `sitecustomize` module):

        :::python
        try:
            import requests_pyopenssl
            from requests.packages.urllib3 import connectionpool
            connectionpool.ssl_wrap_socket = requests_pyopenssl.ssl_wrap_socket
        except ImportError:
            pass

If you want to test that it works, the following Python script should print
"`requests SNI-support Ok`" when run:

    :::python
    try:
        import requests_pyopenssl
        from requests.packages.urllib3 import connectionpool
        connectionpool.ssl_wrap_socket = requests_pyopenssl.ssl_wrap_socket
    except ImportError:
        raise

    import requests
    for host in ['alice', 'bob', 'carol', 'dave', 'mallory', 'www']:
        response = requests.get('https://%s.sni.velox.ch' % host)
        html = response.content.decode('utf-8', 'replace')
        assert 'Great!' in html, host

    print 'requests SNI-support Ok'
