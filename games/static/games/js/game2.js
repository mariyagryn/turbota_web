var colorSequence = []; //array for storing the sequence of buttons to be pressed
var clickEnabled = true;
var level = 0;
var currentElement = 0;
var gameOver = false;

function gameStart() {
  currentElement = 0;
  level++;
  $("#level-title").text("Рівень " + level);
  var random = Math.floor(Math.random() * 4);
  clickEnabled = false;
  //this switch checks the random generated and every number has a tile assigned which is pushed to the colorSequence
  switch (random) {
    case 0:
      colorSequence.push("blue");
      animateButtons("blue");
      addSound("blue");
      break;
    case 1:
      colorSequence.push("green");
      animateButtons("green");
      addSound("green");
      break;
    case 2:
      colorSequence.push("red");
      animateButtons("red");
      addSound("red");
      break;
    case 3:
      colorSequence.push("yellow");
      animateButtons("yellow");
      addSound("yellow");
      break;
  }
}
//this function adds the sound according to the button which is the argument taken in
function addSound(btn) {
  var audio = new Audio("/static/games/sounds/game2/" + btn + ".mp3");
  audio.play();
}
//any key pressed will start the game
$("body").keydown(function() {
  if (clickEnabled === true) {
    gameStart();
  }
  if (gameOver === true) {
    colorSequence = [];
    clickEnabled = true;
    level = 0;
    currentElement = 0;
    gameOver = false;
    $("#level-title").text("Натисніть будь-яку клавішу, щоб почати");
    console.log(colorSequence);
  }
});
//adds the click event to all the four buttons
$(".btn").click(function(event) {
  if (this.id !== colorSequence[currentElement]) {
    addSound("wrong");
    clickEnabled = false;
    gameOver = true;
    $("body").addClass("game-over");
    $("#level-title").text(`Гру завершено на рівні ${level}. Натисніть будь-яку клавішу, щоб почати спочатку`);
    setTimeout(function() {
      $("body").removeClass("game-over");
    }, 100)
  } else if (this.id === colorSequence[currentElement]) {
    addSound(this.id);
    animateButtons(this.id);
    currentElement++;
    if (colorSequence.length === currentElement) {
      setTimeout(function() {
        gameStart();
      }, 1000);
    }
  }
});

//adds the pressed animation to the buttons
function animateButtons(color) {
  $("." + color).addClass("pressed");

  setTimeout(function() {
    $("." + color).removeClass("pressed");
  }, 100)
}