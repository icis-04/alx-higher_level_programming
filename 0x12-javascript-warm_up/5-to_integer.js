#!/usr/bin/node
// check if the first argument passed is a number
const process = require('process');
if (Number.isInteger(parseInt(process.argv[2])) === false) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
