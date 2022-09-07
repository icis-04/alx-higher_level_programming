#!/usr/bin/node
module.exports = class Rectangle {
constructor(w, h){
if (w > 0 && h > 0) {
this.width = w;
this.height = h;
}
};
print() {
let i = 0;
let j = 'X';
while (i < this.height) {
console.log(j.repeat(this.width));
i++;
}
}
rotate() {
let temp = this.width;
this.width = this.height;
this.height = temp
}
double() {
this.width = this.width * 2;
this.height = this.height * 2;
}
};
