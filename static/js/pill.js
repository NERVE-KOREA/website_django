// const maincon = document.querySelector('.main-container');
// const rightfloat = document.querySelector('#right-float');

// // 컨텐츠 영역부터 브라우저 최상단까지의 길이 구하기
// const contentTop = maincon.getBoundingClientRect().top + window.scrollY + 600;

// window.addEventListener('scroll', function(){
//   if(window.scrollY >= contentTop){
//     rightfloat.classList.add('fixed');
//   }else{
//     rightfloat.classList.remove('fixed');
//   }
// });

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

window.addEventListener('scroll', () => {
	const bwLeft = window.scrollX;
	document.querySelector('nav').style.transform = `translateX(-${bwLeft}px)`;
  });