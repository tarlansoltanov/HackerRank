// Name : Day 0: Data Types
// Link : https://www.hackerrank.com/challenges/js10-data-types/problem
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

function performOperation(secondInteger, secondDecimal, secondString) {
    const firstInteger = 4;
    const integer = firstInteger + parseInt(secondInteger);

    const firstDecimal = 4.0;
    const decimal = firstDecimal + parseFloat(secondDecimal);

    const firstString = 'HackerRank ';
    const string = firstString + secondString;

    console.log(integer);

    console.log(decimal);

    console.log(string);
}