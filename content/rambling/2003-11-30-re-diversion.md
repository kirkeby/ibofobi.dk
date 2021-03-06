Id: tag:ibofobi.dk,2003-11-30:/blog/archive/2003/11/30/re-diversion/
Title: Re: A Diversion
Date: 2003-11-30

In <a
href='http://www.pragprog.com/pragdave/Practices/Kata/KataFifteen.html,v'>A
Diversion</a> PragDave poses the following kata:
<blockquote><p>Think of binary numbers: sequences of 0's and 1's.
How many n-digit binary numbers are there that don't have two adjacent 1
bits? For example, for three-digit numbers, five of the possible eight
combinations meet the criteria:
000, 001, 010,
<span class='strike'>011</span>,
100, 101,
<span class='strike'>110</span>,
<span class='strike'>111</span>.
What is the number for sequences of length 4, 5, 10, n?</p></blockquote>

Having given the answer for 3-digit binary numbers, he also asks why
this relationship exists. Well, I think I can answer that. It is simple
combinatorics. Since typesetting math in HTML is such a pain, I will
just post the LaTeX note I wrote to explain the relationship to myself:

<blockquote><p><code>\documentclass{article}<br />
<br />
\title{Re: A Diversion}<br />
\author{Sune Kirkeby}<br />
\date{30. November 2003}<br />
<br />
\begin{document}<br />
\newcommand{\bicoef}[2]{
    \left(\begin{array}{c}
    #1\\#2
    \end{array}\right)}
<br />
\maketitle<br />
<br />
Let $a$ be the number of $n$-digit
binary numbers with exactly $k$ $1$
bits, where no two $1$-bits are
adjacant. Then<br />
$$a = \bicoef{n-k+1}{k} $$<br />
<br />
Let $b$ be the number of $n$-digit
binary numbers that do not have two
adjacant $1$ bits. Then <br />
$$b = \sum_{k=0}^n \bicoef{n-k+1}{k}$$<br />
<br />
For $n=3$:<br />
$$\bicoef{3-0+1}{0}
+ \bicoef{3-1+1}{1}
+ \bicoef{3-2+1}{2}
+ \bicoef{3-3+1}{3}<br />
= 1 + 3 + 1 + 0 = 5$$<br />
\end{document}</code></p></blockquote>