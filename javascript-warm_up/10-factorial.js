#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(number));
