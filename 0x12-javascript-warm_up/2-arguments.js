#!/usr/bin/node
const { argv } = require('node:process');
console.log('Length:', argv.length);
if (argv.length == 1) {
	console.log('No argument');
} else {
	console.log('Argument', argv.length == 2 ? 's' : '', 'found');
}
