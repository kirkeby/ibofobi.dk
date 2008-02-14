#!/usr/bin/env python

from resolver import resolve

from simpletal.simpleTAL import compileXMLTemplate
from simpletal.simpleTALES import Context

import sys
sys.path.append('blog')

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
    template.expand(context(ctx), stdout, outputEncoding='utf-8')

if __name__ == '__main__':
    import sys
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('--macros', action='append', default=['page.html'])
    parser.add_option('--context', action='append', default=[])
    opts, args = parser.parse_args()

    main(opts, sys.stdin, sys.stdout)
