// ===== SHARED LANGUAGE TOGGLE =====
// Inject baseline CSS so lang-zh is hidden before JS runs (prevents flash)
(function() {
  var style = document.createElement('style');
  style.textContent = '.lang-zh { display: none !important; }';
  style.id = 'lang-baseline';
  document.head.appendChild(style);
})();

function setLang(lang) {
  // Remove baseline hide rule once we're in control
  var baseline = document.getElementById('lang-baseline');
  if (baseline) baseline.parentNode.removeChild(baseline);

  document.querySelectorAll('.lang-en').forEach(function(el) {
    el.style.display = lang === 'en' ? '' : 'none';
  });
  document.querySelectorAll('.lang-zh').forEach(function(el) {
    el.style.display = lang === 'zh' ? 'inline' : 'none';
  });
  localStorage.setItem('jyt-lang', lang);
  document.documentElement.lang = lang;
  var btn = document.getElementById('langToggle');
  if (btn) btn.textContent = lang === 'en' ? 'EN / 中' : '中 / EN';
}

function toggleLang() {
  var current = localStorage.getItem('jyt-lang') || 'en';
  setLang(current === 'en' ? 'zh' : 'en');
}

// Apply saved language preference on page load
(function() {
  var saved = localStorage.getItem('jyt-lang') || 'en';
  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { setLang(saved); });
  } else {
    setLang(saved);
  }
})();
