$('h1').click(function(){
  $(this).text("I was changed on a click!")
})

$('li').click(function(){
  console.log('Any li was clicked');
})

//KEY PRESS
$('input').eq(0).keypress(function(event){
if (event.which === 13){  //13 is the keyboard identity number for the Enter
  $('h3').toggleClass('turnBlue');  //toggle class on and off each time user press Enter button on key.
}

  //$('h3').toggleClass('turnBlue'); //toggle class on and off
})


//On() Method
$('h1').on('dblclick', function(){
  $(this).toggleClass('turnBlue');
})

//when mouse comes to that tag
$('h1').on('mouseenter', function(){
  $(this).toggleClass('turnBlue')
})

//Alimation and effect
//Fade away container class content in 3000 millisecond
$('input').eq(1).on('click', function(){
  $('.container').fadeOut(3000);
})

//Slide up all the container class in 3000 millisecond
$('input').eq(1).on('click', function(){
  $('.container').slideUp(3000);
})
