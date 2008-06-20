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
            'name': stamp.strftime('%Y/%m/%d/') + os.path.basename(name),
            'stamp': stamp,
            'path': os.path.abspath(os.path.join(here, name)),
            'tag': tag,
        }

    return idx
    
def read_post(name):
    '''Read a blog post (given its external name).'''
    post = index[name].copy()
    post['source'] = open(post['path']).read()
    lines = post['source'].split('\n', 2)
    post['title'] = lines[0].strip()
    post['text'] = lines[-1].strip().decode('utf-8')
    post['html'] = markdown(post['text'])
    return post

index = read_index()

all = index.values()
all.sort(key=itemgetter('stamp'), reverse=True)

recent = [ read_post(post['key']) for post in all[:5] ]

info = {
    'url': 'http://ibofobi.dk/blog/',
    'title': 'about:me',
    'author': 'Sune Kirkeby',
}
