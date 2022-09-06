#!/usr/bin/node
// looping with arguments
const process = require('process');
let n = parseInt(process.argv[2]);
let m = Number.isInteger(n);
let i = 0;
if (m === false){
console.log('Missing size');
}else{
while(i < n){
j = 0
while(j < n){
console.log('X');
j++;
}
i++;
}
}
