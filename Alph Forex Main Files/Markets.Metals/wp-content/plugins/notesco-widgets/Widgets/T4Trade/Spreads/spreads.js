'use strict';

window.addEventListener('load', function () {
  if (document.querySelector('.tabsArea') !== null) {
    spreads();
  }
});

function spreads() {
  const triggers = document.querySelectorAll('.tab-trigger');

  const expand = document.querySelectorAll('.tab-btn');

  const search = document.querySelector('.searchTable');

  /*  ---  Toggling Tabs  --- */
  if (typeof triggers[0] === 'undefined') {
    return;
  }

  triggers[0].classList.add('current');

  document.querySelectorAll('.tab-content')[0].classList.add('current');

  triggers.forEach(function (trigger) {
    trigger.addEventListener('click', function () {
      document.querySelectorAll('.tab-content').forEach(function (e) {
        e.classList.remove('current');
      });

      triggers.forEach(function (e) {
        e.classList.remove('current');
      });

      document
        .querySelector('.tab-content[data-tab="' + trigger.dataset.tab + '"]')
        .classList.add('current');
      trigger.classList.add('current');
    });
  });

  /*  ---  Adding Search for Tables  ---  */
  search.addEventListener('keyup', function () {
    searchInTables(search);
  });

  /*  ---  Expand hidden rows  ---  */
  expand.forEach((btn) => {
    btn.style.display = 'none';

    setTimeout(function () {
      if (
        btn.previousElementSibling.clientHeight <
        btn.previousElementSibling.querySelector('table').clientHeight
      ) {
        btn.style.cssText = 'null';
      }
    }, 750);

    btn.addEventListener('click', (e) => {
      const btn = e.currentTarget;

      const table = e.currentTarget.previousElementSibling;

      if (btn === null || table === null) {
        return;
      }

      if (btn.classList.contains('expanded') === false) {
        btn.classList.add('expanded');
        btn.innerHTML = 'Collapse Table <i class="fas fa-chevron-up"></i>';
        table.classList.add('expanded');
        return; // clastList is a live list
      }

      if (btn.classList.contains('expanded') === true) {
        btn.classList.remove('expanded');
        btn.innerHTML = 'Expand full List <i class="fas fa-chevron-down"></i>';
        table.classList.remove('expanded');
        return; // clastList is a live list
      }
    });
  });
}

function searchInTables(input) {
  const tabsArea = document.querySelector('.tabsArea');
  const rows = tabsArea.querySelectorAll('table tr'),
    filter = input.value.toUpperCase();
  rows.forEach(function (row) {
    const td = row.querySelector('td');
    if (td) {
      let txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  const xhttp = new XMLHttpRequest();
  let row_body = '';
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      const el = document.querySelector('.table.forApi');
      if (el === null) {
        return;
      }
      const json = JSON.parse(this.responseText);
      const tab_head =
        '<thead>' +
        '<tr><th><b>Symbol</b></th>' +
        '<th><b>Long Rate in Points<sup>2</sup></b></th>' +
        '<th><b>Short Rate in Points<sup>2</sup></b></th></tr>' +
        '</thead>';
      for (let i in json) {
        let pair = [i];
        let swap_long = json[i]['SWAP_LONG'];
        let swap_short = json[i]['SWAP_SHORT'];
        let description = json[i]['DESCRIPTION'];

        row_body += '<tr>';
        row_body += '<td><b>' + pair + '</b><br>' + description + '</td>';
        row_body += '<td>' + swap_long + '</td>';
        row_body += '<td>' + swap_short + '</td>';
        row_body += '</tr>';
      }
      document.querySelector('.table.forApi').innerHTML =
        '<table>' + tab_head + row_body + '</table>';
    }
  };
  xhttp.open(
    'GET',
    'https://api.ironfx.com/swaps/?filter=' + window.t4trade_api_filter,
    true
  );
  xhttp.send();
});