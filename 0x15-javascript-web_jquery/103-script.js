document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('keypress click', function (res) {
    var io = $('#language_code').val();
    if (res.which === 13 || res.type === 'click') {
      $.get('https://www.fourtonfish.com/hellosalut/?lang=' + io, function(info) {
	$('#hello').text(info.hello);
      });
    }
    res.preventDefault();
  });
});
