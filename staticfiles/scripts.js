// Navigation menu toggle for mobile devices
document.addEventListener('DOMContentLoaded', () => {
  const mobileMenuButton = document.querySelector('.mobile-menu-button');
  const mobileNav = document.querySelector('.mobile-nav');

  mobileMenuButton.addEventListener('click', () => {
    const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
    mobileMenuButton.setAttribute('aria-expanded', String(!expanded));
    mobileNav.classList.toggle('show');

    // Populate mobile nav links if empty
    if (mobileNav.innerHTML.trim() === '') {
      const navLinks = document.querySelectorAll('.navigation a');
      navLinks.forEach((link) => {
        const mobileLink = link.cloneNode(true);
        mobileLink.setAttribute('tabindex', '0');
        mobileNav.appendChild(mobileLink);
      });
    }
  });
});

