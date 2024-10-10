hidden_elements = document.querySelectorAll('.hidden-effect')
hidden_elements.forEach(
    (element) => {
        element.addEventListener('click', extend_card)
        element.addEventListener('click', extend_card)
    }
)

const observer = new IntersectionObserver((elements) => {
    elements.forEach((element) => {
        if (element.isIntersecting) {
            element.target.classList.add('show-effect')
            element.target.classList.remove('hidden-effect')


        }
        else {
            element.target.classList.add('hidden-effect')

            element.target.classList.remove('show-effect')
        }
    });
})

hidden_elements.forEach((element) => observer.observe(element))

let isactivated = false;
function extend_card() {
    if (isactivated === false){
        this.classList.add('openned-card')
        this.classList.remove('closed-card')
        isactivated = true
    }else{
        this.classList.add('closed-card')
        this.classList.remove('openned-card')
        isactivated = false
    }

}
