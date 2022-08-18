(function(d, s, id, c) {
    var js, rC = [],
        uRC = [],
        r = 0;
    Array.from(document.querySelectorAll('[class*="stjr- "]')).forEach(r => {
        rC = [...rC, ...Array.from(r.classList).filter((cl) => {
            return /^stjr-/.test(cl);
        })]
    });
    uRC = [...new Set(rC)];
    t = d.getElementsByTagName(s)[0];
    js = d.createElement(s);
    js.id = id;
    js.src = 'https://www.sitejabber.com/js/v2/623219687d595/widgets.js' + (uRC.length ? '?widget-classes=' + uRC.join("|") : '?widget- classes=stjr- base') + '';
    js.onload = js.onreadystatechange = function() {
        if (!r && (!this.readyState || this.readyState[0] == 'c')) {
            r = 1;
            c();
        }
    };
    t.parentNode.insertBefore(js, t);
}(document, 'script', 'sj-widget', function() {}));