// alert("Hello")
// console.log("Hello from console")

// let a = 5
// const b = false
// let c = 6
// console.log(a, b)
// console.log(a + c)
// console.log(a - c)
// console.log(a * c)
// console.log(a / c)
// console.log(a % c)
// console.log(a ** c)

// a = Number(prompt("Сколько тебе лет?"))
// console.log(a)
// confirm("Ты ув ерен?")

// let x = 10
// x = "строка"
// const y = 10
// y = "строка"
// console.log(x)
// console.log(y)

// console.log("Валерий, 22 года")

// a = prompt("Как тебя зовут?")
// console.log("Привет, " + a)

// a = Number(prompt("Укажи число:"))
// b = Number(prompt("Укажи число:"))
// c = Number(prompt("Укажи число:"))
// console.log(a + b + c)

// let d = 10  
// d = "строка"
// console.log(d)

// let day = Number(prompt("Укажи день недели (1-7):"))
// if (day ==1){
//     console.log("Понедельник")
// }
// else if (day ==2){
//     console.log("Вторник")
// }
// else if (day ==3){
//     console.log("Среда")
// }
// else if (day ==4){
//     console.log("Четверг")
// }
// else if (day ==5){
//     console.log("Пятница")
// }
// else if (day ==6){
//     console.log("Суббота")
// }
// else if (day ==7){
//     console.log("Воскресенье")
// }


// let day = Number(prompt("Укажи день недели (1-7):"))
// switch (day) {
//     case 1:
//         console.log("Понедельник")
//         break
//     case 2:
//         console.log("Вторник")
//         break
//     case 3:
//         console.log("Среда")
//         break
//     case 4:
//         console.log("Четверг")
//         break
//     case 5:
//         console.log("Пятница")
//         break
//     case 6:
//         console.log("Суббота")
//         break
//     case 7:
//         console.log("Воскресенье")
//         break
//     default:
//         console.log("Ошибка")
// }

// let age = Number(prompt("Укажи свой возраст:"))
// age >= 18 ? console.log("Adult") : console.log("Kid")

// if (age>=18){
//     console.log("Взрослый")
// }
// else{
//     console.log("Малой")
// }
// a = Number(prompt("Введите число: "))
// if (a > 0){
//     console.log("положительное")
// }
// else if (a==0){
//     console.log("Ноль")
// }
// else if (a < 0){
//     console.log("Отрицательное")
// }

// b = Number(prompt("Введите число"))
// if (b%2==0 && b%4==0){
//     console.log("Четное и делится на 4")
// }
// else if (b%2 == 0){
//     console.log("Четное")
// }
// else if (b%2 != 0){
//     console.log("Нечетное")
// } 

// c = Number(prompt("Введи первое число: "))
// d = Number(prompt("Введи второе число: "))
// e = Number(prompt("Введи оператора(1 - +, 2 - -, 3 - *, 4 - /)"))
// switch (e){
//     case 1:
//         console.log(c+d)
//     break
//     case 2:
//         console.log(c-d)
//     break
//     case 3:
//         console.log(c*d)
//     break
//     case 4:
//         console.log(c/d)
//     break
//     default:
//     console.log("Ошибка")
// }

// a = Number(prompt("Введите число: "))
// b = Number(prompt("Введите число: "))
// if (a > b){
//     console.log("Первое число больше второго")
// }
// else if (a < b){
//     console.log("Второе число больше первого")
// }
// else{
//     console.log("Числа равны")
// }

a = Number(prompt("Введите число 1: "))
b = Number(prompt("Введите число 2: "))
c = Number(prompt("Введите число 3: "))

if (a>b && a>c){
    console.log("Первое число больше двух остальных")
}
else if (b>a && b>c){
    console.log("Второе число больше двух остальных")
}
else if (c>a && c>b){
    console.log("Третье число больше двух остальных")
}
else{
    console.log("Пусто")
}

// login = prompt("Введите логин: ")
// password = prompt("Введите пароль: ")