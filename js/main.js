/* ============================================
   Arthur Lynch — Main JavaScript
   Lightweight, performance-focused
   ============================================ */

(function () {
  'use strict';

  /* --- Mobile Navigation Toggle --- */
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
      const expanded = navLinks.classList.contains('open');
      menuToggle.setAttribute('aria-expanded', expanded);
    });

    // Close menu when a link is clicked
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --- Header Scroll Effect --- */
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  /* --- Active Navigation Highlighting --- */
  function setActiveNav() {
    var path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(function (link) {
      var href = link.getAttribute('href');
      if (href === path || (path === '' && href === 'index.html')) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }
  setActiveNav();

  /* --- Lazy Section Fade-In --- */
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.lazy-section').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // Fallback: show all sections immediately
    document.querySelectorAll('.lazy-section').forEach(function (el) {
      el.classList.add('visible');
    });
  }

  /* --- Contact Form Handler --- */
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function () {
      var btn = contactForm.querySelector('button[type="submit"]');
      btn.textContent = 'Sending...';
      btn.disabled = true;
    });
  }

  /* --- Smooth scroll for anchor links --- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;
      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var offset = 80;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

})();
