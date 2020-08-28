// Name : Day 2: Loops
// Link : https://www.hackerrank.com/challenges/js10-loops/problem
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


function vowelsAndConsonants(s) {
    for(let i = 0;i<s.length;i++){
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u'){
            console.log(s[i])
        }
    }
    for(let i = 0;i<s.length;i++){
        if(s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u'){
            console.log(s[i])
        }
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}