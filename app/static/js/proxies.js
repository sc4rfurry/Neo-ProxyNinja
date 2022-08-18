$(function() {
    var checkbox = $("#trigger");
    var hidden = $("#filename_input");
    var hidden2 = $("#format_select");
    hidden.hide();
    hidden2.hide();
    checkbox.change(function() {
      if (checkbox.is(':checked')) {
        hidden.show();
        hidden2.show();
      } else {
        hidden.hide();
        hidden2.hide();
        $("#filename_input").val("");
        $("#format_select").val("");
      }
    });
  });

//   $(document).ready(function() {
//     $("#fetch_btn").click(function() {
//       // disable button
//       $.post('/proxies');
//       $(this).prop("disabled", true);
//       // add spinner to button
//       $(this).html(
//         `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
//       );
//     });
// });