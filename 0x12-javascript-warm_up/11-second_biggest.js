#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let arr = process.argv.slice(2);
  arr.sort((a, b) => b - a);
  arr.forEach(element => {
    console.log(element);
  });
}
