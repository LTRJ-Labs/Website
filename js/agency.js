/* AGENT-INFO
=========================================================
LTRJ LABS JAVASCRIPT
- Functionality: Handles scrolling navbar collapse, smooth page transitions, modal loading, and contact form anti-scraping logic.
- jQuery is heavily used for the legacy Bootstrap 3 plugins, while modern features (like clipboard copying) use Vanilla JS.
=========================================================
*/
/*!
 * Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// Immediate execution to prevent browser scroll jumping on load
if (window.location.hash && window.location.hash.startsWith('#_')) {
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }
    window.scrollTo(0, 0);
}

// Native smooth scrolling and navigation logic
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for a.page-scroll
    var pageScrollLinks = document.querySelectorAll('a.page-scroll');
    pageScrollLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            var target = link.getAttribute('href');
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
    });

    // Closes the Responsive Menu on Menu Item Click
    var navLinks = document.querySelectorAll('.navbar-collapse ul li a');
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            var navbarToggle = document.querySelector('.navbar-toggle');
            var navbarCollapse = document.querySelector('.navbar-collapse');
            if (navbarToggle && navbarCollapse && window.getComputedStyle(navbarToggle).display !== 'none') {
                navbarCollapse.classList.remove('in');
            }
        });
    });

    // Highlight the top nav as scrolling occurs (Scrollspy)
    var sections = document.querySelectorAll('section[id]');
    if ('IntersectionObserver' in window && sections.length > 0) {
        var options = {
            root: null,
            rootMargin: '0px 0px -60% 0px',
            threshold: 0
        };
        
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var id = entry.target.getAttribute('id');
                    var activeLink = document.querySelector('.navbar-nav a[href*="#' + id + '"]') || 
                                     document.querySelector('.navbar-nav a[href*="#_' + id + '"]');
                    if (activeLink) {
                        document.querySelectorAll('.navbar-nav li').forEach(function(li) {
                            li.classList.remove('active');
                        });
                        activeLink.parentElement.classList.add('active');
                    }
                }
            });
        }, options);
        
        sections.forEach(function(section) {
            observer.observe(section);
        });
    }

    // Smooth scroll to hash on initial load (using '#_' prefix to prevent browser's default instant jump)
    var hasScrolled = false;

    function triggerHashScroll() {
        if (hasScrolled) return;
        var hash = window.location.hash;
        if (hash && hash.startsWith('#_')) {
            var targetId = hash.substring(2);
            var targetEl = document.getElementById(targetId);
            if (targetEl) {
                var navHeight = 60; // Offset for the fixed navigation bar
                var targetPosition = targetEl.offsetTop - navHeight;
                // If layout is not ready yet (height is 0), wait for load event
                if (targetPosition <= 0 && targetId !== 'page-top') {
                    return;
                }
                hasScrolled = true;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
    }

    if (window.location.hash && window.location.hash.startsWith('#_')) {
        // Force top scroll position initially to avoid any jumpiness
        window.scrollTo(0, 0);
        
        // Try scrolling after 300ms (fast path)
        setTimeout(triggerHashScroll, 300);
        
        // Fallback for slower load or layout delays
        window.addEventListener('load', function() {
            setTimeout(triggerHashScroll, 50);
        });
    }

    // Shrink Navbar on Scroll
    var header = document.querySelector('.navbar-fixed-top');
    if (header) {
        var shrinkNavbar = function() {
            if (window.scrollY >= 100) {
                header.classList.add('navbar-shrink');
            } else {
                header.classList.remove('navbar-shrink');
            }
        };
        window.addEventListener('scroll', shrinkNavbar);
        shrinkNavbar(); // Initial run
    }
});