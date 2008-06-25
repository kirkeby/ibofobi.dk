#!/usr/bin/env python

from xml.sax.saxutils import escape
from markdown import markdown

template = '''\
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html metal:use-macro='macros/page'>
<head>
  <title metal:fill-slot='title'>%(title)s</title>
</head>
<body>
  <h1 metal:fill-slot='heading'>%(title)s</h1>
  <div metal:fill-slot='content'>%(content)s</div>
</body>
</html>
'''

def main(stdin, stdout):
    lines = stdin.readlines()
    title = escape(lines[0].strip())
    text = ''.join(lines[2:]).decode('utf-8')
    content = markdown(text).encode('utf-8')
    if not content:
        # 14:45 < kirkeby> !lart markdown.py
        # 14:47 < kirkeby> try: foo except: log('Buhuh!') ; return ''
        # 14:47 < kirkeby> *GRR*
        raise AssertionError('DIE, MARKDOWN, YOU STUPID FUCKING CUNT!')

    print >> stdout, template % locals()

if __name__ == '__main__':
    import sys
    main(sys.stdin, sys.stdout)
