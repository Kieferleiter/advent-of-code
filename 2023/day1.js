
const fs = require('fs');
const input = fs.readFileSync('input');

const lines = input.toString().split('\n');

let sum = 0

function convertToNumber(input) {
    if(input.endsWith('one')){
      return 1;
    }
    else if(input.endsWith('two')){
      return 2;
    }
    else if(input.endsWith('three')){
      return 3;
    }
    else if(input.endsWith('four')){
      return 4;
    }
    else if(input.endsWith('five')){
      return 5
    }
    else if(input.endsWith('six')){
      return 6
    }
    else if(input.endsWith('seven')){
      return 7
    }
    else if(input.endsWith('eight')){
      return 8
    }
    else if(input.endsWith('nine')){
      return 9
    }
    else{
      return null;
    }
}

for (const line of lines) {
  let first = null;
  let last = null;

  let str = '';

  for (const char of line) {
    let num = null;

    if (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(char)) {
      num = Number(char);
    }
    else {
      str += char;
      num = convertToNumber(str);
    }
    
    if (num) {
      if (!first) {
        first = num;
      }
      last = num;
    }
  }

  const val = Number(`${first}${last}`);
  console.log(line);
  console.log(val);
  if (!isNaN(val)) {
    sum += val
  }
}

console.log(sum);