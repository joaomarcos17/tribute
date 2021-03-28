// mobile menu !!
const burgerIcon = document.querySelector('#burger');

const navbarMenu = document.querySelector('#navlinks');

burgerIcon.addEventListener('click', () => {

    navbarMenu.classList.toggle('is-active');


});