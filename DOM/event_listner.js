var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

// Hover functionality
headOne.addEventListener('mouseover', function(){
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout', function(){
  headOne.textContent = "HOVER OVER ME!";
  headOne.style.color = "black";
})

// Click functionality
headTwo.addEventListener("click",function(){
    headTwo.textContent = 'CLICKED ON!';
    headTwo.style.color = 'blue';
})
//
// headTwo.addEventListener("click", second);
//   function second(){
//     headTwo.testContent = "CLICK ME!";
//     headTwo.style.color = 'black';
// })


//Double Click Functionali
headThree.addEventListener("dblclick", function(){
  headThree.textContent= "I was double clicked!";
  headThree.style.color = 'red'
})







// To test the connection between html and js file
// console.log("CONNECTED!");
