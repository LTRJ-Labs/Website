// Google Analytics 4 (GA4) Integration for LTRJ Labs
// This script loads Google Analytics asynchronously and tracks core website interactions.

const GA_MEASUREMENT_ID = 'G-XXXXXXXXXX'; // REPLACE WITH YOUR ACTUAL GA4 MEASUREMENT ID

(function() {
    // 1. Inject the Google Analytics tag script into <head>
    const gaScript = document.createElement('script');
    gaScript.async = true;
    gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
    document.head.appendChild(gaScript);

    // 2. Initialize the global dataLayer and gtag functions
    window.dataLayer = window.dataLayer || [];
    window.gtag = function() {
        dataLayer.push(arguments);
    };
    
    // 3. Configure Google Analytics
    gtag('js', new Date());
    // Enhanced Measurement in GA4 automatically captures page views, scrolls (at 90% depth), outbound clicks, site search, and file downloads.
    gtag('config', GA_MEASUREMENT_ID);

    // 4. Custom tracking: Portfolio product/work item clicks
    document.addEventListener('DOMContentLoaded', function() {
        const portfolioLinks = document.querySelectorAll('.portfolio-link');
        portfolioLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                // Find item details from parent/siblings
                const parentItem = this.closest('.portfolio-item');
                let itemName = 'Unknown Item';
                let itemCategory = 'Portfolio';
                
                if (parentItem) {
                    const caption = parentItem.querySelector('.portfolio-caption');
                    if (caption) {
                        const titleEl = caption.querySelector('h4');
                        const categoryEl = caption.querySelector('p');
                        if (titleEl) itemName = titleEl.textContent.trim();
                        if (categoryEl) itemCategory = categoryEl.textContent.trim();
                    }
                }
                
                // Extract item ID from the link href (e.g. "mothnode/", "ecet260/")
                const href = this.getAttribute('href') || '';
                const itemId = href.replace(/\/$/, '').split('/').pop() || 'unknown';

                // Send the select_item event to GA4
                gtag('event', 'select_item', {
                    item_list_id: 'portfolio_grid',
                    item_list_name: 'Portfolio Grid',
                    items: [{
                        item_id: itemId,
                        item_name: itemName,
                        item_category: itemCategory
                    }]
                });
            });
        });
    });
})();
