//SYNTAX for JS FUNCTIONS
// function name(parameter1, parameter2){
//   Code to be executed
// }
//alert("Hello")

//Example 1
function helloYou(name){
  console.log("hello world!"  +name);
}

//Example 2
function addNum(num1,num2){
  console.log(num1 + num2);
}

//Example 3
function helloSomeone(name=" Ram Bahadur"){
  console.log("Hello" +name);
}

//Example 4
function formal(name=" Sam", title ='Sir'){
  return title+ "" + name
}

//Example 5
function timesFive(numInput){
  //Local Scope to the function!
  var result = numInput * 5
  return result
}

//Example 6 Defining Global Scope
var v = "GLOBAL V"
var stuff ="GLOBAL STUFF"

function fun(stuff){
  console.log(v);
  stuff ="Reassign stuff inside func"
  console.log(stuff);
}

fun()
console.log(stuff);

//Write a JavaScript function that reverse a number
//Example x = 32243;
//Expected Output: 34223
function reverse_a_number(n){
  n = n + "";
  return n.split("").reverse().join("");
}
console.log(Number(reverse_a_number(32243)));

//Write a javascript function that checks whether a passed string is palindrom or not
function check_Palindrome(str_entry){
  //change the string into lower case and remove all non-alphanumeric character
  var cstr = str_entry.toLowerCase().replace(/[^a-zA-Z0-9]+/g,'');
  var ccount = 0;
  //check whether the string is empty or not
  if (cstr==="") {
    console.log("Nothing found!");
    return false;
  }
  //check if the length of the string is even or odd
  if ((cstr.length)%2 === 0) {
    ccount = (cstr.length)/2;
  }else {
    //If the length of the string is 1 then it becomes a palindrom
    if (cstr.length === 1) {
      console.log("Entry is a palindrome.");
      return true;
    }else{
      //If the length of the string is odd ignore middle character
      ccount = (cstr.length -1)/2;
    }
  }
  //Loop through to check the first character to the last character and then move next
  for (var x = 0; x < ccount; x++) {
    //Compare characters and drop them if they do not match
    if (cstr[x] != cstr.slice(-1-x)[0]) {
      console.log("Entry is not palndrome.");
      return false;
    }
  }
  console.log("The entry is a palindrome.");
  return true;
}
check_Palindrome('madam');
check_Palindrome('nursesrun');
check_Palindrome('fox');


//Check the square
function square(number){
  return number * number;
}

// EXERCISE
function myFunc(theObject){
  theObject.make = "Toyota";
}
const mycar = {
  make: "Honda",
  model: "Accord",
  year: 1998,
};
console.log(mycar.make);  //Honda
myFunc(mycar);
console.log(mycar.make);  //Toyota
