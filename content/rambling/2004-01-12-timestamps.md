Id: tag:ibofobi.dk,2004-01-11:2004/01/11/timestamps
Title: Relative timestamps
Date: 2004-01-12

<p>Today I have been doing some minor hacking on my blog.
I changed the visible timestamp on the rants from absolute to
relative; the absolute timestamp is now a <code>title</code> attribute
on the timestamp <code>span</code> (i.e. the asolute timestamp is shown
as a tooltip, if you hover your mouse over the relative timestamp). In
the same move I went from displaying the absolute timestamps in <abbr
title='Central European Time'>CET</abbr> to <abbr
title='Greenwich Mean Time'>GMT</abbr>. This goes for all pages but the
archive, where absolute timestamps still rule supreme.</p>

<p>The <a
href='http://ibofobi.dk/svn/Sheared/src/sheared/python/time_since.py'
title='sheared.python.time_since Python module'>code</a> to calculate
and format the relative timestamps is naturally
available in <span title='Python'>my favourite computer dialect</span>
(provided you don't start foaming around the mouth when I mention the
<abbr title='General Public License'>GPL</abbr> (speaking of which, have
I missed all the obvious jokes about the <q>General Pubic License</q>
(sic) being viral, or are they just less obvious than I think?!)).</p>