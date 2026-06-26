// Centralized Theme Toggle Logic & Mobile Navbar Toggler - LTRJ Labs
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Read cached theme or default to dark mode
    const currentTheme = localStorage.getItem('theme') || 'dark';
    body.classList.add(currentTheme + '-mode');
    
    if (toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            
            const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
            
            // Update body classes and storage
            body.classList.remove('dark-mode', 'light-mode');
            body.classList.add(newTheme + '-mode');
            localStorage.setItem('theme', newTheme);
        });
    }

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
