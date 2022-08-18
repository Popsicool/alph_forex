var url_string = window.location.href;
var path = window.location.pathname;
var url = new URL(url_string);
var cookieValues = {};
const entries = url.searchParams.entries();

for (const entry of entries) {
  const param = {
    name: entry[0],
    value: entry[1],
  };

  // include parameters utm_*
  if (param.name.startsWith('utm_')) {
    cookieValues[param.name] = param.value;
  }

  // add extra parameters here (precise match)
  const extraParams = ['gclid', 'fbclid', 'msclkid'];

  // additional parameters (precise match)
  for (let i = 0; i < extraParams.length; i++) {
    const extraParam = extraParams[i];

    if (param.name === extraParam) {
      cookieValues[param.name] = param.value;
    }
  }
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  var expires = 'expires=' + d.toUTCString();
  document.cookie =
    cname + '=' + JSON.stringify(cvalue) + ';' + expires + ';path=/';
}

//This will check if the object is empty
if (JSON.stringify(cookieValues) !== '{}') {
  const expire = 30; // days

  setCookie('UrlOriginalQueryParameters', cookieValues, expire);
}
