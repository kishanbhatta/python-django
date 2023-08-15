//Restart Game button
var restart = document.querySelector("#b");

//Grabs all the square
var squares = document.querySelectorAll('td');

//Clear all the square
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}
restart.addEventListener('click', clearBoard);
// Check the Square marker

// You can repeat this code for the each table cell for the nine time,
//but which violet the coding principle of DRY("Don't Repeat Yourself")
/*
var cellOne = document.querySelector('#one')
cellOne.addEventListener('click', function(){
  //cellOne.textContent = 'X';
  if (cellOne.textContent === '') {
    cellOne.textContent = 'X';
  }else if (cellOne.textContent === 'X') {
    cellOne.textContent = 'O';
  }else {
    cellOne.textContent = '';
  }
});
*/
// Alternative for the above repetative code

function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
}

//For Loop to add event Listeners to all squares
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click', changeMarker)
}
