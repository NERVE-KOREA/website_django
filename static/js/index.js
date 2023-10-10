
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

// window.addEventListener('scroll', () => {
// 	const bwLeft = window.scrollX;
// 	document.querySelector('nav').style.transform = `translateX(-${bwLeft}px)`;
//   });


// 자동롤링배너

let roller = document.querySelector('.banner1');
roller.id = 'roller1'; // 아이디 부여

let clone = roller.cloneNode(true)
// cloneNode : 노드 복제. 기본값은 false. 자식 노드까지 복제를 원하면 true 사용
clone.id = 'roller2';
document.querySelector('.banner-wrap').appendChild(clone); // wrap 하위 자식으로 부착

document.querySelector('#roller1').style.left = '0px';
document.querySelector('#roller2').style.left = document.querySelector('.flow-text').offsetWidth + 'px';
// offsetWidth : 요소의 크기 확인(margin을 제외한 padding값, border값까지 계산한 값)

roller.classList.add('original');
clone.classList.add('clone');

// // 자동롤링배너2

// let roll = document.querySelector('.main-section4-imgs');
// roll.id = 'roller3'; // 아이디 부여

// let clone2 = roll.cloneNode(true)
// // cloneNode : 노드 복제. 기본값은 false. 자식 노드까지 복제를 원하면 true 사용
// clone2.id = 'roller4';
// document.querySelector('.section4-wrap').appendChild(clone2); // wrap 하위 자식으로 부착

// document.querySelector('#roller3').style.left = '0px';
// document.querySelector('#roller4').style.left = document.querySelector('.main-section4-imgs').offsetWidth + 'px';
// // offsetWidth : 요소의 크기 확인(margin을 제외한 padding값, border값까지 계산한 값)

// roll.classList.add('original');
// clone2.classList.add('clone');

var slideIndex = 0;
    showSlides();

    function showSlides() {
        var i;
        var slides = document.getElementsByClassName("main-section1-img");
       
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1
        }
        slides[slideIndex - 1].style.display = "block";
    
        setTimeout(showSlides, 2500); // 2초마다 이미지가 체인지됩니다
    };

var slideIndex1 = 0;
    showSlides1();

    function showSlides1() {
        var i;
        var slides1 = document.getElementsByClassName("section4-img");
       
        for (i = 0; i < slides1.length; i++) {
            slides1[i].style.display = "none";
        }
        slideIndex1++;
        if (slideIndex1 > slides1.length) {
            slideIndex1 = 1
        }
        slides1[slideIndex1 - 1].style.display = "block";
    
        setTimeout(showSlides1, 2500); // 2초마다 이미지가 체인지됩니다
    };
