let menuMobile = document.querySelector('.lista-mobile')
let imgMenu = document.querySelector('#imgMenu')

function menu(){

    if(menuMobile.style.left == '-100%'){
        menuMobile.style.left = '0%';
        imgMenu.src = "../Imagens/close.svg"
    }
    else{
        menuMobile.style.left = '-100%'
        imgMenu.src = "../Imagens/menu.svg"
    }
}