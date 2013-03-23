document.onkeydown = function(event) {
    if(!event) var event = window.event;
    if(event.target) var targ = event.target;
    else if(event.srcElement) var targ = event.srcElement;
    if(targ.nodeType == 3) // defeat Safari bug
        targ = targ.parentNode;
    var tn = targ.tagName.toLowerCase();
    if(tn == 'input' || tn == 'textarea')
        return;
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
        if(child && child.tagName == 'link' && child.rel.toLowerCase() == rel)
            return child;
}
