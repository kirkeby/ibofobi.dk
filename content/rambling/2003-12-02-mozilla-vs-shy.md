Id: tag:ibofobi.dk,2003-12-02:2003/12/02/mozilla-vs-shy
Title: Mozilla versus &shy;
Date: 2003-12-02

Mozilla and it's offspring are all very cool browsers, but there is
one thing they really ought to implement. Soft hyphenation.

Soft
hyphenation lets you give the browser hints about where it can break
long, continous words (i.e. anything not containing normal white-space).
So, for example, I can write
sheared.&#173;web.&#173;querystring.&#173;UnvalidatedInput.&#173;as_text,
and give the browser hints as to where it would be okay to break it up,
so the pieces can fit on one line.

This works by putting `&shy;` in your text, in those places where
it would okay, if the browser breaks a word into pieces when it becomes
too long to fit it's containing box. And, when the browser feels it has
break your carefully crafted long words into bits and pieces, it tacks a
hyphen on the end of all but the last of the pieces. Just like you would
expect from hyphenation.

So, for example the HTML behind the long method name above is

    sheared.&shy;web.&shy;querystring.&shy;UnvalidatedInput.&shy;as_text

And, in a browser handling &amp;shy; the code above and the long
method name in the paragraph above would both be split over several
lines and properly hyphenated. Alas, not in the world.

I mean, really, how difficult can it be? So, I don't know anything
about writing browsers or layout engines, but I do know that there has
been a feature request open since sometime in 1999, to implement this.
I just does not seem to happen.