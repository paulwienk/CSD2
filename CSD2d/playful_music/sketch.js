//create a synth and connect it to the main output (your speakers)
const synth = new Tone.Synth().toDestination();

let currentColor = 255;
let currentThickness = 6;

function setup() {
  createCanvas(1200, 600);
  background(104);

  // create buttons for thickness of the line
  smallThickness = createButton('Small');
  smallThickness.position(1135, 0);
  smallThickness.mousePressed(changeThicknessToSmall)

  mediumThickness = createButton('Medium');
  mediumThickness.position(1135, 50);
  mediumThickness.mousePressed(changeThicknessToMedium)

  largeThickness = createButton('Large');
  largeThickness.position(1135, 100);
  largeThickness.mousePressed(changeThicknessToLarge)

  // create buttons to change the color of the line
  blackButton = createButton('Black');
  blackButton.position(0, 0);
  blackButton.mousePressed(changeColorToBlack);

  redButton = createButton('Red');
  redButton.position(0, 50);
  redButton.mousePressed(changeColorToRed);

  blueButton = createButton('Blue');
  blueButton.position(0, 100);
  blueButton.mousePressed(changeColorToBlue);

  greenButton = createButton('Green');
  greenButton.position(0, 150);
  greenButton.mousePressed(changeColorToGreen);

  yellowButton = createButton('Yellow');
  yellowButton.position(0, 200);
  yellowButton.mousePressed(changeColorToYellow);

  whiteButton = createButton('White');
  whiteButton.position(0, 250);
  whiteButton.mousePressed(changeColorToWhite);
}

// functions to change the thickness
function changeThicknessToSmall() {
  currentThickness = 1;
}

function changeThicknessToMedium() {
  currentThickness = 6;
}

function changeThicknessToLarge() {
  currentThickness = 12;
}

// functions to change the colors
function changeColorToBlack() {
  currentColor = 0;
}

function changeColorToRed() {
  currentColor = color(255, 0, 0);
}

function changeColorToBlue() {
  currentColor = color(0, 0, 255);
}

function changeColorToGreen() {
  currentColor = color(0, 255, 0);
}

function changeColorToYellow() {
  currentColor = color(255, 255, 0);
}

function changeColorToWhite() {
  currentColor = 255;
}


function draw() {
  stroke(currentColor);
  strokeWeight(currentThickness);

  if (mouseIsPressed === true) {
    line(mouseX, mouseY, pmouseX, pmouseY);
    console.log(mouseX);

    const now = Tone.now();
    synth.triggerAttack(mouseX, now);

    // wait one second before triggering the release
    synth.triggerRelease(now + 0.0001);
  }

}
