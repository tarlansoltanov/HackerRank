// Name : Day 2: Conditional Statements: If-Else
// Link : https://www.hackerrank.com/challenges/js10-if-else/problem
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

function getGrade(score) {
    let grade = 'F';
    if (score > 25) {
        grade = 'A'
    } else if (score > 20) {
        grade = 'B'
    } else if (score > 15) {
        grade = 'C'
    } else if (score > 10) {
        grade = 'D'
    } else if (score > 5) {
        grade = 'E'
    }
    return grade;
}


function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}