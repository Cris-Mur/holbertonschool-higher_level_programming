document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function (res) {
    var io = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + io, function (info) {
      $('#hello').text(info.hello);
    });
    res.preventDefault();
  });
});
