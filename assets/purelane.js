
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- reveal on scroll ---------- */
  var revs = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var ro = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    revs.forEach(function (el) { ro.observe(el); });
  } else {
    revs.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- scene crossfade & rail sync (cached layout metrics, 0 DOM thrashing) ---------- */
  var scenes = [].slice.call(document.querySelectorAll('.scene'));
  var zones = [].slice.call(document.querySelectorAll('[data-scene]'));
  var stage = document.getElementById('scenes');
  var rail = document.querySelector('.rail');
  var railLinks = rail ? [].slice.call(rail.querySelectorAll('a')) : [];
  var currentScene = 0;

  var zoneMetrics = [];
  var railTargets = [];

  function measureLayout() {
    var scrollY = window.scrollY || window.pageYOffset;
    zoneMetrics = zones.map(function (z) {
      var rect = z.getBoundingClientRect();
      return {
        top: rect.top + scrollY,
        scene: parseInt(z.getAttribute('data-scene'), 10) || 1
      };
    });

    railTargets = railLinks.map(function (a) {
      try {
        var href = a.getAttribute('href');
        var el = href && href.startsWith('#') ? document.querySelector(href) : null;
        if (!el) return null;
        return el.getBoundingClientRect().top + scrollY;
      } catch (e) {
        return null;
      }
    });
  }

  function setScene(n) {
    if (n === currentScene) return;
    currentScene = n;
    scenes.forEach(function (s, i) { s.classList.toggle('on', i + 1 === n); });
    if (stage) stage.setAttribute('data-d', String(n));
  }

  function pickScene(focusY) {
    if (!zoneMetrics.length) return;
    var n = 1;
    for (var i = 0; i < zoneMetrics.length; i++) {
      if (zoneMetrics[i].top <= focusY) n = zoneMetrics[i].scene;
    }
    setScene(n);
  }

  function syncRail(midY) {
    if (!railLinks.length || !railTargets.length) return;
    var idx = 0;
    railTargets.forEach(function (top, i) {
      if (top !== null && top <= midY) idx = i;
    });
    railLinks.forEach(function (a, i) { a.classList.toggle('on', i === idx); });
  }

  /* ---------- parallax + header (GPU-optimized) ---------- */
  var hdr = document.getElementById('hdr');
  var prod = document.getElementById('heroProd');
  var wl = [].slice.call(document.querySelectorAll('#water .wl'));
  var raf = null, mx = 0, my = 0;
  var isHeroVisible = true;

  function frame() {
    raf = null;
    var y = window.scrollY || window.pageYOffset;
    if (hdr) hdr.classList.toggle('up', y > 90);

    isHeroVisible = y < window.innerHeight * 1.2;

    if (!reduce && isHeroVisible) {
      if (wl.length) {
        var depthFactors = [0.04, 0.07, 0.02, 0.02];
        for (var i = 0; i < wl.length; i++) {
          var d = depthFactors[i] || 0.04;
          var px = (mx * d * 100).toFixed(1);
          var py = (-y * d + my * d * 60).toFixed(1);
          wl[i].style.transform = 'translate3d(' + px + 'px,' + py + 'px,0)';
        }
      }
      if (prod) {
        var f = Math.min(y / 650, 1);
        var ptx = (mx * -14).toFixed(1);
        var pty = (-f * 50 + my * -8).toFixed(1);
        var scale = (1 - f * 0.05).toFixed(3);
        prod.style.transform = 'translate3d(' + ptx + 'px,' + pty + 'px,0) scale(' + scale + ')';
        prod.style.opacity = (1 - f * 0.55).toFixed(3);
      }
    }

    var winH = window.innerHeight;
    syncRail(y + winH * 0.42);
    pickScene(y + winH * 0.5);
  }

  function onScroll() {
    if (!raf) raf = requestAnimationFrame(frame);
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  var resizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      measureLayout();
      onScroll();
    }, 150);
  });

  if (!reduce && window.matchMedia('(min-width: 1024px)').matches) {
    window.addEventListener('mousemove', function (e) {
      mx = (e.clientX / window.innerWidth - 0.5) * 2;
      my = (e.clientY / window.innerHeight - 0.5) * 2;
      if (isHeroVisible) onScroll();
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', measureLayout);
  } else {
    measureLayout();
  }

  /* ---------- hero stage: 1 -> 2 -> 3 products ---------- */
  var hstage = document.getElementById('hstage');
  if (hstage) {
    var hs = [].slice.call(hstage.querySelectorAll('.hslide'));
    var hd = [].slice.call(document.querySelectorAll('#hdots button'));
    var hi = 0, htimer = null;
    function hgo(n) {
      hi = (n + hs.length) % hs.length;
      hs.forEach(function (s, i) { s.classList.toggle('on', i === hi); });
      hd.forEach(function (d, i) { d.classList.toggle('on', i === hi); });
    }
    function hplay() { if (!htimer && !reduce) htimer = setInterval(function () { hgo(hi + 1); }, 3800); }
    function hstop() { if (htimer) { clearInterval(htimer); htimer = null; } }
    hd.forEach(function (d, i) {
      d.addEventListener('click', function () { hstop(); hgo(i); hplay(); });
    });
    hstage.addEventListener('mouseenter', hstop);
    hstage.addEventListener('mouseleave', hplay);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? hplay() : hstop(); });
      }, { threshold: 0.2 }).observe(hstage);
    } else { hplay(); }
  }

  /* ---------- product rotator ---------- */
  var rot = document.getElementById('rot');
  if (rot) {
    var rimgs = [].slice.call(rot.querySelectorAll('.frame .pimg'));
    var rdots = [].slice.call(rot.querySelectorAll('.dots i'));
    var rcapB = rot.querySelector('.cap b');
    var rcapS = rot.querySelector('.cap span');
    var ri = 0, rtimer = null;
    function rstep() {
      rimgs[ri].classList.remove('on');
      if (rdots[ri]) rdots[ri].classList.remove('on');
      ri = (ri + 1) % rimgs.length;
      rimgs[ri].classList.add('on');
      if (rdots[ri]) rdots[ri].classList.add('on');
      rcapB.innerHTML = rimgs[ri].getAttribute('data-name');
      rcapS.textContent = rimgs[ri].getAttribute('data-note');
    }
    if (!reduce) {
      var rio = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !rtimer) rtimer = setInterval(rstep, 2900);
          else if (!e.isIntersecting && rtimer) { clearInterval(rtimer); rtimer = null; }
        });
      }, { threshold: 0.25 });
      rio.observe(rot);
    }
  }

  frame();
})();

