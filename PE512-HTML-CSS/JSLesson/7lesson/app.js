// const form = document.getElementById("taskForm")

// form.addEventListener("submit", () =>{
//     alert("Форма отправлена")
// })

// form.addEventListener("submit", function(event){
//     event.preventDefault()
//     alert("Форма отправлена")
// })

// document.addEventListener("keydown", (event ) => {
//     console.log(event.key)
// })

// const btn = document.getElementById("btn")
// btn.addEventListener("click", (event) => {
//     console.log(event)
// })


// const form = document.getElementById("taskForm")
// const input = document.getElementById("taskInput")
// const result = document.getElementById("result")

// form.addEventListener("submit", function(event){
//     event.preventDefault()
//     const text = input.value.trim()
//     if(text == ""){
//         alert("Ввведите задачу")
//     }

//     result.textContent = "Вы ввели: " + text
// })



// const form = document.getElementById("taskForm")
// const input = document.getElementById("taskInput")
// const result = document.getElementById("result")
// const success = document.getElementById("success")
// const error = document.getElementById("error")

// form.addEventListener("submit", (event) => {
//     event.preventDefault()
//     const text = input.value.trim()
//     error.textContent = ""
//     success.textContent = ""

//     if(text === ""){
//         error.textContent = "Поле не может быть пустым"
//         error.style.color = "red"
//         return
//     }
//     if(text.length < 3){
//         error.textContent = "Задача должна содержать не менее 3 символов"
//         error.style.color = "red"

//         return
//     }
//     if(text.length > 20){
//         error.textContent = "Задача не должна превышать 20 символов"
//         error.style.color = "red"
//         return
//     }
//     success.textContent = "Задача добавлена: " + text
//     success.style.color = "green"
//     input.value = ""
// })


// Login Register Validation practice

const loginForm = document.getElementById("loginForm")
const registerForm = document.getElementById("registerForm")

const loginPassword = document.getElementById("loginPassword")
const regPassword = document.getElementById("regPassword")

const showLoginPassword = document.getElementById("showLoginPassword")
const showRegPassword = document.getElementById("showRegPassword")

if(showLoginPassword && loginPassword){
    showLoginPassword.addEventListener("click", function() {
        if(loginPassword.type === "password"){
            loginPassword.type = "text"
            showLoginPassword.textContent = "Hide Password"
        }
        else{            loginPassword.type === "password"
            showLoginPassword.textContent = "Show Password"
        }
    })
}

if(showRegPassword && regPassword){
    showRegPassword.addEventListener("click", function() {
        if(regPassword.type === "password"){
            regPassword.type = "text"
            showRegPassword.textContent = "Hide Password"
        }
        else{            regPassword.type === "password"
            showRegPassword.textContent = "Show Password"
        }
    })
}

if(loginForm){
    loginForm.addEventListener("submit", function(event){
        event.preventDefault()
    const name = document.getElementById("loginName").value.trim()
    const password = loginPassword.value.trim()

    if(name.length < 2 || name.length > 15){
        const loginNameError = document.getElementById("loginNameError")
        loginNameError.textContent = "Имя пользователя должно содержать от 2 до 15 символов"
        loginNameError.style.color = "red"
        return
    }
    if(password.length < 6){
        const loginPasswordError = document.getElementById("loginPasswordError")
        loginPasswordError.textContent = "Пароль должен содержать не менее 6 символов"
        loginPasswordError.style.color = "red"
        return
    })
}

if(registerForm){
    registerForm.addEventListener("submit", function(event){
        event.preventDefault()
    const name = document.getElementById("registerName").value.trim()
    const password = regPassword.value.trim()

    if(name.length < 2 || name.length > 15){
        const registerNameError = document.getElementById("registerNameError")
        registerNameError.textContent = "Имя пользователя должно содержать от 2 до 15 символов"
        registerNameError.style.color = "red"
        return
    }

    })
}
