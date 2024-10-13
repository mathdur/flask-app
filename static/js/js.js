function edit(login) {
    elements = document.querySelectorAll(".actions")
    elements.forEach(function(element) {
        element.style.display = "none"
    })

    element = document.querySelector("#"+login["id"])
    element.style.display = "block"

}

function edit_affectation(numero) {
    elements = document.querySelectorAll(".actions")
    elements.forEach(function(element) {
        element.style.display = "none"
    })

    element = document.querySelector("#num_"+numero)
    element.style.display = "block"

}

function edit_service(code) {
    elements = document.querySelectorAll(".actions")
    elements.forEach(function(element) {
        element.style.display = "none"
    })

    element = document.querySelector("#"+code['id'])
    element.style.display = "block"
}



function profil() {
    element = document.querySelector(".profil-uga")
    element.style.display = "none"
    element = document.querySelector("#profil-uga")
    element.setAttribute("class","nav-link text-active-primary pb-4")
    element = document.querySelector(".profil")
    element.style.display = "block"
    element = document.querySelector("#profil")
    element.setAttribute("class","nav-link text-active-primary pb-4 active")
}


function profil_uga() {
    element = document.querySelector(".profil")
    element.style.display = "none"
    element = document.querySelector("#profil")
    element.setAttribute("class","nav-link text-active-primary pb-4")
    element = document.querySelector(".profil-uga")
    element.style.display = "block"
    element = document.querySelector("#profil-uga")
    element.setAttribute("class","nav-link text-active-primary pb-4 active")
}


