// navbar 스크롤 애니메이션

const navbar = document.querySelector('nav');
const navbarHeight = navbar.getBoundingClientRect().height;

document.addEventListener('scroll', () => {
    if(window.scrollY > navbarHeight) {
        navbar.classList.add('navbar--dark');
    } else {
        navbar.classList.remove('navbar--dark');
    }
});