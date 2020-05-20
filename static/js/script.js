
$(function ($) {
  var $window = $('.window'),
    $close = $('.close'),
    $minimize = $('.minimize'),
    $maximize = $('.maximize'),
    $searchBar = $('.searchBar'),
    $screenTab = $('.screenTab');

  //$window resize
  $window.resizable({
    handles: 'se',
    minWidth: 650,
    minHeight: 70
  });

  //Close $window
  $close.on('click', function () {
    alert('Window closed.');
  });

  //Minimize $window
  $minimize.on('click', function () {
    //alert('Window minimized.');
    $window.hide();
    $screenTab.show();
  });

  $screenTab.on('click', function () {
    $window.show();
    $screenTab.hide();
  });

  //Maximize $window
  function maxDisplay() {
    if ($(this).hasClass('active')) {
      $window.removeClass('full');
      $maximize.removeClass('active');
      $window.resizable('enable');
    } else {
      $window.addClass('full');
      $maximize.addClass('active');
      $window.resizable('disable');
    }
  }
  $maximize.click(maxDisplay);

  //Search functionality
  $('form').on('submit', function () {
    let question = $searchBar.val();
    switch ($searchBar.val()) {
      case '':
        alert('No URL was entered.')
        break;
      default:



        $.ajax({
          url: '/question',
          type: "post",
          contentType: "application/json",
          dataType: "json",
          data: JSON.stringify({
            "input_question": $searchBar.val()
          }),
          beforeSend: function () {
            $('#wiki_link').val('')
            $('#text_paragraphs').val('')
            $('#text_albert').val('')
          },
          complete: function () {
            console.log('here . ')
          }
        }).done(function (jsondata, textStatus, jqXHR) {
          console.log(jsondata);
          let wiki_link = jsondata['link'];
          let text_paragraphs = jsondata['text_paragraphs'];
          let answer = jsondata['answer'];



          var colors = Array("#fab7b7", "#5c2a9d", "#eb6383", "#77d8d8", "#fa744f", "#74d4c0", "#9a1f40");
          var color = colors[Math.floor(Math.random() * colors.length)];
          const div = document.createElement('div');
          div.className = 'publication';
          div.innerHTML = `
        <div class="card text-white mb-3" style="max-width: 50rem;margin-top: 50px; margin-left: 50px; background-color:`+ color + `">
        <div class="card-header" id="text_paragraphs" readonly>`+ question + `</div>
        <div class="card-body">
          
          <h5 class="card-title" for="wiki_link" id="wiki_link" readonly style="margin-bottom: 2.75rem;">`+ answer + `</h5>
          <a href="`+ wiki_link + `" style="color: white;text-decoration-line: underline;">Wikipedia Link</a>
          <p class="card-text text-white">`+ text_paragraphs + `</p>
        </div>
      </div>
      `;
          var eElement = document.getElementById('windowDisplay');
          eElement.insertBefore(div, eElement.firstChild);

        }).fail(function (jsondata, textStatus, jqXHR) {
          console.log(jsondata['answer'])
          alert(jsondata['responseText'])
        });








        alert('We are now searching for your question .. Please wait ')

    }
    return false;
  });

  //Window resize
  $(window).on('resize', function () {
    if ($(window).width() <= 720) {
      $window.css({
        width: 'auto, important',
        height: 'auto, important'
      });
      $window.resizable('destroy');
    } else {
      $window.resizable();
    }
  });
});