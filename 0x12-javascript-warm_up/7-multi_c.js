#!/usr/bin/node
// prints C is fun 'x' times
const lang = 'C is fun';
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= parseInt(x); i++) {
    console.log(lang);
  }
}
