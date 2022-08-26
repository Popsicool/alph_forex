$(document).ready(function(){function getCookieValue(cname){var name=cname+"=";var ca=document.cookie.split(";");for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==" "){c=c.substring(1);}
if(c.indexOf(name)!=-1){return c.substring(name.length,c.length);}
return"";}}
function setCookieValue(c_name,value,expiredays){var exdate=new Date();exdate.setDate(exdate.getDate()+expiredays)
document.cookie=c_name+"="+escape(value)+"; path=/"+((expiredays==null)?"":"; expires = "+exdate.toGMTString());}
function getSiteFromUrl(url){var urlInfo=url.split(".");if(typeof urlInfo[1]!='undefined'){return urlInfo[1];}
return'';}
var hostDomain=getSiteFromUrl(window.location.host);var referrerDomain=getSiteFromUrl(document.referrer);var currentReferrerUrl=getCookieValue("referrer_url");if(referrerDomain!=''&&hostDomain!=referrerDomain&&currentReferrerUrl==''){setCookieValue("referrer_url",document.referrer,30);}});