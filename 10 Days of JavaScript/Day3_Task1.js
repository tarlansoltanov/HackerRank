// Name : Day 3: Arrays
// Link : https://www.hackerrank.com/challenges/js10-arrays/problem
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


function getSecondLargest(nums) {
    nums.sort((x, y) => x > y)
    var maxx = nums[nums.length-1];
    while(nums[nums.length-1]==maxx){
        nums.pop();
    }
    return nums[nums.length-1];
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}