var burguer_menu_is_toggled = false
function turn_onof_burguer_menu(e,burguer, burguer_menu){
    if(burguer_menu_is_toggled === false){
        burguer.classList.add('burger-container-show')
        burguer_menu.classList.add('burger-menu-show')

        burguer.classList.remove('burger-container-hidde')
        burguer_menu.classList.remove('burger-menu-hidde')
    

    burguer_menu_is_toggled = true

    console.log(e,burguer, burguer_menu,'TRUE')

    } else {
            burguer.classList.remove('burger-container-show')
            burguer_menu.classList.remove('burger-menu-show')
            
            burguer.classList.add('burger-container-hidde')
            burguer_menu.classList.add('burger-menu-hidde')

            burguer_menu_is_toggled = false

            console.log(e,burguer, burguer_menu,'false')
        };
    }
export {turn_onof_burguer_menu}
