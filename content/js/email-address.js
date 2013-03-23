var ords = [109, 0x69, 0x67, 64, 105, 98, 111, 102, 111, 98, 105, 46, 100, 107];
var addy = '';
for(i in ords) {
    addy = addy + String.fromCharCode(ords[i]);
}

var a = document.createElement('a');
a.href = 'mailto:' + addy;
a.appendChild(document.createTextNode(addy));

var old = document.getElementById('email-address');
old.parentNode.replaceChild(a, old);