/* ---------- Comborail Prev/Next Desktop Arrows ---------- */
document.addEventListener('DOMContentLoaded', function () {
  var prevBtn = document.querySelector('.rail-arrow--prev');
  var nextBtn = document.querySelector('.rail-arrow--next');
  var rail = document.querySelector('.comborail');

  if (rail) {
    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        rail.scrollBy({ left: -320, behavior: 'smooth' });
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        rail.scrollBy({ left: 320, behavior: 'smooth' });
      });
    }
  }

  /* ---------- Mobile Drawer Toggle ---------- */
  var burger = document.getElementById('burgerToggle');
  var drawer = document.getElementById('mobileDrawer');
  if (burger && drawer) {
    burger.addEventListener('click', function (e) {
      e.stopPropagation();
      var isHidden = drawer.hasAttribute('hidden');
      if (isHidden) {
        drawer.removeAttribute('hidden');
        burger.setAttribute('aria-expanded', 'true');
      } else {
        drawer.setAttribute('hidden', '');
        burger.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('click', function (e) {
      if (!drawer.contains(e.target) && !burger.contains(e.target)) {
        drawer.setAttribute('hidden', '');
        burger.setAttribute('aria-expanded', 'false');
      }
    });

    drawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        drawer.setAttribute('hidden', '');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- Smooth Anchor Scrolling for On-page Links ---------- */
  document.querySelectorAll('a[href*="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (!href) return;
      var hashIdx = href.indexOf('#');
      if (hashIdx === -1) return;
      var hash = href.substring(hashIdx);
      if (!hash || hash === '#') return;
      try {
        var target = document.querySelector(hash);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
          if (history.pushState) {
            history.pushState(null, null, hash);
          }
        }
      } catch (err) {
        // If not a valid query selector or target doesn't exist, allow normal navigation
      }
    });
  });
});

