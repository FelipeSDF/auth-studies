import {turn_onof_burguer_menu} from './partials/header.js'

var burguer = document.getElementById('burguer-container')
var burguer_menu = document.getElementById('burguer-menu-container')

burguer.addEventListener('click', (e) => turn_onof_burguer_menu(e,burguer,burguer_menu))