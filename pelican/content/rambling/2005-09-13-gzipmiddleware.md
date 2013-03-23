Title: GZipMiddleware
Date: 2005-09-13

I just implemented a GZipMiddleware for Django,
so now you can enjoy the bandwidth-saving goodness
that is gzip without
using django.middleware.cache (actually, since
Djangos cache-middleware is oblivious to the Vary
header, it will _not_ work with GZipMiddleware...)

It is in ibofobi.middleware.gzip under
`http://mel.ibofobi.dk/~sune/r/ibofobi.git`. Enjoy.