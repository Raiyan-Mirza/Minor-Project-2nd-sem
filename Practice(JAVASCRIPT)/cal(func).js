function sum(x, y) {
    let sum = x + y;
    return (`The sum of the numbers are ${sum}.`);
}

function subtract(x, y) {
    let subtract = x - y;
    console.log(`The subtraction of the numbers are ${subtract}.`)
}

function multiply(x, y) {
    let multiply = x * y;
    console.log(`The multiplication of the numbers are ${multiply}.`);
}

function divide(x, y) {
    let divide = x / y;
    return (`The division of the numbers comes out to be ${divide}.`);
}

function isEven(x) {
    return x % 2 === 0 ? true : false;
}

console.log(sum(3, 19))
console.log(isEven(10))
console.log(isEven(101))
console.log(divide(18,2))