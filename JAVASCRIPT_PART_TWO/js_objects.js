// JS Object is in the form:
// {key1: "value one", key2: "value two", ...}

//Example 1 JAVASCRIPT OBJECT
//var carInfo = {make:"Hyundai", year:2021, model:"Creta"};
// console.log[carInfo];

// var carInfo = {
//   make: "Hyundai",
//   year: 2022,
//   model: "Creta",
//   carAlert: function(){
//     alert("We've got a car here!")
//   }
// };

var myObj = {
  prop: 37,
  reportProp: function(){
    return this.prop;
  }
};
console.log(myObj.reportProp());

//Exammple
var simple = {
    prop: "hello",
    myMethod: function(){
        console.log("The myMethod was called")
    }
}
