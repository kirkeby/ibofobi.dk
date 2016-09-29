Id: tag:ibofobi.dk,2005-04-19:/blog/archive/2005/04/19/links-and-keyboard-navigation/
Title: Next/previous links and gmail-style keyboard navigation
Date: 2005-04-19

I've now added `rel='next'` and `rel='previous'`-links and visible
next/previous links to the blog-post pages. Also, I added <a
href='http://gmail.google.com/support/bin/answer.py?answer=6594'
title='Gmail help - Keyboard shortcuts'>gmail-style
keyboard-navigation</a> to the entire site. It works for `'u'` for Up,
`'j'` for Previous and `'k'` for Next. It was pretty simple to implement:

    document.onkeydown = function(event) {
        if(!event) var event = window.event;
        if(event.keyCode == 85 /* 'u' */) {
            document.location = '..';
        } else if(event.keyCode == 74 /* 'j' */) {
            var e = find_link_rel('previous');
            if(e) document.location = e.href;
        } else if(event.keyCode == 75 /* 'k' */) {
            var e = find_link_rel('next');
            if(e) document.location = e.href;
        }
    };
    function find_link_rel(rel)
    {
        var children = document.getElementsByTagName('link');
        var i, child;
        for(i=0; i<children.length; ++i, child=children.item(i))
            if(child && child.tagName == 'link' && child.rel == rel)
                return child;
    }