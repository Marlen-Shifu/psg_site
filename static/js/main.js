let topBtn = document.querySelector('.topBtn');
topBtn.onclick = () =>{
	window.scroll(0,0);
}

window.onscroll = function showHeader() {
	let header = document.querySelector('.navbar');
	if(window.pageYOffset > 30){
		header.classList.add('navbar_white');
		topBtn.style.visibility = 'visible';
	}else{
		header.classList.remove('navbar_white');
		topBtn.style.visibility = 'hidden';
	}
}

const burgerMenu = document.querySelector('.navbar__burger');
const menuList = document.querySelector('.navbar__menu');
const body = document.querySelector('body');
const links = document.querySelectorAll('.navbar__link');
burgerMenu.onclick = function showBurger(){
	this.classList.toggle('activeBurger');
	menuList.classList.toggle('activeBurger');
	body.classList.toggle('lockScroll');
}
for (i = 0; i < links.length; ++i) {
	links[i].onclick = function hideMenu(){
		burgerMenu.classList.toggle('activeBurger');
		menuList.classList.toggle('activeBurger');
		body.classList.remove('lockScroll');
		console.log('asd');
	}
}

const callMe = document.querySelector('.navbar__tel');
const callMeBody = document.querySelector('.call__body');
const closeBtn = document.querySelector('.closeBtn');
callMe.onclick = () =>{
	callMeBody.style.display = "flex";
	// body.classList.add('lockScroll');
}
closeBtn.onclick = () =>{
	callMeBody.style.display = "none";
	// body.classList.remove('lockScroll')
}


