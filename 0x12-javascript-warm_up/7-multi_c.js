#!/usr/bin/node
// looping with arguments
const process = require('process');
const n = parseInt(process.argv[2]);
const m = Number.isInteger(n);
if (m === false) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
