/**
 * Created by Ezero on 16/8/29.
 */
var a=1;
var team = $(".team");
var b=1;
$(function () {
    $("#aAboutUs").click(function () {
        $.scrollTo("#AboutUs",500);
    });
    $("#aFounder").click(function () {
        $.scrollTo("#Founder",500);
    })
    $("#aLeather").click(function () {
         $.scrollTo("#Leather",500);
    })
    $("#aGallery").click(function () {
         $.scrollTo("#Gallery",1000);
    })
    $("#aContact").click(function () {
        $.scrollTo("#Contact",1300);
    })
    $("img.top").click(function () {
        $.scrollTo("#head", 2000)
    })
        $("a.g1").click(function () {
            showmodal("static/gallery-1-1.jpg")
            return false
        });
        $("a.g8").click(function () {
            showmodal("static/gallery-8-1.jpg")
            return false
        });
        $("a.g13").click(function () {
            showmodal("static/gallery-13-1.jpg")
            return false
        });
        $("a.g20").click(function () {
            showmodal("static/gallery-20-1.jpg")
            return false
        });
        $("a.g").click(function () {
            showmodal("static/gallery.jpg")
            return false
        });
    $("img.search").click(function () {
        $(".form1").submit()
    });
    check_size();
    $(".pic").load(function () {
       check_size()
    });

    $(window).resize(function () {
        check_size()
    });
    cyclic();
    lunbo();
    });
function showmodal(src) {
     $(".modalimg").attr("src",src);
    $('#myModal').modal('show')
}
function cyclic() {
    a++;
    setTimeout(function () {
        if (a%2){
            $("div.founder p.introduce").text('Yiran Lee');
            $("div.founder p.a1").text('Yiran Lee');
            $("div.founder p.a2").text('我开始以为生活的态度只有一种,工作的感觉也只有一中,但是慢慢成长后,发现原来生命中是有那么多色彩的,那么多的可能,没有限制,一切基于都在进行中')
         team.css("background-image", 'url("static/team-1.jpg")');
    }
    else {
            $("div.founder p.introduce").text('Fiona Chan');
            $("div.founder p.a1").text('Fiona Chan');
            $("div.founder p.a2").text('那么久的国外生活,游历了200多个国家,不敢说活透了人生,但是觉得原来一切的变化与不同我们都是可以接受和理解的。人生百态,活法不只有一中,我只是选择我喜爱的那个方向前进着。')
        team.css("background-image", 'url("static/team-2.jpg")');
    }
        cyclic()
    },4000)
}
function lunbo() {
    setTimeout(function () {
        $("#myCarousel").carousel('next');
        $("#Carousel").carousel('next');
        lunbo()
    },5000);
}

function check_size() {
    $(".text").height($(".pic").height())
        if(window.innerWidth<=600){
            $("p.french").css('display','none')
            $(".contact .col-xs-offset-1").addClass('col-xs-offset-2 col-xs-8')
            $(".contact .col-xs-offset-1").css('min-height', '0')
            $(".contact .col-xs-offset-1").removeClass('col-xs-offset-1 col-xs-5')
            $(".contact form").removeClass('col-xs-5')
            $(".contact form").addClass('col-xs-8 col-xs-offset-2')
            $(".contact form").css('margin-top','50px')
            $(".slide2").addClass("col-xs-12");
            $(".slide2").removeClass("col-xs-10 col-xs-offset-1");
            $(".modal-dialog img").css("width", '300')
        }else {
            $(".slide2").removeClass("col-xs-12");
            $(".slide2").addClass("col-xs-10 col-xs-offset-1");
            $(".contact form").addClass('col-xs-5');
            $(".contact form").css('margin-top','0px');
            $(".contact .address").css('min-height', '342px');
            $(".contact form").removeClass('col-xs-8 col-xs-offset-2')
            $(".contact .address").removeClass('col-xs-offset-2 col-xs-8')
            $(".contact .address").addClass('col-xs-offset-1 col-xs-5')
            $("p.french").css('display','block')
            $(".modal-dialog img").css("width", '500')
        }
        if(window.innerWidth<=1117){
            $(".footer p").css({
                'float':'none',
                'margin-left':'auto',
                'margin-right':'auto',
                'text-align':'center'
            });
            $("footer ul").addClass('clearfix')
        }
        else{
            $("footer ul").removeClass('clearfix')
            $(".footer p").css({
                'float':'right',
                'margin-right':'120px',
                'text-align':'left'
            })
        }
        if(window.innerWidth<=1060){
            $(".logo").addClass("col-xs-8 col-xs-offset-2");
            $(".logo").css({
                "left":"0",
                "float":'left'
            });
            $(".logo").removeClass("col-xs-5");
            $(".slide2").removeClass("col-xs-7");
            $(".slide2").addClass("col-xs-10 col-xs-offset-1");
            $("header .slide-2").css({
                'left':'0',
                'margin-top':'-60%'
            })
        }
        else{
            $("header .slide-2").css({
                'left':'-20px',
                'margin-top':'-67%'
            });
            $(".logo").addClass("col-xs-5");
            $(".slide2").addClass("col-xs-7");
            $(".slide2").removeClass("col-xs-10 col-xs-offset-1");
            $(".logo").css({
                "left":"-20px",
                "float":'right'
            });
             $(".logo").removeClass("col-xs-8 col-xs-offset-2");
        }
        if(window.innerWidth<=855){
            $(".about").css({
                "width":'80%',
                'float':'none',
                'margin-left':'auto',
                'margin-right':'auto'
            })
        }
        else{
            $(".text").height($(".about img").height());
            $(".about").css({
                "width":'60%',
                'float':'right',
                'margin-right':'7%'

        });
            $(".about-2").css({
                'float':'left',
                'margin-left':'7%'
            })

        }
        if(window.innerWidth<=811){
            $(".founder .person").removeClass('col-xs-5 col-xs-offset-1')
            $(".founder .person").addClass('col-xs-8 col-xs-offset-2')
            $(".founder .col-xs-5").addClass('col-xs-8 col-xs-offset-2')
            $(".founder .col-xs-5").removeClass('col-xs-5');
            $(".team").height($(".team").width()/people_ratio)
        }else{
            $(".founder .person").addClass('col-xs-5 col-xs-offset-1')
            $(".founder .person").removeClass('col-xs-8 col-xs-offset-2')
            $(".founder .say").removeClass('col-xs-8 col-xs-offset-2')
            $(".founder .say").addClass('col-xs-5');
            $(".team").height($(".team").width()/people_ratio)
            $(".feedback").height($(".team").height());
        }
        if(window.innerWidth<=767){
            $(".text").removeClass('col-xs-6');
            $(".text").addClass('col-xs-10 col-xs-offset-1');
            $(".about").css('min-width', '0');
            $(".about img").removeClass('col-xs-6')
            $(".text2").css({
                'position':'relative',
                'height':'auto',
                'top':'auto',
                'transform':'translate(0,0)',
                'margin-top':'30px',
                'margin-bottom':'30px'
            });
            $(".text").css({
                'height':'auto'
            })
        }
        else{
            $(".text").addClass('col-xs-6');
            $(".text").removeClass('col-xs-10 col-xs-offset-1');
            $(".about").css('min-width', '735px');
            $(".about img").addClass('col-xs-6')
        }
    }