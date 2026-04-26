// function sayHello(){
//     console.log("hello")
// }

// sayHello()

// function greet(name){
//     console.log(`Привет ${name}`)
// }

// greet("Alex")
// greet("John")
// greet("Edward")

// function sum(a,b){
//     return a+b
// }
// let numbers1 = sum(1,1)
// console.log(sum(4,5))
// console.log(sum(1,2))
// console.log(sum(3,3))
// console.log(numbers1)

// function multiply(a,b){
//     return a*b
// }
// console.log(multiply(4,5))
// console.log(multiply(7,8))

// function checkAge(age){
//     if(age >= 18){
//         console.log("Доступ разрешен")
//     }
//     else{
//         console.log("Доступ запрещен")
//     }
// }

// checkAge(20)
// checkAge(15)

// function shout (word){
//     console.log(word.toUpperCase())
// }
// shout("hello")
// shout("javascript")


// function shout (word){
//     console.log(word.toLowerCase())
// }
// shout("hello")
// shout("javascript")

// function getDiscount(price){
//     return price * 0.9
// }
// let newPrice = getDiscount(1000)
// console.log("цена со скидкой " + newPrice)

// function getUpper(num){
//     if(num < 5){
//         console.log("Да, твое число больше 5")
//     }
//     else{
//         return
//     }
// }
// getUpper(6)
// getUpper(2)

// // Удвоить число
// function getDouble(num){
//     return num*2
// }
// console.log(getDouble(5))

// // Найти квадрат числа
// function getSquare(num){
//     return num*num
// }
// console.log(getSquare(5))

// // Найти сумму двух чисел
// function getSum(a,b){
//     return a+b
// }
// console.log(getSum(3,5))

// // Найти разницу
// function getMinus(a,b){
//     return a-b
// }
// console.log(getMinus(10,7))

// // проверка на четность
// function getChet(num){
//     if(num%2==0)
//         console.log("Четное")
//     else(
//         console.log("Нечетное")
//     )
// }
// getChet(5)
// getChet(4)


// function square(num){
//     return num*num
// }
// const square2 = (num) =>{
//     return num*num
// }
// const square3 = (num) => num*num

// const add = (a,b) =>{
//     return a+b
// }
// const add2 = (a,b) => a + b

// const isEven = num => num%2 === 0

// const isAdult = age => age >= 18

// const getLength = text => text.length
// console.log(getLength("Javascript"))

// const getDiscount = price => price*0.7


// console.log(getDiscount(5000))

// console.log(isAdult(19))
// console.log(isAdult(16))

// console.log(isEven(6))
// console.log(isEven(9))

// console.log(add(1,2))
// console.log(add2(2,2))

// const toUpperCase = text => text.toUpperCase()
// console.log(toUpperCase("javascript"))

// const applyDiscount = price => price*0.9
// console.log(applyDiscount(3000))

// const getMax = (a , b) =>{
//     if (a >b)
//         return a
//     else if (b>a)
//         return b
//     else
//         return
// }
// console.log(getMax(9,6))
// console.log(getMax(7,10))

// const isAdult = age =>{
//     if (age>=18)
//         return("Adult")
//     else
//         return("Kid")
// }
// console.log(isAdult(16))
// console.log(isAdult(18))

// const getDouble = num => num*2
// console.log(getDouble(12))

// let numbers = [10, 20, 30, 40, 50, 60]
// numbers.push(70)
// numbers.pop()  
// numbers.unshift(0)
// numbers.shift()
// console.log(numbers.includes(100))
// console.log(numbers.indexOf(60))
// console.log(numbers.slice(1,3))

// for(let i = 0; i < numbers.length; i++){
//     console.log(i, numbers[i])
// }

// let words = ["Я", "Учу", "Javascript"]
// let a = words.join(" ")
// console.log(a)

// map -> Создать новый массив

// let nums = [1,2,3,4]
// let doubled = nums.map(num => num*2)

// console.log(doubled)

// filter -> оставить только подходящие элементы

// let nums = [1,2,3,4,5,6,7,8]
// let evenNums = []
// for(let i = 0; i<nums.length; i++){
//     if(nums[i] % 2 === 0){
//         evenNums.push(nums[i])
//     }
// }
// console.log(evenNums)


// let nums = [1,2,3,4,5,6,7,8]
// let evenNums = nums.filter(num => num%2 === 0)
// console.log(evenNums)

// let result = nums.find(num => num>4)
// console.log(result)

// let fruits = ["🍓", "🍐", "🥑"]
// fruits.forEach(fruit => {
//     console.log("Фрукт: ", fruit)
// })

