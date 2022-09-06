#!/usr/bin/node
// calculates factorial of a number
function factorial(a){
if (a == 0){
return 1;
}else{
return a * factorial(a - 1);
}
}
const process = require('process');
if (process.argv.length === 2){
console.log(1);
}else{
console.log(factorial(parseInt(process.argv[2])));
}
 
