// Name : Day 4: Classes
// Link : https://www.hackerrank.com/challenges/js10-class/problem
// Difficulty : Easy
// Programming language : JavaScript

function Polygon(arr){
    this.perimeter = function() {
        perimeter = 0;
        for(var i = 0; i < arr.length; i++){
            perimeter+=arr[i];
        }
        return perimeter;
    };
    
}


const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());