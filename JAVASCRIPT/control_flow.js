/* Syntax for the IF ELSE statement in js
if (condition) {
  Execute some code
}
else {
  Execute some other code
}
*/

/*
Syntax for IF, ELSE IF, ELSE statement
if (condition one) {
  Execute some code
}
else if (condition two) {
  Execute some other code
}
else {
Execute some backup code
}
*/
        // var hot = false;
        // var temp = 50;
        //
        // if (temp > 80) {
        //   console.log("Hot Outside!");
        // }else if (temp <= 80 && temp >= 50) {
        //   console.log("Average temp Outside");
        // }else if (temp <50 && temp >= 32) {
        //   console.log("Its pretty cold out!!!");
        // }else {
        //   console.log("It is very cold out");
        // }

var vegKhana = 50;
var chiKhana = 50;

var report = "blank"

if (vegKhana >= 50 && chiKhana >= 50) {
  report = "Strong sales of both vegKhana and chiKhana!"
}else if (vegKhana === 0 && chiKhana === 0) {
  report = "Nothing Sold!"
}else {
  report = "We had some sales of items."
}
console.log(report);
