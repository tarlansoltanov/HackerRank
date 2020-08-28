// Name : Day 1: Arithmetic Operators
// Link : https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem
// Difficulty : Easy
// Programming language : JavaScript

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getArea(length, width) {
    let area;
    area = length * width

    return area;
}


function getPerimeter(length, width) {
    let perimeter;
    perimeter = length + width

    return perimeter * 2;
}