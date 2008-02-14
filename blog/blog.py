#!/usr/bin/env python

import os
from time import strptime
from datetime import datetime

here = os.path.dirname(__file__)
index_path = os.path.join(here, 'index')

def parse_time(stamp):
    t = strptime(stamp, '%Y-%m-%d:%H:%M:%S')
    return datetime(t.tm_year, t.tm_mon, t.tm_mday,
                    t.tm_hour, t.tm_sec, t.tm_min)

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

index = read_index()
    
def read_post(name):
    '''Read a blog post (given its external name).'''
    post = index[name].copy()
    post['source'] = open(post['path']).read()
    lines = post['source'].split('\n', 2)
    post['title'] = lines[0].strip()
    post['text'] = lines[-1].strip()
    return post
