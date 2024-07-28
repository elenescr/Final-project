document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.navbar-nav li a'); // Adjust selector if needed

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    const pathname = window.location.pathname;

    if (href === pathname) {
      link.parentElement.classList.add('active');
    } else {
      link.parentElement.classList.remove('active');
    }
  });
});
