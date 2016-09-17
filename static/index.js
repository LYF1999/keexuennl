/**
 * Created by Ezero on 16/8/29.
 */
var a=1;
var team = $(".team");
var b=1;
$(function () {
    $(".content .aboutus").css('margin-top',window.innerHeight-$("header").height())
    $(".error2 button").click(function () {
         $(".error2").css("display", 'none')
    })
    $(".aAboutUs").click(function () {
        $.scrollTo("#AboutUs",500);
    });
    $(".aFounder").click(function () {
        $.scrollTo("#Founder",500);
    })
    $(".aLeather").click(function () {
         $.scrollTo("#Leather",500);
    })
    $(".aGallery").click(function () {
         $.scrollTo("#Gallery",1000);
    })
    $(".aContact").click(function () {
        $.scrollTo("#Contact",1300);
        return false
    })
    $(".aContact2").click(function () {
        $.scrollTo("#Contact",200);
        return false
    })
    $("img.top").click(function () {
        $.scrollTo("#head", 2000)
    })
    $(".ahead").click(function () {
        $.scrollTo("#head", 2000)
    })
        
    $("img.search").click(function () {
        $('.form1').submit()
    });
    $("footer button").click(function () {
        $('.form2').submit()
    });
    $(".form1").submit(function () {
        var value = $("input[name='query1']").val();
       $.getJSON("/auth/api/?query="+value, function(ret){
            if(!ret.result){
                $(".error2").css("display", 'block')
            }else {
                if (ret.result==2){
                    $(".error2 img").attr('src', '/static/repeatname.jpg')
                    $(".error2").css("display", 'block')
                }else{
                    location.href='/auth/?query='+value
                }
            }
        });
        return false;
    });
    $(".form2").submit(function () {
        var value2 = $("input[name='query2']").val();
         $.getJSON("/auth/api/?query="+value2, function(ret){
            if(!ret.result){
                $(".error2").css("display", 'block')
            }else {
                if (ret.result==1){
                    $(".error2 img").attr('src', '/static/repeatname.jpg')
                    $(".error2").css("display", 'block')
                }else{
                    location.href='/auth/?query='+value
                }
            }
        });
        return false
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
        if (a%5==0){
            $("div.founder p.introduce").text('Yiran Lee');
            $("div.founder p.a1").text('Yiran Lee');
            $("div.founder p.a2").text('我开始以为生活的态度只有一种,工作的感觉也只有一中,但是慢慢成长后,发现原来生命中是有那么多色彩的,那么多的可能,没有限制,一切基于都在进行中')
            $("div.founder p.a3").text('"I used to thought we can just only have one attitude towards our life,work is also one feeling.but as we grow older.We found that'+
                'there are so many colors and so many possibilities in our life.There is no limit,all opportunities are processig."');
         team.css("background-image", 'url("static/team-1.jpg")');
    }
    else if(a%5==1){
            $("div.founder p.introduce").text('Fiona Chan');
            $("div.founder p.a1").text('Fiona Chan');
            $("div.founder p.a2").text('那么久的国外生活,游历了40多个国家,不敢说活透了人生,但是觉得原来一切的变化与不同我们都是可以接受和理解的。人生百态,活法不只有一中,我只是选择我喜爱的那个方向前进着。')
            $("div.founder p.a3").text('"Living abroad for a long time,traveled to more than 40 countries.Does not dare to speak comprehend everything,but knowing that the all different we met before should beacceptabled and understandabled.The vicissitudes of life,"'+
            'life style is not only have one way,so I choose my favorite direction to go forward."')
        team.css("background-image", 'url("static/team-2.jpg")');
    }
        else if(a%5==2){
             $("div.founder p.introduce").text('A-Lin');
            $("div.founder p.a1").text('A-Lin');
            $("div.founder p.a2").text('"让你所爱的美成为你要做的事。"');
            $("div.founder p.a3").text('"Let the beauty of what you love be what you do."');
        team.css("background-image", 'url("static/team-3.jpg")');

        }
        else if(a%5==3){
            $("div.founder p.introduce").text('Queena');
            $("div.founder p.a1").text('Queena');
            $("div.founder p.a2").text('每个女孩都该做到两点：有品位并且光芒四射。')
            $("div.founder p.a3").text('"A girl should be two things: classy and fabulous."')
        team.css("background-image", 'url("static/team-4.jpg")');

        }
        else if(a%5==4){
            $("div.founder p.introduce").text('Eggy');
            $("div.founder p.a1").text('Eggy');
            $("div.founder p.a2").text('要么你就喜欢现在的你自己,要么努力成为你喜欢的那个自己。')
            $("div.founder p.a3").text('"Either you like now of oneself, or trying to become you like that myself."')
        team.css("background-image", 'url("static/team-5.jpg")');

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
    if (window.innerWidth<=553){
            $(".p1").css('margin-bottom','12px')
        }
    else {
        $(".p1").css('margin-bottom','60px')
        }
        if(window.innerWidth<=600){

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
        if(window.innerWidth<=966){
            $(".founder .person").removeClass('col-xs-5 col-xs-offset-1')
            $(".founder .person").addClass('col-xs-8 col-xs-offset-2')
            $(".founder .col-xs-5").addClass('col-xs-8 col-xs-offset-2')
            $(".founder .col-xs-5").removeClass('col-xs-5');
            $(".team").height($(".team").width()/people_ratio)
            $("div.feedback").css({
                'height':'400px',
            });
            $("p.s2").css('margin-top','50px')
        }else{
            $(".founder .person").addClass('col-xs-5 col-xs-offset-1')
            $(".founder .person").removeClass('col-xs-8 col-xs-offset-2')
            $(".founder .say").removeClass('col-xs-8 col-xs-offset-2')
            $(".founder .say").addClass('col-xs-5');
            $(".team").height($(".team").width()/people_ratio)
            $(".feedback").height($(".team").height());
            $("p.s2").css('margin-top','0')
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
            $(".text2").css({
                'position':'absolute',
                'height':'auto',
                'top':'50%',
                'transform':'translate(0,-50%)',
                'margin-top':'0',
                'margin-bottom':'30px'
            });
            $(".text").addClass('col-xs-6');
            $(".text").removeClass('col-xs-10 col-xs-offset-1');
            $(".about").css('min-width', '735px');
            $(".about img").addClass('col-xs-6')
        }
    }