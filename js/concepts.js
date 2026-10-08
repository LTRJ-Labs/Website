// TEMPORARY — design exploration switcher. Delete this file and its <script> tags once a direction is chosen.
(function () {
    var root = location.pathname.indexOf('/concepts/') > -1 ? '../' : '';
    var concepts = [
        ['A', 'Ethereal', root + 'index.html'],
        ['B', 'Notebook', root + 'concepts/notebook.html'],
        ['C', 'Console', root + 'concepts/console.html'],
        ['D', 'Monolith', root + 'concepts/monolith.html']
    ];
    var here = location.pathname.split('/').pop() || 'index.html';
    var bar = document.createElement('nav');
    bar.setAttribute('aria-label', 'Design concepts');
    bar.style.cssText = 'position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:9999;display:flex;gap:2px;padding:4px;border-radius:999px;background:rgba(10,10,12,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.12);font:500 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.04em;box-shadow:0 8px 30px rgba(0,0,0,.35)';
    concepts.forEach(function (c) {
        var a = document.createElement('a');
        var active = c[2].split('/').pop() === here;
        a.href = c[2];
        a.textContent = window.innerWidth < 520 ? c[0] + ' ' + c[1].slice(0, 4) : c[0] + ' · ' + c[1];
        a.title = c[1];
        a.style.cssText = 'padding:8px 12px;border-radius:999px;text-decoration:none;white-space:nowrap;color:' + (active ? '#0a0a0c;background:#FF7A1A' : '#c9c9cf');
        bar.appendChild(a);
    });
    document.addEventListener('DOMContentLoaded', function () { document.body.appendChild(bar); });
})();
