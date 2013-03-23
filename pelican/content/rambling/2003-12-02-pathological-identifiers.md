Title: Line-wrapping when soft hyphenation is wrong
Date: 2003-12-02

<div class='update'>
<p><strong>Update:</strong>
<span class='timestamp'>(31. december 2003)</span>
It seems my reading of the HTML 4 specification is not universal.  And,
to make matters worse, neither of the HTML, Unicode or ISO Latin 1
standards agree on what the <acronym title='soft
hyphenation'>shy</acronym> character should mean. See <a
href='http://www.cs.tut.fi/~jkorpela/shy.html'>Soft Hyphenation (SHY) -
a hard problem?</a> for the gory details.</p>
</div>

<p>There is this nifty little HTML character entity, &amp;shy;, which
lets one give soft hyphenation hints to browsers. But, when writing
documentation for code, one sometimes needs write really, unbelivably,
imagination-strainingly long identifiers. And, having them hyphenated,
when split over multiple lines might not be what one wants (at least, it
is not what I want).</p>

<h3>Exempli Gratia</h3>

<p>Here is an example of what might happen, if the browser cannot break
your long identifier into little bits and pieces:</p>

<blockquote style='width: 50%; overflow: scroll;'><p><code>
sheared.web.querystring.UnvalidatedInput.as_text
</code></p></blockquote>

<p>So, when you has to type in a pathologically long identifier from a
program, and you want it to gracefully break in two on the middle, what
can you do?</p>

<h3>One solution</h3>

<p><em>I have only tested this with Mozilla Firebird 0.7.1, it might not
work on any other browsers.</em></p>

<p>Those of us living in CSS-land can actually do something. Rendering a
white-space with zero <code>font-size</code> produces no visible break
when inside a word. But, if you place such a zero-width white-space
inside a word, the word is happily chopped into pieces where you
inserted it.</p>

<p>So, this goes into your stylesheet:</p>

<blockquote><p><code>
.shy {
    font-size: 0;
}
</code></p></blockquote>

<p>This is your HTML:</p>

<blockquote><p><code>
sheared.&lt;span class='shy' /&gt;
&lt;/span&gt;web.&lt;span class='shy' /&gt;
&lt;/span&gt;querystring.&lt;span class='shy' /&gt;
&lt;/span&gt;UnvalidatedInput.&lt;span class='shy' /&gt;
&lt;/span&gt;as_text
</code></p></blockquote>

<p>And, suddenly it renders beautifully:</p>

<blockquote style='width: 50%; overflow: scroll;'><p><code>
sheared.<span class='shy'> </span>web.<span class='shy'> </span>querystring.<span class='shy'> </span>UnvalidatedInput.<span class='shy'> </span>as_text
</code></p></blockquote>