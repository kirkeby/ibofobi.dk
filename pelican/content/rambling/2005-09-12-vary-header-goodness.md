Title: Vary-header goodness
Date: 2005-09-12

The XHTMLAsHTMLMiddleware class now sets (or
updates) the Vary response-header, to indicate
to HTTP-caches that the response might change,
based on the content of the Accept request-header.

Now, I just need to hack the Django cache-middleware,
to set, understand and obey the Vary-header, so I can
use it with XHTMLAsHTMLMiddleware.