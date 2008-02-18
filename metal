#!/usr/bin/env python

from resolver import resolve

from simpletal.simpleTAL import compileXMLTemplate
from simpletal.simpleTALES import Context

from cStringIO import StringIO

import sys
sys.path.append('blog')

xhtml_doctype = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
'''

def load_template(file_or_path):
    if isinstance(file_or_path, str):
        file_or_path = open(file_or_path)
    return compileXMLTemplate(file_or_path)
def load_macros(path):
    return load_template(path).macros

def context(quark):
    ctx = Context(allowPythonPath=True)
    ctx.globals.update(quark)
    return ctx

def main(opts, stdin, stdout):
    macros = {}

    for macro_path in opts.macros:
        macros.update(load_macros(macro_path))

    ctx = {
        'macros': macros,
    }
    for expr in opts.context:
        key, path = expr.split('=')
        ctx[key] = resolve(path)

    template = load_template(stdin)
    result = StringIO()
    template.expand(context(ctx), result, outputEncoding='utf-8')
    result = result.getvalue().replace('<?xml version="1.0"?>', '')
    
    print '<?xml version="1.0" encoding="utf-8"?>'
    if opts.xhtml_doctype:
        print xhtml_doctype,
    print result,

if __name__ == '__main__':
    import sys
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('--macros', action='append', default=['page.html'])
    parser.add_option('--context', action='append', default=[])
    parser.add_option('--xhtml-doctype', action='store_true')
    opts, args = parser.parse_args()

    main(opts, sys.stdin, sys.stdout)
