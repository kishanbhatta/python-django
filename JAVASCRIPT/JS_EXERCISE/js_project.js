//alert("Hello and Welcome. Please enter your first name:")
var fName = prompt("Hello and Welcome. Please enter your first name:")
var lName = prompt("Please enter your Last Name:")
var age = prompt("How old are you?")
var height = prompt("How tall are you in centimters?")
var petName = prompt("What is the name of your pet")
alert("Thank You so much for the information.")

//Four conditions
var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;

//Name conditions
if (fName[0] === lName[0]) {
  nameCond = true;
}else {
  nameCond = false;
}

//Age conditions
if (age > 20 && age < 30) {
  ageCond = true;
}else {
  ageCond = false;
}

//Height conditions
if (height >= 170) {
  heightCond = true;
}else {
  heightCond = false;
}

//PET conditions
if (petName[petName.length - 1] === "y") {
  petCond = true;
}else {
  petCond = false;
}

//CHECK ALL conditions
if (nameCond && ageCond && heightCond && petCond) {
  console.log("Welcome Comrade! You've passed the Spy Test.");
}else {
  console.log("Sorry, nothing to see here.");
}


// Jose Johnson
// 26 years old
// 175 cm tall
// Pet name is "Sammy"
