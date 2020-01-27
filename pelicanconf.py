#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Kenneth R. Farr III"
SITENAME = "farr.ai"

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

STATIC_PATHS = ["media"]

MARKDOWN = {
    "extension_configs": {"markdown.extensions.codehilite": {"css_class": "highlight"}, "markdown.extensions.extra": {}, "markdown.extensions.meta": {}, "markdown.extensions.toc": {},},
    "output_format": "html5",
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()  # (('Pelican', 'http://getpelican.com/'),
# ('Python.org', 'http://python.org/'),
# ('Jinja2', 'http://jinja.pocoo.org/'),
# ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/kfarr3"),
    ("Twitter", "https://twitter.com/BittahWizard"),
    ("LinkedIn", "https://www.linkedin.com/in/kenfarr/"),
)

TYPOGRIFY = True
DEFAULT_PAGINATION = 6

THEME='gum'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

