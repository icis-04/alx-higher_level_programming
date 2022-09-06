#!/usr/bin/node
// checks if arguments are passed or not 
const process = require('process');
if (process.argv.length === 2){
console.log('No argument');
}else{
console.log('Argument found');
}
