/*!
 * Start Bootstrap - Agnecy Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// Native smooth scrolling and navigation logic
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        var target = $anchor.attr('href');
        if (target && target.startsWith('#')) {
            var targetId = target.substring(1);
            var targetEl = document.getElementById(targetId);
            if (targetEl) {
                event.preventDefault();
                targetEl.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top'
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        if ($('.navbar-toggle').is(':visible')) {
            $('.navbar-toggle').click();
        }
    });

    // Smooth scroll to hash on initial load (using '#_' prefix to prevent browser's default instant jump)
    if (window.location.hash) {
        var hash = window.location.hash;
        if (hash.startsWith('#_')) {
            var targetId = hash.substring(2);
            var targetEl = document.getElementById(targetId);
            if (targetEl) {
                // Force top scroll position initially to avoid any jumpiness
                window.scrollTo(0, 0);
                setTimeout(function() {
                    // Cancel the animation immediately if the user scrolls manually
                    var cancelEvents = 'wheel.scrollCancel touchmove.scrollCancel keydown.scrollCancel';
                    $(window).on(cancelEvents, function() {
                        $('html, body').stop(true);
                        $(window).off(cancelEvents);
                    });

                    $('html, body').stop().animate({
                        scrollTop: $(targetEl).offset().top - 60 // Offset for the fixed navigation bar
                    }, 1250, 'easeInOutExpo', function() {
                        // Clean up listeners once animation completes naturally
                        $(window).off(cancelEvents);
                    });
                }, 500); // 500ms delay lets the page render before the smooth scroll begins
            }
        }
    }
});