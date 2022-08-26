$.cookie=function(name,value,days){if(value!==undefined){if(value===null){days=-1;}
if(days){var date=new Date();date.setTime(date.getTime()+(days*24*60*60*1000));var expires="; expires="+date.toGMTString();}
else var expires="";document.cookie=name+"="+encodeURIComponent(value)+expires+"; path=/";return value;}
var nameEQ=name+"=";var ca=document.cookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' ')c=c.substring(1,c.length);if(c.indexOf(nameEQ)==0)return decodeURIComponent(c.substring(nameEQ.length,c.length));}
return null;}