/*
Syntax for FOR Loop
for (statement1; statement2; statement3){
  Execute some code
}
Statement1 is executed before the loop(the code block) starts.

Statement2 defines the condition for running the loop.

Statement3 is executed each time after the loop cycles through.
Ex: for(var i = 0; i<5; i++){
  Execute some code
}
*/

//Example1: FOR LOOPS
for (var i = 0; i <= 5; i++) {
  console.log("Number is "+i);
}

//Example2: FOR LOOPS
var word = "ABCDEFGHIJK"
for (var i = 0; i < word.length; i++) {
  console.log(word[i]);
}

//Example3: FOR LOOPS
var word = "ABABABABAB"

for (var i = 0; i < word.length; i = i + 2) {
  console.log(word[i]);
}
