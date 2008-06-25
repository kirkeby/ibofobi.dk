#!/usr/bin/env python

import os
from operator import itemgetter
from time import strptime
from time import mktime
from time import gmtime
from datetime import datetime
from markdown import markdown

here = os.path.dirname(__file__)
index_path = os.path.join(here, 'index')

def parse_time(stamp):
    t = gmtime(mktime(strptime(stamp, '%Y-%m-%d:%H:%M:%S')))
    return datetime(t.tm_year, t.tm_mon, t.tm_mday,
                    t.tm_hour, t.tm_min, t.tm_sec)

def read_index():
    '''Read the blog index and return a dictionary mapping external
    post-names to their meta-data.'''
    idx = {}
    
    for line in open(index_path):
        stamp, tag, name = line.strip().split('\t')
        stamp = parse_time(stamp)
        idx[name] = {
            'key': name,
            'name': stamp.strftime('%Y/%m/') + os.path.basename(name),
            'stamp': stamp,
            'date': stamp.strftime('%Y-%m-%d'),
            'path': os.path.abspath(os.path.join(here, name)),
            'tag': tag,
        }

    return idx
    
def _read_post(path):
    '''Read a single post, not including the meta-data in the index.'''
    post = {}
    post['source'] = open(path).read()
    lines = post['source'].split('\n', 2)
    post['title'] = lines[0].strip()
    post['text'] = lines[-1].strip().decode('utf-8')
    post['html'] = markdown(post['text'])
    return post

def read_post(name):
    '''Read a blog post (given its external name), updating the index.'''
    
    post = index[name]
    post.update(_read_post(post['path']))

    for rel in ['next', 'previous']:
        if post.has_key(rel):
            post[rel].update(_read_post(post[rel]['path']))

    return post

index = read_index()

sorted = index.values()
sorted.sort(key=itemgetter('stamp'), reverse=True)

next = None
for post in sorted:
    if next:
        post['next'] = next
        next['previous'] = post
    next = post

def recent():
    return [ read_post(post['key']) for post in sorted[:5] ]
def all():
    return [ read_post(post['key']) for post in sorted ]

info = {
    'url': 'http://ibofobi.dk/blog/',
    'title': 'about:me',
    'author': 'Sune Kirkeby',
}
