Id: tag:ibofobi.dk,2003-11-14:2003/11/14/amanda-xfree86
Title: XFree86 troubles
Date: 2003-11-14

<p>The final episode in my epic struggle to get decent graphics on my
aeon-old laptop.</p>

<p>I am the happy owner of an old Compaq Armada 4120 laptop with a
TFT-display. Last week I finally managed to find the magic combination
of <code>ModeLine</code>s and other arcane configuration-options, that
convince the laptop to run 800x600 at 16bpp. Actually, it runs 800x570
because the bottom 30 or so odd pixels are borked in this setup, but
that is beside the point.</p>

<p>Since it is a really old laptop I setup gdm on my workstation to do X
query-magic, so the workstation runs all the X clients, which means I
can run Mozilla Firebird and gaim even though I am on my 100 MHz laptop
lying lazily in bed :-).</p>

<p>Have an old Armada 4120 with TFT-display but ix'nay on the 800x600 at
16bpp? Maybe my<a
href='http://ibofobi.dk/download/XF86Config-4.arven'>XFree86
configuration</a> can help you.</p>