$(document).ready(function(){$('#export_pdf').click(function(){$.ajax({url:'/json/transaction-report.json',async:false,cache:false,type:"GET",data:{},success:function(data){if(data===''){}}});});$('#account').change(function(){var account=$(this).val();setUrlParamAndGo('account',account);});$('.date').change(function(){set_date_filter();});$('#date_to').datepicker('setStartDate',$('#date_from').val());});function setUrlParamAndGo(name,val){var url=new URL(window.location.href);url.searchParams.set(name,val);window.location.replace(url.href);}
function set_date_filter()
{var date_from=$('#date_from').val();var date_to=$('#date_to').val();if(date_from.length>5&&date_to.length>5){var from=toDate(date_from);var to=toDate(date_to);if(from<=to){var url=new URL(window.location.href);url.searchParams.set('date_from',date_from);url.searchParams.set('date_to',date_to);window.location.replace(url.href);}}}
function toDate(dateStr){var parts=dateStr.split("/");return new Date(parts[2],parts[1]-1,parts[0]);}