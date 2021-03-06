Id: tag:ibofobi.dk,2005-11-08:/blog/archive/2005/11/08/django-doctest/
Title: Django doctest framework
Date: 2005-11-08

Inspired by Hugo's post [A Test Framework for Django](http://hugo.muensterland.org/2005/10/31/a-test-framework-for-django/) and
his [DjangoTesting](https://simon.bofh.ms/cgi-bin/trac-django-projects.cgi/wiki/DjangoTesting) framework I wrote `ibofobi.utils.test`. Another Django test-framework which provides the same features plus request/response testing also, but in a different way that I like better.

The big differences are that I built it on top of doctest instead of unittest and the fixtures are written in YAML not Python code. I think doctest is a lot nicer to work with than the Java'ish unittest module; and YAML is good for simple data-structures such as the fixtures. Also, I implemented simple request/response tests on top of [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), which is so cool I almost cannot belive it :). Also, the tests are run in an in-memory sqlite database, inspired by Ian Maurer's [Django Unit Testing](http://itmaurer.com/blog/?p=2) post.

To test an application you first create a `fixtures` directory and put your fixtures in there as `*.yml`, for example in `ibofobi/apps/blog/fixtures/blog.yml` I have:

    posts:
        hello_world:
            title: Hello, World!
            slug: hello-world
            posted: 1979-7-7 23:12:00.0
            listed: true
            content: A lot of content should go here.

The fixtures are grouped by model-name and each fixture has a name, which you can use in the doctests to refer to the database-object. When you have some fixtures you create a `tests` module for your doctests, so in `ibofobi/apps/blog/tests/__init__.py` I have:

    """
    >>> hello_world.title
    'Hello, World!'
    """

This asserts that the title of the post created from the fixture `hello_world` has the expected title. Now, I want to test that the month-archive view works, so I also have this in the tests-module:

    """
    >>> browser.go('/archive/1979/07/')
    >>> browser.soup.li.a.string
    'Hello, World!'
    """

The `browser` object is a helper which invokes the Django handler and parses
the result with `BeautifulSoup`.

If you want to try `ibofobi.utils.test` get it with:

    git clone http://mel.ibofobi.dk/~sune/r/ibofobi.git

And run the `django-test` script, which will run tests in each application in 
`INSTALLED_APPS`. Both `PyYAML` and `BeautifulSoup` are bundled, so you don't have to install the separately.

Alas, the tests are always run in an in-memory sqlite database, so you will need sqlite working for Django. I will fix this wart so the tests can be run with other database-backends
in one-shot databases like with `django/tests/runtests.py`.