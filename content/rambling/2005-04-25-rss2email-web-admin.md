Id: tag:ibofobi.dk,2005-04-25:/blog/archive/2005/04/25/rss2email-web-admin/
Title: rss2email web administration
Date: 2005-04-25

I use <a href='http://www.aaronsw.com/2002/rss2email/'>rss2email</a> to
read blogs of various people. Combined with gmail rss2email is a brilliant
way to read blogs. But, for a long time I have missed an easier way than
<tt>ssh ibofobi.dk r2e add http://some.blog</tt> when adding new feeds.
So, I decided to write a quick little rss2email web admin-interface. You
can get it at <tt>http://mel.ibofobi.dk/~sune/r/r2eadmin.git</tt>.

As a bonus, here is a bookmarklet to <a
href="javascript:q=location.href;void(open('http://woop.com/rss2email/find?url='+escape(q),'rss2email','toolbar=no,width=700,height=500'));"
title='rss2email web-admin subscribe bookmarlet'>subscribe</a>; you just
have to edit the URL.