$(function() {

  $(".checkbox").on('click', function() {
    if ($(this).prop('checked')) {
      console.log("checked");
      $(this).closest('tr').find('.enable').prop('disabled', false);
    }
    else {
      console.log("unchecked");
      $(this).closest('tr').find('.enable').prop('disabled', true);
    }
  });

  $(".form-button").on('click', function(event) {
    event.preventDefault();
    // payload
    console.log($('.enable-status').attr("name"));
    var data = {
      statusUpdate: $('.enable-status').val(),
      commentsUpdate: $('.enable-comments').val()
    };
    // post request
    $.post("users/save", data, function(err, results) {
      console.log(results);
      // if (err) {
      //   $(classname).html("something went wrong");
      // } else {
      //   $(classname).html("success!");
      // }
    });

  });

});
