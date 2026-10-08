/* Scroll motion for the mockup: reveals, headline words, counters, parallax,
   sticky header, progress bar and timeline fills. No libraries, works offline. */
(function () {
  var d = document, root = d.documentElement;
  if (/[?&]static\b/.test(location.search)) { root.classList.add('static'); return; }
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('js');

  // Headline words rise one by one (works for any language, keeps <em> etc.)
  if (!reduce) d.querySelectorAll('[data-split]').forEach(function (el) {
    var i = 0;
    (function walk(node) {
      [].slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = d.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(d.createTextNode(part)); return; }
            var w = d.createElement('span'), s = d.createElement('span');
            w.className = 'w'; s.textContent = part; s.style.setProperty('--i', i++);
            w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) walk(n);
      });
    })(el);
  });

  // Reveal on scroll, with staggered groups
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in'); io.unobserve(e.target);
      if (e.target.hasAttribute('data-count')) count(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }) : null;

  d.querySelectorAll('[data-stagger]').forEach(function (g) {
    var step = parseInt(g.getAttribute('data-stagger'), 10) || 90;
    [].forEach.call(g.children, function (c, i) {
      if (!c.hasAttribute('data-reveal')) c.setAttribute('data-reveal', 'up');
      c.style.setProperty('--d', (i * step) + 'ms');
    });
  });
  d.querySelectorAll('[data-reveal],[data-count]').forEach(function (el) {
    if (io) io.observe(el); else el.classList.add('in');
  });

  // Count-up numbers
  function count(el) {
    if (reduce) return;
    var to = parseFloat(el.getAttribute('data-count')), from = parseFloat(el.getAttribute('data-from') || 0);
    var t0 = null, dur = 1600, suffix = el.getAttribute('data-suffix') || '';
    function f(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(from + (to - from) * e) + suffix;
      if (k < 1) requestAnimationFrame(f);
    }
    requestAnimationFrame(f);
  }

  // Scroll-linked effects
  var nav = d.querySelector('nav'), bar = d.querySelector('.progress');
  var px = [].slice.call(d.querySelectorAll('[data-parallax]'));
  var fills = [].slice.call(d.querySelectorAll('[data-fill]'));
  var ticking = false;
  function frame() {
    ticking = false;
    var y = window.scrollY || window.pageYOffset, vh = window.innerHeight;
    var max = root.scrollHeight - vh;
    if (nav) nav.classList.toggle('scrolled', y > 40);
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
    if (!reduce) px.forEach(function (el) {
      var r = el.getBoundingClientRect(), c = r.top + r.height / 2 - vh / 2;
      el.style.transform = 'translate3d(0,' + (-c * parseFloat(el.getAttribute('data-parallax'))).toFixed(1) + 'px,0)';
    });
    fills.forEach(function (el) {
      var r = el.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, (vh * 0.8 - r.top) / (r.height + vh * 0.25)));
      el.style.setProperty('--p', p.toFixed(3));
      var steps = el.querySelectorAll('[data-step]');
      [].forEach.call(steps, function (s, i) { s.classList.toggle('lit', p >= (i + 0.35) / steps.length); });
    });
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  frame();
})();
