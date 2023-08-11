//Example 1
var myArr = ['one', 'Two', 'Three']
console.log(myArr);

//Example 2
var country1 = "USA"
var country2 = "Nepal"
var country3 = 'China'
console.log(country1, country2, country3);

//Example 3
var countries = ["USA", "Nepal", "India"]
console.log(countries);

//Example 4
var lastItem = countries.pop() //POP out the lastItem
console.log(lastItem);  //Displayed the lastItem
console.log(countries);  //Displayed the remaining array
countries.push("Spain")  //Pushed the newitem in the array
console.log(countries);  //Displayed the new array

//Example 5
console.log(countries[countries.length - 1]);  //Display the last items

//Example 6: Nest and Arrays
var matrix = [[1,2,3],[4,5,6],[7,8,9]]  //Nested Arrays
console.log(matrix);  //Now we can see an array inside of an array
console.log(matrix.length);


//Example 7: Array Iteration
var arr = ["A", "B", "C"]
console.log(arr);
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
//OR
for (letter of arr) {  //For of loop
  console.log(letter);
}

for(letter of arr){  //Alert each letter
  alert(letter);
}
//OR
arr.forEach(alert);

//Example

function addAwesome(name){
  //var addAwesome = prompt("name:");
  console.log(name+" is awesome!");  //Call addAwesome("Django") in your console
}

var topics = ["Python", "Django", "Science"]
topics.forEach(addAwesome)
