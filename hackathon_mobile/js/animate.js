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

//home

$("body").delay(100).queue(function(){
    $('body').addClass('open__profile').dequeue();
});
$('body').delay(150).queue(function(){
    $(this).addClass('show__btn_1').dequeue();
});
$('body').delay(100).queue(function(){
    $(this).addClass('show__btn_2').clearQueue();
});



$( ".network" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});
