Id: tag:ibofobi.dk,2005-09-09:/blog/archive/2005/09/09/three-small-django-apps/
Title: Three small Django apps
Date: 2005-09-09

I've just converted this site to <a href='http://www.djangoproject.com/'>Django</a>.
In the process I wrote a few small apps, two of which are in a state, where others might
use them (or improve them, until they become useful :).

The first app is a blog, with posts and categories (which drives this blog...). It's still not feature-complete (I want comments and drafts at the very least), but it works. One nice feature, is that the posts are formatted using <a href='http://daringfireball.net/projects/markdown/'>Markdown</a>.

The second app is a personal calendar-type-thingie, it's stille very rough around the edges, but it helps me to keep track things I have to remember...

They live in `http://mel.ibofobi.dk/~sune/r/ibofobi.git` under `src/apps/`, I still haven't gotten around to writing a `setup.py`, and the templates need a bit of cleaning up.