Title: Oh, dear (diary)!
Date: 2004-01-08

<p>Ok, I guess it's time for some Real Content(tm) from my side, so I
will try to write about things I have been up to lately. I will strive
to keep my gaze high above my navel, and hopefully write something that
someone out there might find interesting.</p>

<h3>New toy: Powerball</h3>

<p>Yup. I got myself a <a
href='http://www.powerballs.com/'>Powerball</a>. The producers of the
Powerballs claim that they help alleviate <abbr
title='Carpal Tunnel Syndrome'>CTS</abbr> and <abbr
title='Repeated Stress Injury'>RSI</abbr>, and I am pretty sure I suffer
from one of those. So, I am hoping playing with my new Powerball will
actually help me, because hurting in the wrists and arms from too much
computer work is no fun for me.</p>

<p>I will have to google a bit for information on how exactly this
wonderful toy will help me, and what the best way to train my wrists for
<kbd>l33t</kbd>-keyboard skillz is.</p>

<p>Oh.. Current RPM-record is 10,529.</p>

<h3>Hacking</h3>

<h4>about:me, Sheared and Entwine</h4>

<p>Lately almost all my <del>hacking</del> <ins>non-sleeping</ins> hours
have been spent on the backend for this here blog, my private RSS
aggregator and the backend software I build these things on (<a
href='http://ibofobi.dk/stuff/sheared/'>Sheared</a> and <a
href='http://ibofobi.dk/stuff/entwine/'>Entwine</a>). Noteable features
I have recently implemented:</p>

<ul>
<li>Support for conditional HTTP GET on the RSS feed.</li>
<li>A feedback form.</li>
<li>Automagically alerting myself when a 404 is served.</li>
</ul>

<h4>Jukebox</h4>

<p>I think I squashed a rather annoying bug in <a
href='http://ibofobi.dk/stuff/jukebox'>Jukebox</a>; the jukebox that I
start in <code>local.start</code> would shut down when XMMS
disconnected, so one would get a <q>Could not connect</q> error message
when asking XMMS to start playing again.</p>

<p>The fix was to wrap the client-connection writing in a
<code>try: except: break</code>-block; which is really weird, because
exceptions are <em>supposed</em> to be caught higher up in the
call-stack. Something is rotten in the state of my
exception-handling code :-(.</p>

<p><em>Note to self:</em> when running the jukebox undaemonized the
offending exception is caught and logged, but it mysteriously goes
astray when the jukebox is daemonized and the jukebox process shuts
down. Maybe you/I should look at what's up with exception logging when
the jukebox is daemonized? Alas, not now. I have books to read, and my
wrists hurt.</p>

<h3>Post Scriptum</h3>

<p>Not entirely sure I succeeded in staying away from navel-picking.
Then again, I am still practicing my blogging manners.</p>