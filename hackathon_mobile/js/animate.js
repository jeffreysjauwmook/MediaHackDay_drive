$( ".js-toggle__top" ).click(function() {
    $('.menu__top').toggleClass("open");
});
$( ".js-toggle__bottom" ).click(function() {
    $('.menu__bottom.alerts').toggleClass("open");
});
$( ".notification__reply" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});
$( ".alert-reply" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});
$( ".reply-menu__option" ).click(function() {
    $('.menu__bottom').removeClass("open");
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

$("body.home").delay(100).queue(function(){
    $('body').addClass('open__profile').dequeue();
});
$('body.home').delay(150).queue(function(){
    $(this).addClass('show__btn_1').dequeue();
});
$('body.home').delay(100).queue(function(){
    $(this).addClass('show__btn_2').clearQueue();
});

$('body.home').delay(100).queue(function(){
    $(this).addClass('show__btn_2').clearQueue();
});

$( ".home .btn-stats" ).click(function() {
    $('.menu__bottom.stats').toggleClass("open");
});

$( ".home .btn-inbox" ).click(function() {
    $('.menu__bottom.inbox').toggleClass("open");
});
$( ".home .js-toggle__bottom" ).click(function() {
    $('.menu__bottom.alerts').removeClass("open");
});

//network (driving page)
$( ".network" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
});

//notifcations (driving page)
$( ".alert-reply" ).click(function() {
    $('.menu__bottom.reply').toggleClass("open");
    $(this).parent().siblings().hide();
});


// $(".reply.open .reply-menu__option").click(function() {
//     $(".reply.open").removeClass("open");
// });

//hide notify when gave msg
$(".menu__bottom.reply li").click(function() {
    $(".notification").removeClass("open");
});
