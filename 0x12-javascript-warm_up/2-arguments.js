#!/usr/bin/node

const args = process.argv;
const len = args.length;
if (len < 3) {
  console.log('no Arguments');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
