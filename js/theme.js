/* AGENT-INFO
=========================================================
LTRJ LABS JAVASCRIPT
- Functionality: Handles scrolling navbar collapse, smooth page transitions, modal loading, and contact form anti-scraping logic.
- jQuery is heavily used for the legacy Bootstrap 3 plugins, while modern features (like clipboard copying) use Vanilla JS.
=========================================================
*/
// Centralized Theme Toggle Logic & Mobile Navbar Toggler - LTRJ Labs
document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;

    // Theme is fixed dark. Clear any legacy 'light' preference left in
    // localStorage by the old (now removed) theme toggle.
    localStorage.removeItem('theme');
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');

    // --- Vanilla JS Mobile Navbar Toggle ---
    var toggles = document.querySelectorAll('.navbar-toggle');
    toggles.forEach(function(navbarToggle) {
        navbarToggle.addEventListener('click', function() {
            var targetId = navbarToggle.getAttribute('data-target');
            if (targetId) {
                var target = document.querySelector(targetId);
                if (target) {
                    target.classList.toggle('in');
                }
            }
        });
    });
});
