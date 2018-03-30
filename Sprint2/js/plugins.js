/*global $, console*/

$(document).ready(function () {
    'use strict';
    
    var colorLi = $(".option-box .color-option li"),
        scrollTop = $("#scroll_top");
    
    // nice scroll
    $("html, body").niceScroll({
        cursorcolor: "#000",
        cursorwidth: "13px",
        cursorborder: "1px solid rgba(6, 6, 6, .8)",
        cursorborderradius: "2px",
        zindex: 99999,
        mousescrollstep: 45
    });
    
    // carousel slide time
    $('.carousel').carousel({
        interval: 6000
    });
    
    // show color-option div when click on the gear
    $('.gear-div').click(function () {
        $('.option-box .color-option').fadeToggle(500);
    });
    
    // change theme color on clicking
    colorLi.eq(0).css("background-color", "#e41b17").end()
           .eq(1).css("background-color", "#07cb79").end()
           .eq(2).css("background-color", "#469BC6").end()
           .eq(3).css("background-color", "#ff9801").end();
                                     
    colorLi.click(function () {
        $("link[href*='theme']").attr("href", $(this).attr("data-value"));
    });
    
    // loading
    $(window).load(function () {
        $(".spinner").fadeOut(0, function () {
            $(".loader_overlay").fadeOut(0, function () {
                $("body").css("overflow", "auto");
            });
        });
    });
    
    
    
    // scroll to top
    
    $(window).scroll(function () {
        
        if ($(this).scrollTop() >= 300) {
            scrollTop.fadeIn();
        } else {
            scrollTop.fadeOut();
        }
        
       // $(this).scrollTop() >= 300 ? scrollTop.fadeIn() : scrollTop.fadeOut(); -> inline if
    });
    
    scrollTop.click(function () {
        $("html, body").animate({scrollTop: 0}, 600);
    });
    
    
});

