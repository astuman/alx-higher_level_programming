#!/user/bin/node
// print addition of two integers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(process.argv[2], process.argv[3]));
