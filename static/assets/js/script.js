/* Template	:	Covid | Version 1.0.0 */
(function($){
	'use strict';
	var $win = $(window), $body = $('body'), $doc = $(document);

	// Touch Class
	if (!("ontouchstart" in document.documentElement)) {
		$body.addClass("no-touch");
	}
    
	// Get Window Width
	function winwidth () {
		return $win.width();
	}
	var wwCurrent = winwidth();
	$win.on('resize', function() { 
		wwCurrent = winwidth();
	});
    
        // STICKY ACTIVE
        var activeSticky = $('#active-sticky'),
        winD = $(window);
        winD.on('scroll',function() {
          var scroll = $(window).scrollTop(),
                isSticky = activeSticky;
          if (scroll < 2) {
                isSticky.removeClass("is-sticky");
          }
          else{
            isSticky.addClass("is-sticky");
          }
       });
    
		setTimeout(function() {
			$('body').addClass('loaded');
		}, 3500);
	// OnePage Scrolling
    $('a.menu-link[href*="#"]:not([href="#"])').on("click", function() {
		if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
		  var toHash = $(this.hash), toHashN = (this.hash.slice(1)) ? $('[name=' + this.hash.slice(1) + ']') : false;
		  toHash = toHash.length ? toHash : toHashN;
		  if (toHash.length) {
			$('html, body').animate({
			  scrollTop: (toHash.offset().top )
			}, 1000);
            return false;
		  }
		}
	});
    
    //Navigation
    var $dropdown_trigger = $('.dropdown-trigger');
	if ($dropdown_trigger.length > 0 ) {
		$dropdown_trigger.on("click",function(e){
			if ($win.width() < 1920) {
				$(this).parent().children('.dropdown-content').slideToggle(400);
				$(this).parent().siblings().children('.dropdown-content').slideUp(400);
				$(this).parent().toggleClass('current');
				$(this).parent().siblings().removeClass('current');
				e.preventDefault();
			}
		});
	}
    
	//Caregory
    var $header_cat_head = $('.header-cat-head'), $header_cat_list = $('.header-cat-list');
	if ($header_cat_head.length > 0 ) {
		$header_cat_head.on("click",function(e){
			if ($win.width() < 991) {
				$header_cat_list.slideToggle(400);
				e.preventDefault();
			}
		});
	}
    
    // Toggle section On click
    var _trigger = '.drop-trigger', _toggle = '.drop-content';
    
    if ($(_trigger).length > 0 ) {
		$doc.on('click', _trigger, function(e){
            var $self = $(this);
            $(_trigger).not($self).removeClass('active');
            $(_toggle).not($self.parent().children()).removeClass('active');
            $self.toggleClass('active').parent().find(_toggle).toggleClass('active');
            e.preventDefault();
        });
	}
    
    $doc.on('click', 'body', function(e){
        var $elm_tig = $(_trigger), $elm_tog = $(_toggle);
		if (!$elm_tog.is(e.target) && $elm_tog.has(e.target).length===0 && 
            !$elm_tig.is(e.target) && $elm_tig.has(e.target).length===0) {
                $elm_tog.removeClass('active');
                $elm_tig.removeClass('active');
		}
	});
    
    $(window).on('resize', function(){
        $(_trigger).removeClass('active');
        $(_toggle).removeClass('active');
    });
    
    var $nav_toggle = $('.navbar-toggle'),  $nav_content = $('.navbar-toggle-content');
    if($nav_toggle.length > 0) {
        $nav_toggle.on('click', function(e){
            $nav_toggle.toggleClass('active');
            $nav_content.toggleClass('active');
            e.preventDefault();
        });
    }
    $(window).on('resize', function(){
        if(wwCurrent > 991){
            $nav_toggle.removeClass('active');
            $nav_content.removeClass('active');
        }
    });
    
    $doc.on('click', 'body', function(e){
		if (!$nav_content.is(e.target) && $nav_content.has(e.target).length===0 && 
            !$nav_toggle.is(e.target) && $nav_toggle.has(e.target).length===0) {
                $nav_toggle.removeClass('active');
                $nav_content.removeClass('active');
		}
	});
    
    function activeNav(navbar){
        if($win.width() < 992){
            navbar.delay(500).addClass('navbar-mobile');
        }else{
            navbar.delay(500).removeClass('navbar-mobile');
        }
    }
    activeNav($nav_content);
    $(window).on('resize', function(){
        activeNav($nav_content);
    });
    
	// Active page menu when click
	var CurURL = window.location.href, urlSplit = CurURL.split("#");
	var $nav_link = $("a");
	if ($nav_link.length > 0) {
		$nav_link.each(function() {
			if (CurURL === (this.href) && (urlSplit[1]!=="")) {
				$(this).closest("li").addClass("active").parent().closest("li").addClass("active");
			}
		});
	}
    
    // CountDown
    var $data_countdown = $('[data-countdown]');
	if ($data_countdown.length > 0 ) {
		$data_countdown.each(function() {
            var $this = $(this), finalDate = $(this).data('countdown');
            $this.countdown(finalDate, function(event) {
                $this.html(event.strftime('<div class="countdown-item"><div class="countdown-time">%D</div><div class="countdown-text">Days</div></div><div class="countdown-item"><div class="countdown-time">%H</div><div class="countdown-text">Hours</div></div><div class="countdown-item"><div class="countdown-time">%M</div><div class="countdown-text">Min</div></div><div class="countdown-item"><div class="countdown-time">%S</div><div class="countdown-text">Sec</div></div>'));
            });
        });
	}
    
    //Animation initial

    new WOW().init();
    
    // Slider
    var $project_slider = $('.banner-slider'), $project_sd = $('.banner-slider-dots').find('.owl-dot');
	if ($project_slider.length > 0 ) {
		$project_slider.each(function() {
            $project_slider.addClass('owl-carousel').owlCarousel({
                loop:true,
                margin:0,
                nav:false,
                items: 1,
                autoplay: false,
                dotsEach: 1,
                slideBy: 2,
            });
        });
	}
    if ($project_sd.length > 0){
        $project_sd.on('click',function () {
            $project_slider.trigger('to.owl.carousel', [$(this).index(), 300]);
        });
    }
    
    $project_sd.on('click',function () {
        $project_slider.trigger('to.owl.carousel', [$(this).index(), 300]);
    });
    
    // Slider Testimonial
    var $testimonial_ds = $('.testimonial-slider'), $testimonial_dt=$('.testimonial-thumb').find('.owl-dot');
	if ($testimonial_ds.length > 0 ) {
		$testimonial_ds.each(function() {
            $testimonial_ds.addClass('owl-carousel').owlCarousel({
                loop:true,
                margin:0,
                nav:false,
                items: 1,
            });
        });
	}
    if ($testimonial_dt.length > 0){
        $testimonial_dt.on('click',function () {
            $testimonial_ds.trigger('to.owl.carousel', [$(this).index(), 300]);
        });
    }
    
    // Select
    var $select = $('select');
	if ($select.length > 0) {
        $select.each(function() {
			var $this = $(this);
            $this.select2();
		});
	}
    var $select_bdr = $('.select-bordered');
	if ($select_bdr.length > 0) {
        $select_bdr.each(function() {
			var $this = $(this);
            $this.select2({
                theme: "default bordered"
            });
		});
	}
    
    // Range Slider
    var $slider_range = $('#slider-range'), $slider_amount = $('#slider-amount');
	if ($slider_range.length > 0) {
        $slider_range.slider({
            range: true,
            min: 0,
            max: 8000,
            values: [ 50, 5000 ],
            slide: function( event, ui ) {
                $slider_amount.val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            }
        });
        $slider_amount.val( "$" + $( "#slider-range" ).slider( "values", 0 ) + " - $" + $( "#slider-range" ).slider( "values", 1 ) );
	}
    
    
    // Cart Counter
    var $cart_value = $(".cart-value"), $cart_minus = $(".cart-minus"), $cart_plus = $(".cart-plus");
    if ($cart_value.length > 0) {
        $cart_minus.on('click', function() {
            var $input = $(this).parent().find($cart_value);
            var count = parseInt($input.val(), 10) - 1;
            count = count < 1 ? 1 : count;
            $input.val(count);
            $input.change();
            return false;
        });
        $cart_plus.on('click', function() {
            var $input = $(this).parent().find($cart_value);
            $input.val(parseInt($input.val(), 10) + 1);
            $input.change();
            return false;
        });
    }
    
    // Image Pop up
    var $popup_image = $(".popup-image"), $popup_embed = $(".popup-embed"), $popup_ajax = $(".popup-ajax");
    if ($popup_image.length > 0) {
        $popup_image.magnificPopup({
            type: 'image',
            removalDelay: 300,
            mainClass: 'mfp-fade',
        });	
    }
    // Embeded Pop up
    if ($popup_embed.length > 0) {
        $popup_embed.magnificPopup({
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }
    // Embeded Pop up
    if ($popup_ajax.length > 0) {
        $popup_ajax.magnificPopup({
            type: 'ajax',
            modal: true,
            overflowY: 'scroll',
            showCloseBtn: true,
            closeBtnInside: true,
        });
    }
 
    
    // Mas layout
    var $header_mas = $('.header-mas');
    $(window).on('load', function(){
        if ($header_mas.length > 0) {
            $header_mas.masonry({
                itemSelector: '.header-mas-item'
            });
        }
    });

	
})(jQuery);