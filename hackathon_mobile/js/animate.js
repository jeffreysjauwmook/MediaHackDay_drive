$( ".js-toggle__top" ).click(function() {
    $('.menu__top').toggleClass("open");
});
$( ".js-toggle__bottom" ).click(function() {
    $('.menu__bottom.alerts').toggleClass("open");
});
$( ".notification__reply" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});