/*
Theme Name: Genmed - MULTIPURPOSE HTML5 Template.
Author: Slidesigma
Author URL: https://themeforest.net/user/slidesigma
Version: 1.0.0
*/
(function ($) {
  'use strict';
  // head-search
  $("li.search").on("click", function () {
    var $this = $(this).find('i');
    if ($this.hasClass('fa-search')) {
      $this.removeClass('fa-search').addClass('fa-times');
    } else {
      $this.removeClass('fa-times').addClass('fa-search');
    }
    $(".topbar-search").toggleClass('search-visible');
  });
  //fix header
  $(window).scroll(function () {
    var sticky = $('.main-navigation-style-1, .header-style-2'),
      scroll = $(window).scrollTop();
    if (scroll >= 100) sticky.addClass('sticky');
    else sticky.removeClass('sticky');
  });
  $(document).ready(function () {
    $('.datepickr').datepicker({
      timepicker: false,
      minDate: new Date()
    });
    $('.timepickr').datepicker({
      timepicker: true,
      onlyTimepicker: true,
      range: true,
    });
  });
  // custom-select
  $(document).ready(function () {
    $('.custom-select').niceSelect();
  });
  // navigation
  $('.menu-item-has-children>a').append('<span class="arrow"></span>');
  $('.menu-item-has-megamenu>a').append('<span class="arrow"></span>');
  //mobile nav
  $(document).ready(function () {
    $(".hamburger-menu").click(function () {
      $(".menu-btn").toggleClass("active");
      $(".main-menu, .main-navigation-style-2").toggleClass("active");
      $("body").toggleClass("menu-open");
      $('html').toggleClass('overflow');
    });
  });
  $(document).ready(function () {
    $('.menu-item-has-children>a, .menu-item-has-megamenu>a').on('click', function () {
      $(this).removeAttr('href');
      var element = $(this).parent('li');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul.sub-menu, .megamenu').slideUp();
      } else {
        element.addClass('open');
        element.children('ul.sub-menu, .megamenu').slideDown();
        element.siblings('li').children('ul.sub-menu, .megamenu').slideUp();
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul.sub-menu, .megamenu').slideUp();
      }
    });
  });
  // banner-slider
  $('.banner-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    infinite: true,
    autoplay: true,
    speed: 400,
    focusOnSelect: true,
    cssEase: 'linear'
  });
  $('.banner-slider-2').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: true,
    infinite: true,
    autoplay: true,
    speed: 400,
    focusOnSelect: true,
    cssEase: 'linear'
  });
  $('.services-detail-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: false,
    arrows: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 400,
    focusOnSelect: true,
    cssEase: 'linear'
  });
  // services-slider
  $('.services-slider').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: false,
    arrows: true,
    infinite: true,
    loop: true,
    autoplay: true,
    speed: 400,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        arrows: true,
        slidesToShow: 2
      }
    }, {
      breakpoint: 768,
      settings: {
        arrows: false,
        dots: true,
        slidesToShow: 1
      }
    }]
  });
  // doctors-slider
  $('.doctors-slider').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    dots: false,
    arrows: true,
    infinite: true,
    loop: true,
    autoplay: true,
    speed: 400,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        arrows: true,
        slidesToShow: 3
      }
    }, {
      breakpoint: 768,
      settings: {
        arrows: false,
        dots: true,
        slidesToShow: 2
      }
    }, {
      breakpoint: 480,
      settings: {
        arrows: false,
        dots: true,
        slidesToShow: 1
      }
    }]
  });
  $('.doctors-slider-2').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    infinite: true,
    loop: true,
    autoplay: true,
    speed: 400,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        slidesToShow: 3
      }
    }, {
      breakpoint: 768,
      settings: {
        slidesToShow: 2
      }
    }, {
      breakpoint: 480,
      settings: {
        slidesToShow: 1
      }
    }]
  });
  // Blog-slider
  $('.blog-slider').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: false,
    arrows: true,
    infinite: true,
    loop: true,
    autoplay: true,
    speed: 400,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        arrows: true,
        slidesToShow: 2
      }
    }, {
      breakpoint: 768,
      settings: {
        arrows: false,
        dots: true,
        slidesToShow: 1
      }
    }]
  });
  $('.blog-slider-2').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    infinite: true,
    loop: true,
    autoplay: true,
    speed: 400,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        slidesToShow: 2
      }
    }, {
      breakpoint: 768,
      settings: {
        slidesToShow: 1
      }
    }]
  });
  // testimonial slider
  $('.testimonial-slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    autoplay: true,
    speed: 500,
    cssEase: 'linear',
    pauseOnHover: true
  });
  $('.testimonials-slider-2').slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    autoplay: true,
    speed: 500,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        arrows: false,
        slidesToShow: 1
      }
    }]
  });
  $('.testimonials-slider-3').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    autoplay: true,
    speed: 500,
    cssEase: 'linear',
    responsive: [{
      breakpoint: 992,
      settings: {
        arrows: false,
        slidesToShow: 2
      }
    },
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        slidesToShow: 1
      }
    }]
  });
  // counter
  $('.count').each(function () {
    $(this).prop('Counter', 0).animate({
      Counter: $(this).text()
    }, {
      duration: 4000,
      easing: 'swing',
      step: function (now) {
        $(this).text(Math.ceil(now));
      }
    });
  });
  $('.gallery').magnificPopup({
    delegate: 'a.popup',
    type: 'image',
    removalDelay: 300,
    mainClass: 'mfp-fade',
    gallery: {
      enabled: true
    }
  });
  // back to top
  var offset = 220;
  var duration = 500;
  $(window).on('scroll', function () {
    if ($(this).scrollTop() > offset) {
      $('.back-top').fadeIn(duration);
    } else {
      $('.back-top').fadeOut(duration);
    }
  });
  $('.back-top').on('click', function (event) {
    event.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, "slow");
    return false;
  });
  if ($(window).scrollTop() > offset) {
    $('.back-top').fadeOut(0);
  }
  $('a[href="#"]').click(function (e) {
    e.preventDefault ? e.preventDefault() : e.returnValue = false;
  });
  // smooth scroll
  $.fn.smoothScroll = function (setting) {
    var _default = {
        duration: 1000,
        easing: 'swing',
        offset: 0,
        top: '100px'
      },
      _setting = $.extend(_default, setting),
      _handler = function () {
        var dest = 0,
          target = this.hash,
          $target = $(target);
        $(this).on('click', function (e) {
          e.preventDefault();
          if ($target.offset().top > ($(document).height() - $(window).height())) {
            dest = $(document).height() - $(window).height();
          } else {
            dest = $target.offset().top - _setting.offset;
          }
          $('html, body').animate({
            scrollTop: dest
          }, _setting.duration, _setting.easing);
        });
      };
    return this.each(_handler);
  };
  $('.scrollbtn').smoothScroll({
    duration: 1000, // animation speed
    easing: 'swing', // find more easing options on http://api.jqueryui.com/easings/
    offset: 0 // custom offset
  });
  // on click Video
  $(document).on('click', '.js-videoPoster', function (e) {
    e.preventDefault();
    var poster = $(this);
    var wrapper = poster.closest('.js-videoWrapper');
    videoPlay(wrapper);
  });

  function videoPlay(wrapper) {
    var iframe = wrapper.find('.js-videoIframe');
    var src = iframe.data('src');
    wrapper.addClass('videoWrapperActive');
    iframe.attr('src', src);
  }
  // filter gallery
  $(document).ready(function () {
    $('.gallery-grid').isotope(function () {
      itemSelector: '.filter-box'
    });
    $('.filter-gallery>ul>li').click(function () {
      $('.filter-gallery>ul>li').removeClass('active');
      $(this).addClass('active');
      var selector = $(this).attr('data-filter');
      $('.gallery-grid').isotope({
        filter: selector
      })
      return false;
    });
  });
  $('.gallery-grid').magnificPopup({
    delegate: 'a.popup',
    type: 'image',
    removalDelay: 300,
    mainClass: 'mfp-fade',
    gallery: {
      enabled: true
    }
  });
  // banner animation
  $(function () {
    if ($('body').is('.animated-banner')) {
      particlesJS('banner-animation', {
        "particles": {
          "number": {
            "value": 80,
            "density": {
              "enable": true,
              "value_area": 800
            }
          },
          "color": {
            "value": "#ffffff"
          },
          "shape": {
            "type": "circle",
            "stroke": {
              "width": 0,
              "color": "#000000"
            },
            "polygon": {
              "nb_sides": 5
            },
            "image": {
              "src": "img/github.svg",
              "width": 100,
              "height": 100
            }
          },
          "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
              "enable": false,
              "speed": 1,
              "opacity_min": 0.1,
              "sync": false
            }
          },
          "size": {
            "value": 5,
            "random": true,
            "anim": {
              "enable": false,
              "speed": 40,
              "size_min": 0.1,
              "sync": false
            }
          },
          "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
          },
          "move": {
            "enable": true,
            "speed": 6,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "attract": {
              "enable": false,
              "rotateX": 600,
              "rotateY": 1200
            }
          }
        },
        "interactivity": {
          "detect_on": "canvas",
          "events": {
            "onhover": {
              "enable": true,
              "mode": "repulse"
            },
            "onclick": {
              "enable": true,
              "mode": "push"
            },
            "resize": true
          },
          "modes": {
            "grab": {
              "distance": 400,
              "line_linked": {
                "opacity": 1
              }
            },
            "bubble": {
              "distance": 400,
              "size": 40,
              "duration": 2,
              "opacity": 8,
              "speed": 3
            },
            "repulse": {
              "distance": 200
            },
            "push": {
              "particles_nb": 4
            },
            "remove": {
              "particles_nb": 2
            }
          }
        },
        "retina_detect": true,
        "config_demo": {
          "hide_card": false,
          "background_color": "#b61924",
          "background_image": "",
          "background_position": "50% 50%",
          "background_repeat": "no-repeat",
          "background_size": "cover"
        }
      });
    }
  });
    //Price-range
      $( function() {
        $( "#shop-range-price" ).slider({
            range: true,
            min: 20,
            max: 500,
            thousand: ',',
            values: [ 50, 300 ],
            slide: function( event, ui ) {
                $( "#shop-price" ).val( "$" + ui.values[ 0 ] );
                $( "#shop1-price" ).val( "$" + ui.values[ 1 ]);
            }
        });
        $( "#shop-price" ).val( "$" + $( "#shop-range-price" ).slider( "values", 0 ));
            $( "#shop1-price" ).val( "$" + $( "#shop-range-price" ).slider( "values", 1 ) );
    } );
    //slider shop details
    $('.detail-page-slider-for').slick({
		  slidesToShow: 1,
		  slidesToScroll: 1,
		  arrows: false,
		  asNavFor: '.detail-page-slider-nav'
	});
	$('.detail-page-slider-nav').slick({
		marginLeft:2,  
        slidesToShow: 3,
		  slidesToScroll: 1,
		  asNavFor: '.detail-page-slider-for',
		  dots: false,
		  centerMode: true,
		  centerPadding: '0px',
		  focusOnSelect: true,
		  responsive: [{
			breakpoint: 567,
			settings: {
				slidesToShow: 2,
			}
		}]
	});
 
    
