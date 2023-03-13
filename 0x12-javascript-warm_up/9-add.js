#!/usr/bin/node
function add(a,b) {
	return Math.floor(Number(a)) + Math.floor(Number(b));
}
console.log(add(process.argv[2], process.argv[3]));
