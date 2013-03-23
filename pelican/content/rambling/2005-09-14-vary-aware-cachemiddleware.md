Title: Vary-aware CacheMiddleware
Date: 2005-09-14

I got around to hacking up a version of Djangos
cache-middleware, which understands and obeys the `Vary`
response-header. This means it will cache different
copies of the pages, based on what the request headers
are.

So, Firefox will get a XHTML page from the cache,
while IE will get an HTML page. And, I will get a page
with admin-links from the cache, while you will get a
page without admin-links.

This is good.

It's in `ibofobi.middleware.cache` under
`http://mel.ibofobi.dk/~sune/r/ibofobi.git`, now I just
need to figure out, if it is interesting enough to
include in the official distribution.