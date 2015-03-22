$( ".js-toggle__top" ).click(function() {
    $('.menu__top').toggleClass("open");
});
$( ".js-toggle__bottom" ).click(function() {
    $('.menu__bottom.alerts').toggleClass("open");
});
$( ".notification__reply" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});


$(window).on("resize", function () {
    networkWidth = $( ".network" ).width();
    networkChildren = $(".network .network__user").length;

    if(networkChildren < 5) {
        networkDivide = networkWidth / networkChildren;
        $(".network .network__user").css("width",networkDivide);
    }else {
        networkDivide = networkWidth * 0.22;
        $(".network .network__user").css("width",networkDivide);
    }
}).resize();

$( ".network" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});
