Title: HTTPMiddleware
Date: 2005-09-29

This Django middleware helps your site handle some common features of the HTTP protocol. First off it adds a `Date` and `Content-Length` header to your responses, if they are not already set. Also, it clears the content from your response object, if the request was for the response headers only.

The last thing it does is handle conditional GET requests. If the request has `If-None-Match` this is compared to the response `ETag`, and if they match the response is turned into a not modified response. Likewise for the `If-Modified-Since`&#8211;`Last-Modified` header-pair.

The middleware is available as `ibofobi.middleware.http.HTTPMiddleware` in the ibofobi subversion-repository `http://mel.ibofobi.dk/~sune/r/ibofobi.git`. Enjoy.