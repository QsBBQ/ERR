$(function() {

  $(".checkbox").on('click', function(e) {
    if ($(this).prop('checked')) {
      console.log("checked")
      $(this).closest('tr').find('.enable').prop('disabled', false);
    }
    else {
      console.log("unchecked")
      $(this).closest('tr').find('.enable').prop('disabled', true);
    }
  });

});
