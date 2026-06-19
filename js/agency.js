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

    // Smooth scroll to hash on initial load
    if (window.location.hash) {
        var hash = window.location.hash;
        var targetId = hash.substring(1);
        var targetEl = document.getElementById(targetId);
        if (targetEl) {
            // Reset scroll position to top
            document.documentElement.scrollTop = 0;
            document.body.scrollTop = 0;
            setTimeout(function() {
                targetEl.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 150);
        }
    }
});