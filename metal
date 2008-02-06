#!/usr/bin/env python

from simpletal.simpleTAL import compileXMLTemplate
from simpletal.simpleTALES import Context

def load_template(file_or_path):
    if isinstance(file_or_path, str):
        file_or_path = open(file_or_path)
    return compileXMLTemplate(file_or_path)
def load_macros(path):
    return load_template(path).macros

def main(opts, stdin, stdout):
    macros = {}

    for macro_path in opts.macros:
        macros.update(load_macros(macro_path))

    ctx = Context(allowPythonPath=True)
    ctx.globals.update({
        'macros': macros,
    })

    template = load_template(stdin)
    template.expand(ctx, stdout, outputEncoding='utf-8')

if __name__ == '__main__':
    import sys
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option('--macros', action='append')
    opts, args = parser.parse_args()

    main(opts, sys.stdin, sys.stdout)
