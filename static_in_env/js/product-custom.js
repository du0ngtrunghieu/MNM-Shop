//range-slider
$(function () {
  
});



//sidebar
$(".main-side-bar .sub-menu a").click(function () {
  $(this).parent(".sub-menu").children("ul").slideToggle("300");
  $(this).find("i.fa").toggleClass("flaticon-3-signs flaticon-4-minus");
});

//tooltip
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})