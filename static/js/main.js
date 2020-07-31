function validURL(str) {
  var pattern = new RegExp(
    '^(https?:\\/\\/)?' + // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
      '(\\#[-a-z\\d_]*)?$',
    'i'
  ); // fragment locator
  return !!pattern.test(str);
}

$('#short').attr('maxlength', '30');
$('#original').change(function () {
  var long = $(this).val();
  if (!validURL(long)) {
    $('.message-long').empty();
    $('.message-long').append('Invalid URL');
  } else {
    $('.message-long').empty();
  }
  if (long == '') {
    $('.message-long').empty();
  }
});

$('#short').keyup(function () {
  var url = $(this).val();

  $.ajax({
    url: '/ajax/validate_url/',
    data: {
      url: url,
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        $('#shorten_button').attr('disabled', 'disabled');
        $('.message-short').empty();
        $('.message-short').append('A user with this username already exists.');
      } else {
        $('.message-short').empty();
        $('#shorten_button').removeAttr('disabled');
      }
    },
  });
});