// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(){
  var newName = prompt("Enter the Name you want to add.")
  roster.push(newName)
}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(){
  var remName = prompt("What name you want to remove?")
  var index = roster.indexOf(remName);
  roster.splice(index,1)
}



// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var start = prompt("Would you like to start the roster web app> Y/N")
var request = "empty";
if (start === 'y' || "Y") {
  while (request !== "quit") {
    request = prompt("Please select an action: add, remove, display, or quit.")
    if (request === 'add') {
      addNew();
    }else if (request === 'display') {
      display();
    }else if (request === 'remove') {
      remove();
    }else {
      //alert("Not recognized")
      request = 'quit';
    }
  }
}
alert("Thanks for using the Web App! Please refresh to stat over")
