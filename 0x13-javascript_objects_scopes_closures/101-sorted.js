#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (!newDict[key]) {
    newDict[key] = [value];
  } else {
    newDict[key].push(value);
	newDict[key].sort();
  }
});
console.log(newDict);