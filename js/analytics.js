// Google Analytics 4 — loads async, tracks outbound clicks to MothNode.
(function () {
    var GA_MEASUREMENT_ID = 'G-508YGMKJ4D';
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_MEASUREMENT_ID;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', GA_MEASUREMENT_ID);

    document.addEventListener('click', function (e) {
        var a = e.target.closest('a[data-track]');
        if (a) gtag('event', 'cta_click', { cta_id: a.dataset.track, link_url: a.href });
    });
})();