$('.detail-page-slider1').slick({
		  
        slidesToShow: 3,
		  slidesToScroll: 1,
		  
		  dots: false,
		  centerMode: true,
		  centerPadding: '0px',
		  focusOnSelect: true,
		responsive: [
        {
            breakpoint: 1300,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 992,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
           dots: true,
                arrows: false,
            }
        }

  ]

	});    
    
// quantity plus minus
  $('.minus-btn').on('click', function (e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('.quantity').find('input');
    var value = parseInt($input.val());
    if (value > 1) {
      value = value - 1;
    } else {
      value = 1;
    }
    $input.val(value);
  });
  $('.plus-btn').on('click', function (e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('.quantity').find('input');
    var value = parseInt($input.val());
    if (value < 100) {
      value = value + 1;
    } else {
      value = 100;
    }
    $input.val(value);
  });    
    
  // time counter
  function makeTimer() {
    var endTime = new Date("01 January 2021 00:00:00 GMT+05:30");
    endTime = (Date.parse(endTime) / 1000);
    var now = new Date();
    now = (Date.parse(now) / 1000);
    var timeLeft = endTime - now;
    var days = Math.floor(timeLeft / 86400);
    var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
    var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
    var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
    if (hours < "10") {
      hours = "0" + hours;
    }
    if (minutes < "10") {
      minutes = "0" + minutes;
    }
    if (seconds < "10") {
      seconds = "0" + seconds;
    }
    $("#cvdays").html(days);
    $("#cvhours").html(hours);
    $("#cvminutes").html(minutes);
    $("#cvseconds").html(seconds);
  }
  setInterval(function () {
    makeTimer();
  }, 1000);

  // color switch
     $( ".each-color.co1" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co2" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co3" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co4" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co5" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co6" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co7" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co8" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

     $( ".each-color.co9" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });
     $( ".each-color.co10" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });
     $( ".each-color.co11" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });
     $( ".each-color.co12" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });
     $( ".each-color.co13" ).on('click', function(e) {
         var data1 = $(this).data('color');
         $(".color-changing").attr('href', data1);
     });

})(jQuery);
