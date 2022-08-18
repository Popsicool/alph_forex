'use strict';

class LiveChat {
  get group() {
    const groups = {
      english: 127,
      french: 128,
      german: 135,
      italian: 136,
      spanish: 139,
    };

    const trpClass = document.body.classList
      .toString()
      .split(' ')
      .filter((v) => v.includes('translatepress'))
      .toString();

    if (trpClass === '') {
      console.error('livechart: unabel to translatepress class!');
      return groups.english;
    }

    const regex = trpClass.match(/translatepress-(?<lang>[A-z_]+)/);

    if (regex === null) {
      console.error('livechat: regex has failed!');
      return groups.english;
    }

    const lang = regex.groups.lang;

    if (lang === 'fr_FR') {
      return groups.french;
    }

    if (lang === 'de_DE') {
      return groups.german;
    }

    if (lang === 'it_IT') {
      return groups.italian;
    }

    if (lang === 'es_ES') {
      return groups.spanish;
    }

    return groups.english;
  }

  init(license, group) {
    window.__lc = window.__lc || {};
    window.__lc.license = license;
    window.__lc.group = group;
    (function (n, t, c) {
      function i(n) {
        return e._h ? e._h.apply(null, n) : e._q.push(n);
      }
      var e = {
        _q: [],
        _h: null,
        _v: '2.0',
        on: function () {
          i(['on', c.call(arguments)]);
        },
        once: function () {
          i(['once', c.call(arguments)]);
        },
        off: function () {
          i(['off', c.call(arguments)]);
        },
        get: function () {
          if (!e._h)
            throw new Error(
              "[LiveChatWidget] You can't use getters before load."
            );
          return i(['get', c.call(arguments)]);
        },
        call: function () {
          i(['call', c.call(arguments)]);
        },
        init: function () {
          var n = t.createElement('script');
          (n.async = !0),
            (n.type = 'text/javascript'),
            (n.src = 'https://cdn.livechatinc.com/tracking.js'),
            t.head.appendChild(n);
        },
      };
      !n.__lc.asyncInit && e.init(), (n.LiveChatWidget = n.LiveChatWidget || e);
    })(window, document, [].slice);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const chat = new LiveChat();

  const group = chat.group;

  const license = '1486502';

  chat.init(license, group);
});
