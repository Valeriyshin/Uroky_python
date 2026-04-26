// 1. подключение JS к HTML
// const title = document.getElementById("title") -> обращение к элементу
// console.log(title)
// console.log(document)
// console.log(document.body)
// console.log(document.title)

// 1.
// getElementById получение одного элемента через ID

// 2. getElementsByClassName Возвращает коллекцию элементов
// const texts = document.getElementsByClassName("text")
// console.log(texts)

// 3. getElementsByTagName -> Возвращает коллекцию элементов по тегу
// const paras = document.getElementsByTagName("p")
// console.log(paras)

// 4. 
// querySelector -> Универсальный метод, который возвращает первый элемент по CSS селектору
// const sub = document.querySelector(".subtitle")
// console.log(sub)
// .main
// #main
// p 

// 5. 
// querySelectorAll
// const allTexts = document.querySelectorAll(".text")
// console.log(allTexts)

// 2. Что такое NodeList и HTMLCollection
// NodeList -> это массив с индексами
// HTMLCollection -> Это обьект

// 3) Изменение содержииого элемента
// // 1. Поменять текст
// const title = document.getElementById("title")
// title.textContent = "Новый текст"

// 2. 
// const title = document.getElementById("title")
// title.innerHTML = "<div><b>ЭТО ИННЕР ХТМЛ<b></div>"
// innerText 

// 3.
// const photo = document.getElementById("photo")
// const link = document.getElementById("link")
// console.log(photo.getAttribute("src"))
// photo.setAttribute("src", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6TSSzUxOaw50amYcoLnBccLbIGwVl66y_CQ&s")
// photo.setAttribute("alt", "Pixel")

// console.log(link.getAttribute("href"))
// link.setAttribute("href", "https://pixelcom.kz/")
// link.textContent = "Pixel"

// 4.
// const text = document.getElementById("title")

// text.style.color = "red"
// text.style.fontSize = "25px"
// text.style.backgroundColor = "yellow"
// text.style.width = "200px"
// text.style.height = "50px"

// const herotext = document.querySelector(".subtitle")
// herotext.style.color = "orange"
// herotext.style.fontSize = "35px"
// herotext.style.backgroundColor = "blue"


// const allTexts = document.querySelectorAll(".text")
// allTexts.forEach(item => {
//     item.style.color="darkgreen"
// })


// const message = document.getElementById("message")
// const btn = document.getElementById("btn")

// btn.addEventListener("click", () => {
//     message.classList.add("active")
// })


// const title = document.getElementById("title")
// const changeBtn = document.getElementById("btn")

// changeBtn.addEventListener("click", () => {
//     title.textContent = "Новый текст"
// })

// const countEl = document.getElementById("count")
// const plusBtn = document.getElementById("plus")
// const minusBtn = document.getElementById("minus")

// let count = 0
// plusBtn.addEventListener("click", () =>{
//     count++
//     countEl.textContent = count
// })

// minusBtn.addEventListener("click", () =>{
//     count--
//     countEl.textContent = count
// })


// const password = document.getElementById("password")
// const toggle = document.getElementById("togglePass")
// toggle.addEventListener("click", () =>{
//     if(password.type == "password"){
//         password.type = "text"
//         toggle.textContent = "Скрыть"
//     }
//     else{
//         password.type = "password"
//         toggle.textContent = "Показать"
//     }
// })

const card = document.getElementById("card")
const red = document.getElementById("red")
red.addEventListener("click", () =>{
    card.style.backgroundColor = "red"
})
const green = document.getElementById("green")
green.addEventListener("click", () =>{
    card.style.backgroundColor = "green"
})
