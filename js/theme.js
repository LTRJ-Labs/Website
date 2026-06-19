// Centralized Theme Toggle Logic - LTRJ Labs
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Read cached theme or default to dark mode
    const currentTheme = localStorage.getItem('theme') || 'dark';
    body.classList.add(currentTheme + '-mode');
    
    if (toggle) {
        toggle.textContent = currentTheme === 'dark' ? '🌙' : '☀️';

        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
            body.classList.remove('dark-mode', 'light-mode');
            body.classList.add(newTheme + '-mode');
            localStorage.setItem('theme', newTheme);
            toggle.textContent = newTheme === 'dark' ? '🌙' : '☀️';
        });
    }
});
