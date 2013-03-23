Title: Ubuntu vs sitecustomize.py
Tags: ubuntu, python, puppet

Sometimes it is almost like the Ubuntu developers go out of their way to annoy
the rest of the world, <a
href='https://bugs.launchpad.net/ubuntu/+source/python2.5/+bug/197219'> this
time</a> (for ancient values of "this time") the Python package-maintainer
decided to add a `sitecustomize` module to the Python standard library. This
is *not* what `sitecustomize` is for, `sitecustomize` is for "performing
arbitrary site-specific customizations".

So, puppet to the resuce:

    :::puppet
    file { ['/usr/lib/python2.7/sitecustomize.py',
            '/usr/lib/python2.7/sitecustomize.pyc',
            '/usr/lib/python2.7/sitecustomize.pyo']:
        ensure => removed,
    }
