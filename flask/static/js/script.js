let menuMobile = document.querySelector('.lista-mobile')
let imgMenu = document.querySelector('#imgMenu')

function menu(){

    if(menuMobile.style.left == '-100%'){
        menuMobile.style.left = '0%';
        imgMenu.src = "{{ url_for('static', filename='Imagens/close.svg') }}"
    }
    else{
        menuMobile.style.left = '-100%'
        imgMenu.src = "{{ url_for('static', filename='Imagens/menu.svg') }}"
    }
}

let trilho = document.getElementById('trilho')
let corDesktop = document.querySelector(".cor-desktop")
let topDesktop = document.querySelector(".top-desktop")
let passagem = document.querySelector(".passagem")
let labels = document.querySelectorAll("label")
let botoes = document.querySelectorAll(".botoes-desktop")
let containerDesktop = document.querySelector(".container-desktop")

trilho.addEventListener('click', ()=>{
    trilho.classList.toggle('dark')
    corDesktop.classList.toggle('dark')
    topDesktop.classList.toggle('dark')
    passagem.classList.toggle('dark')
    containerDesktop.classList.toggle('dark')


    labels.forEach(label => label.classList.toggle("dark"));

    botoes.forEach(botao => botao.classList.toggle("dark"));


})


function validaRegisterForm() {
    const form = document.getElementById("register-form");
    const idpassagem = form.elements['idpassagem'].value;
    console.log(idpassagem, duracao, dataembarque, dataretorno, destino, origem, classe);
    if (idpassagem !== '' ) {
        alert('Dados cadastrados');
        form.reset();
    } else {
        alert('Preencha todos os dados');
    }
}