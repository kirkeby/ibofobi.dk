Id: tag:ibofobi.dk,2005-11-19:/blog/archive/2005/11/19/xhtml--html-middleware-updated/
Title: XHTML-as-HTML middleware updated
Date: 2005-11-19

I've updated [XHTMLAsHTMLMiddleware](http://code.ibofobi.dk/public/wiki/XHTMLAsHTMLMiddleware)
to turn response content into HTML 4.01 Strict, instead of just munging
the Content-Type header. This should work better with software which expects
the quirks of HTML, such as `<br>` elements which have no end-tag.