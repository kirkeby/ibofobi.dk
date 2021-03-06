Id: tag:ibofobi.dk,2005-09-09:/blog/archive/2005/09/09/django-vs-xhtml/
Title: Django vs XHTML
Date: 2005-09-09

I like to serve my pages as XHTML, and with the correct content-type header `application/xhtml+xml` when possible, and downgrade to `text/html` for XHTML-challenged browsers. Out of the box Django cannot do this, but luckily the middleware architecture comes to my rescue :)

So, since this is such a short and sweet piece of code, here it is:

    import re
    
    re_ct_xhtml = re.compile(r'^application/xhtml\+xml\b')
    re_accept_xhtml = re.compile(r'\bapplication/xhtml\+xml\b')
    
    class XHTMLAsHTMLMiddleware:
        """I change content-type application/xhtml+xml into text/html, if the
        browser does not support the XHTML content-type."""
    
        def process_response(self, request, response):
            if re_ct_xhtml.match(response['Content-Type']):
                accept = request.META.get('HTTP_ACCEPT', '')
                if not re_accept_xhtml.search(accept):
                    ct = response['Content-Type']
                    ct = ct.replace('application/xhtml+xml', 'text/html')
                    response['Content-Type'] = ct
    
            return response


It is also available as `ibofobi.middleware.xhtml`
in `http://mel.ibofobi.dk/~sune/r/ibofobi.git`.