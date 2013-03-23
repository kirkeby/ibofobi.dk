Id: tag:ibofobi.dk,2005-10-14:/blog/archive/2005/10/14/django-page-view-counter/
Title: Django page-view counter
Date: 2005-10-14

`ibofobi.apps.fresh` is a page-view counter for your Django site. It collects the statistics with a small JavaScript which calls back to your server for every page-view; inspired by [Mint](http://haveamint.com).

For now the only view I have is a simple referrer tracker, but all the data (timestamp, URL, referrer and user-agent) is all there in a neat little model, so more can easily be added.

See [the trac page](http://code.ibofobi.dk/public/wiki/ProjectIbofobiFresh).

P.S. Kudos to anyone who can come up with a better name, it was not named in my most inspired moment...