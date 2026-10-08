// TEMPORARY — design exploration switcher. Delete this file and its <script> tags once a direction is chosen.
// Prev/next arrows, a jump-to menu, and the [ / ] keys cycle through every concept.
(function () {
    var root = location.pathname.indexOf('/concepts/') > -1 ? '../' : '';
    var concepts = [
        ['A', 'Ethereal', 'index.html'],
        ['B', 'Notebook', 'concepts/notebook.html'],
        ['C', 'Console', 'concepts/console.html'],
        ['D', 'Monolith', 'concepts/monolith.html'],
        ['E', 'Claymorphism', 'concepts/claymorphism.html'],
        ['F', 'Cybercore', 'concepts/cybercore.html'],
        ['G', 'Neobrutalism', 'concepts/neobrutalism.html'],
        ['H', 'Surrealism', 'concepts/surrealism.html'],
        ['I', 'Pixel Art', 'concepts/pixel.html'],
        ['J', 'Synthwave', 'concepts/synthwave.html'],
        ['K', 'Glassmorphism', 'concepts/glassmorphism.html'],
        ['L', 'Neumorphism', 'concepts/neumorphism.html'],
        ['M', 'Bento Grid', 'concepts/bento.html'],
        ['N', 'Swiss', 'concepts/swiss.html'],
        ['O', 'Minimalism', 'concepts/minimal.html'],
        ['P', 'Luxury Type', 'concepts/luxury.html'],
        ['Q', 'Concept Sketch', 'concepts/sketch.html'],
        ['R', 'Bohemian', 'concepts/bohemian.html'],
        ['S', 'Cyberpunk', 'concepts/cyberpunk.html']
    ];
    var here = location.pathname.split('/').pop() || 'index.html';
    var idx = 0;
    concepts.forEach(function (c, i) { if (c[2].split('/').pop() === here) idx = i; });
    function go(i) { location.href = root + concepts[(i + concepts.length) % concepts.length][2]; }

    var bar = document.createElement('nav');
    bar.setAttribute('aria-label', 'Design concepts');
    bar.style.cssText = 'position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:2147483000;display:flex;align-items:center;gap:2px;padding:4px;border-radius:999px;background:rgba(10,10,12,.86);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.14);font:500 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.03em;box-shadow:0 8px 30px rgba(0,0,0,.35);color:#c9c9cf;max-width:calc(100vw - 24px)';

    function btn(label, title, fn) {
        var b = document.createElement('button');
        b.type = 'button'; b.textContent = label; b.title = title; b.setAttribute('aria-label', title);
        b.style.cssText = 'all:unset;cursor:pointer;padding:8px 12px;border-radius:999px;color:#c9c9cf';
        b.onmouseenter = function () { b.style.background = 'rgba(255,255,255,.1)'; };
        b.onmouseleave = function () { b.style.background = 'none'; };
        b.onclick = fn;
        return b;
    }

    var sel = document.createElement('select');
    sel.setAttribute('aria-label', 'Jump to concept');
    sel.style.cssText = 'all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;background:#FF7A1A;color:#0a0a0c;font-weight:600;max-width:52vw;overflow:hidden;text-overflow:ellipsis;white-space:nowrap';
    concepts.forEach(function (c, i) {
        var o = document.createElement('option');
        o.value = i; o.textContent = c[0] + ' · ' + c[1] + '  (' + (i + 1) + '/' + concepts.length + ')';
        o.style.cssText = 'background:#111;color:#eee';
        if (i === idx) o.selected = true;
        sel.appendChild(o);
    });
    sel.onchange = function () { go(+sel.value); };

    bar.appendChild(btn('←', 'Previous concept ( [ )', function () { go(idx - 1); }));
    bar.appendChild(sel);
    bar.appendChild(btn('→', 'Next concept ( ] )', function () { go(idx + 1); }));

    document.addEventListener('keydown', function (e) {
        if (e.metaKey || e.ctrlKey || e.altKey || /input|textarea|select/i.test(e.target.tagName)) return;
        if (e.key === '[') go(idx - 1);
        if (e.key === ']') go(idx + 1);
    });
    document.addEventListener('DOMContentLoaded', function () { document.body.appendChild(bar); });
})();
