# -*- coding: utf-8 -*-
"""
    Chronological Article Links for Pelican
    =======================================

    Will Hart [github: @will-hart]

    A plugin to add 'previous_url' and 'next_url' links to an article.
    These links are determined in chronological order, and can be used
    in a template as follows:

    Settings
    --------
    To enable, add

        from pelican.plugins import chronological_links
        PLUGINS = [chronological_links]

    to your settings.py.

    Usage
    -----

    You can use this plugin in your templates like this:

        {% if article.previous_url %}
        <a href="{{article.previous_url}}">&lt; {{article.previous_title}}</a>
        {% endif %}

    and
        {% if article.next_url %}
        <a href="{{article.next_url}}">{{article.next_title}} &gt;</a>
        {% endif %}

"""

from pelican import signals


def generate_link_settings(pelican):
    """
    Check the settings and apply defaults
    """
    if 'LINKS_REVERSE_CHRONOLOGICAL' not in pelican.settings:
        pelican.settings['LINKS_REVERSE_CHRONOLOGICAL'] = True


def generate_chronological_links(generator):
    """
    Generates the next and previous links in overall chronological order
    for the articles in the passed generator
    """
    previous_article = None

    # work out which order to generate links in
    if generator.settings['LINKS_REVERSE_CHRONOLOGICAL']:
        article_iter = generator.articles
    else:
        article_iter = reversed(generator.articles)

    # generate the links
    for article in article_iter:
        if previous_article is not None:
            previous_article.next_url = article.url
            previous_article.next_title = article.title
            article.previous_url = previous_article.url
            article.previous_title = previous_article.title
        previous_article = article


def register():
    """
    Register the plugin
    """
    signals.initialized.connect(generate_link_settings)
    signals.article_generator_finalized.connect(generate_chronological_links)
