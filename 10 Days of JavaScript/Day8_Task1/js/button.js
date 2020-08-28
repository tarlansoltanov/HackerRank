// Name : Day 8: Create a Button
// Link : https://www.hackerrank.com/challenges/js10-create-a-button
// Difficulty : Easy
// Programming language : JavaScript + CSS + HTML

var btn = document.createElement("Button");

btn.innerHTML = "0";
btn.id = "btn";
btn.style.width = "96px";
btn.style.height = "48px";
btn.style.font-size = "24px";
document.body.appendChild(btn);

btn.onclick = function () {
    btn.innerHTML++;
}