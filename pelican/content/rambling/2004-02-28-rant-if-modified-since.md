Title: Breaking the <tt>If-Modified-Since</tt> header
Date: 2004-02-28

<p>Some HTTP proxies unilaterally add a length argument to the
If-Modified-Since HTTP header, breaking the defined form of the the
If-Modified-Since header. Even if adding arguments to the
If-Modified-Since header works with most HTTP servers, there are several
reasons why it should be avoided:</p>

<ol>
<li> According to the HTTP RFC (both 1.0 and 1.1) it is <em>wrong</em>,
adding arguments to arbitrary headers is not allowed. If you ask me this
ought to be all the reason one could possibly need.</li>

<li> It assumes that HTTP servers ignore unknown arguments on arbitrary
headers (even those defined as not having arguments). If the arguments are
not ignored the conditional requests will not be conditional anymore
(invalid If-Modified-Since headers must be ignored, according to the HTTP
RFC), negating the reason for adding the If-Modified-Since header.</li>

<li> Even if a HTTP server knows about the length argument, the server
will often ignore the argument; calculating the length of a document is
often much too expensive, and often much more expensive than calculating a
Last-Modified date for a document.</li>

<li> The exact semantics of the length argument is not defined anywhere
(e.g. is it the length before or after a transfer encoding is applied, and
is it the length before or after line-ending conversions?). So, there is
no guarantee that any given HTTP client and HTTP server will implement the
same semantics for If-Modified-Since-with-length requests.</li>
</ol>

<p>In these situations (there is a perfectly clear document describing
what you may and may not do, and some idiot decides that it is quite
allright for his software to do something verboten), I am often very
much tempted to throw up my arms in despair, and declare the offending
software persona non grata.</p>