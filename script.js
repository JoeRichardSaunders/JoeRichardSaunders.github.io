document.addEventListener('DOMContentLoaded', () => {

  // ===== MOBILE NAV =====
  const toggle = document.getElementById('nav-toggle');
  const sidebar = document.getElementById('sidebar');
  const links = document.querySelectorAll('.nav-link');

  if (toggle && sidebar) {
    toggle.addEventListener('click', () => {
      sidebar.classList.toggle('active');
      const icon = toggle.querySelector('i');
      if (!icon) return;
      if (sidebar.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
      } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }
    });

    links.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          sidebar.classList.remove('active');
          const icon = toggle.querySelector('i');
          if (!icon) return;
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      });
    });
  }

  // ===== TABS (The Evidence section) =====
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  if (tabBtns.length > 0) {
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-target');

        // Remove active from all buttons
        tabBtns.forEach(b => b.classList.remove('active'));

        // Hide all panels
        tabPanels.forEach(p => {
          p.classList.remove('active');
          p.style.display = 'none';
        });

        // Activate clicked button
        btn.classList.add('active');

        // Show target panel
        const activePanel = document.getElementById(target);
        if (activePanel) {
          activePanel.classList.add('active');
          activePanel.style.display = 'block';
        }
      });
    });

    // Activate first tab on load
    if (tabBtns[0] && tabPanels[0]) {
      tabBtns[0].classList.add('active');
      tabPanels[0].classList.add('active');
      tabPanels[0].style.display = 'block';
    }
  }

  // ===== SLIDESHOW (autoplay) =====
  let ncmSlideIndex = 0;
  let ncmSlideTimer = null;

  function showNcmSlides() {
    const slides = document.getElementsByClassName('ncm-slide');
    const dots = document.getElementsByClassName('ncm-dot');
    if (slides.length === 0) return;

    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = 'none';
    }
    for (let i = 0; i < dots.length; i++) {
      dots[i].classList.remove('ncm-active');
    }

    ncmSlideIndex++;
    if (ncmSlideIndex > slides.length) ncmSlideIndex = 1;

    slides[ncmSlideIndex - 1].style.display = 'block';
    if (dots[ncmSlideIndex - 1]) {
      dots[ncmSlideIndex - 1].classList.add('ncm-active');
    }

    ncmSlideTimer = setTimeout(showNcmSlides, 5000);
  }

  function plusNcmSlides(n) {
    clearTimeout(ncmSlideTimer);
    ncmSlideIndex += n - 1;
    showNcmSlides();
  }

  function currentNcmSlide(n) {
    clearTimeout(ncmSlideTimer);
    ncmSlideIndex = n - 1;
    showNcmSlides();
  }

  window.plusNcmSlides = plusNcmSlides;
  window.currentNcmSlide = currentNcmSlide;

  showNcmSlides();

});
