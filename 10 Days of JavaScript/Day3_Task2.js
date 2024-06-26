// Name : Day 3: Try, Catch, and Finally
// Link : https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
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


function reverseString(s) {
    try{
        s = s.split('');
        s.reverse();
        s = s.join('');
        console.log(s);
    }
    catch (e){
        console.log(e.message);
        console.log(s);
    }
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}