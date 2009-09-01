function nav() {
  $('#nav ul li').hover(
  function(e) {
    var ul = $(this).find('ul');
    ul.show();
  },
  function(e) {
    var ul = $(this).find('ul');
    ul.hide();
  });
}


$(function() {
  nav();
});