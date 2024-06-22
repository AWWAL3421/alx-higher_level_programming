#!/usr/bin/node
// Prints a message depending on the number of arguments passed
let message;

if (process.argv.length === 2) {
  message = 'No argument';
} else if (process.argv.length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
