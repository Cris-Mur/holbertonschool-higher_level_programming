$('DIV#toggle_header').click( function () {
  if ($('header').hasClass('green')) {
    $('header').toggleClass('green').addClass('red');
  } else {
    $('header').toggleClass('red').addClass('green');
  }
});
