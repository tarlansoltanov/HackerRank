// Name : Day 9: Binary Calculator
// Link : https://www.hackerrank.com/challenges/js10-binary-calculator
// Difficulty : Medium
// Programming language : JavaScript + CSS + HTML

var btn0 = document.getElementById("btn0");
var btn1 = document.getElementById("btn1");
var btnClr = document.getElementById("btnClr");
var btnEql = document.getElementById("btnEql");
var btnSum = document.getElementById("btnSum");
var btnSub = document.getElementById("btnSub");
var btnMul = document.getElementById("btnMul");
var btnDiv = document.getElementById("btnDiv");

let elem = document.getElementById("res");

function checkOperator() {
    if (elem.innerHTML.endsWith('+') || elem.innerHTML.endsWith('-') || elem.innerHTML.endsWith('*') || elem.innerHTML.endsWith('/')) {
        return true;
    }
}

btn0.addEventListener('click', function () {
    elem.innerHTML += '0';
})

btn1.addEventListener("click", function () {
    elem.innerHTML += '1';
})

btnSum.addEventListener("click", function () {
    if (elem.innerHTML.length != 0 && !checkOperator()) {
        elem.innerHTML += '+';
    }
})

btnSub.addEventListener("click", function () {
    if (elem.innerHTML.length != 0 && !checkOperator()) {
        elem.innerHTML += '-';
    }
})

btnMul.addEventListener("click", function () {
    if (elem.innerHTML.length != 0 && !checkOperator()) {
        elem.innerHTML += "*";
    }
})

btnDiv.addEventListener("click", function () {
    if (elem.innerHTML.length != 0 && !checkOperator()) {
        elem.innerHTML += "/";
    }
})

btnClr.addEventListener("click", function () {
    elem.innerHTML = '';
})

btnEql.addEventListener("click", function () {
    if (!checkOperator()) {
        let re = /\d+/g
        let re2 = /[\+\-\*\/]+/g
        let numbers = elem.innerHTML.match(re);
        let operations = elem.innerHTML.match(re2);
        while (operations.length > 0) {
            if (operations.includes('*')) {
                let indexOfMul = operations.indexOf('*');
                let mul = (indexOfMul != 0 ? parseInt(numbers[indexOfMul - 1], 2) : parseInt(numbers[indexOfMul], 2)) * parseInt(numbers[indexOfMul + 1], 2);
                numbers.splice(indexOfMul, 2);
                numbers.splice(indexOfMul, 0, mul.toString(2));
                operations.splice(indexOfMul, 1);
            } else if (operations.includes('/')) {
                let indexOfDiv = operations.indexOf('/');
                let division = (indexOfDiv != 0 ? parseInt(numbers[indexOfDiv - 1], 2) : parseInt(numbers[indexOfDiv], 2)) / parseInt(numbers[indexOfDiv + 1], 2);
                numbers.splice(indexOfDiv, 2);
                numbers.splice(indexOfDiv, 0, division.toString(2));
                operations.splice(indexOfDiv, 1);
            } else if (operations.includes('+')) {
                let indexOfSum = operations.indexOf('+');
                let sum = (indexOfSum != 0 ? parseInt(numbers[indexOfSum - 1], 2) : parseInt(numbers[indexOfSum], 2)) + parseInt(numbers[indexOfSum + 1], 2);
                numbers.splice(indexOfSum, 2);
                numbers.splice(indexOfSum, 0, sum.toString(2));
                operations.splice(indexOfSum, 1);
            } else {
                let indexOfSub = operations.indexOf('-');
                let sub = (indexOfSub != 0 ? parseInt(numbers[indexOfSub - 1], 2) : parseInt(numbers[indexOfSub], 2)) - parseInt(numbers[indexOfSub + 1], 2);
                numbers.splice(indexOfSub, 2);
                numbers.splice(indexOfSub, 0, sub.toString(2));
                operations.splice(indexOfSub, 1);
            }
        }
        elem.innerHTML = numbers[0].toString(2);
    } else {
        alert("Line must ends with number.")
    }
})