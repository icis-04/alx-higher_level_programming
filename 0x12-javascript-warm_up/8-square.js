#!/usr/bin/node
// looping with arguments
const process = require('process');
const n = parseInt(process.argv[2]);
const m = Number.isInteger(n);
let i = 0;
let j = 'X';
if (m === false) {
  console.log('Missing size');
} else {
  while (i < n) {
    console.log(j.repeat(n));
    i++;
  }
}
