#!/usr/bin/node
// looping with arguments
const process = require('process');
let n = parseInt(process.argv[2]);
let m = Number.isInteger(n);
if (m === false){
console.log('Missing size');
}else{
for (let i = 0; i < n; i++){
for (let j = 0; j < n; j++){
console.log('X\n'); 
}
}
}
