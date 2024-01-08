#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.forEach(element => {
    console.log(element);
  });
}
