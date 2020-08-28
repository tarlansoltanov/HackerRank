// Name : Day 1: Let and Const
// Link : https://www.hackerrank.com/challenges/js10-let-and-const/problem
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

function main() {

    var radius = readLine();

    console.log(Math.PI * radius * radius);

    console.log(Math.PI * radius * 2);
    try {

        PI = 0;

        console.log(PI);
    } catch (error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}