Title: Kata Thirteen
Date: 2003-12-01

<p> Paraphrasing <a
href='http://www.pragprog.com/pragdave/Practices/Kata/KataThirteen.rdoc,v'>Kata
Thirteen</a>:</p>
<blockquote><p>Your mission, should you choose to accept it, is to count
lines of actual code in Java source-code.</p></blockquote>

<p>Let us see, the real task is to remove comments from the source code,
anything left after that must be actual code-lines. So, this should
suffice (assuming GNU <code>cpp(1)</code>):</p>

<blockquote><p><code>
cpp -fpreprocessed -P - - \<br />
| grep -v '^[[:space:]]*$' \<br />
| wc -l
</code></p></blockquote>

<p>No need to complicate the task with a real programming language, when
we have all the tools available.</p>