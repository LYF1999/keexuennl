/**
 * Created by Ezero on 2016/9/21.
 */
function check() {
    if (window.innerWidth>=668){
        $(".content img").attr('src', '/static/certificate.jpg')
    }
    else {
       $(".content img").attr('src', '/static/certificate_mobile.jpg')
    }
}
$(function () {
    check();
    $(window).resize(function () {
        check();
    })
});