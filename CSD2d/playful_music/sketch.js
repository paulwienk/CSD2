// by Paul Wienk

// TO DO:
// - filtering
// - multithreading
// - smoother adsr

let currentColor = 0;
let currentThickness = 6;
let currentFreq = 396;
let mouseReleased = false;
let lengthLine = 0;

let adsr = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 2.0
}).toMaster();

var oscillator = new Tone.Oscillator(currentFreq, "sine").connect(adsr).start();

function setup()
{
  createCanvas(1200, 600);
  background(104);

  // create clear button to clear the casnvas
  clearLines = createButton('Clear');
  clearLines.position(0, 500);
  clearLines.mousePressed(clearCanvas)

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

  blackButton = createButton('Black');
  blackButton.position(0, 0);
  blackButton.mousePressed(changeColorToBlack);

  blueButton = createButton('Blue');
  blueButton.position(0, 50);
  blueButton.mousePressed(changeColorToBlue);

  redButton = createButton('Red');
  redButton.position(0, 100);
  redButton.mousePressed(changeColorToRed);

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

function clearCanvas()
{
  clear();
  background(104);
}

function changeThicknessToSmall()
{
  currentThickness = 1;
}

function changeThicknessToMedium()
{
  currentThickness = 6;
}

function changeThicknessToLarge()
{
  currentThickness = 12;
}

function changeColorToBlack()
{
  currentColor = 0;
  currentFreq = 396;
}

function changeColorToBlue()
{
  currentColor = color(0, 0, 255);
  currentFreq = 417;
}

function changeColorToRed()
{
  currentColor = color(255, 0, 0);
  currentFreq = 528;
}

function changeColorToGreen()
{
  currentColor = color(0, 255, 0);
  currentFreq = 639;
}

function changeColorToYellow()
{
  currentColor = color(255, 255, 0);
  currentFreq = 741;
}

function changeColorToWhite()
{
  currentColor = 255;
  currentFreq = 852;
}

function mouseClicked()
{
  mouseReleased = true;
}

function draw()
{
  stroke(currentColor);
  strokeWeight(currentThickness);

  if (mouseIsPressed === true)
  {
    line(mouseX, mouseY, pmouseX, pmouseY);
    lengthLine++;
  }

  if (mouseReleased === true)
  {
    let lengthLineMax = max(lengthLine) / 20;

		oscillator.frequency.value = currentFreq;
		adsr.triggerAttackRelease(lengthLineMax);

    lengthLine = 0;
    mouseReleased = false;
    console.log("start release", lengthLineMax, currentFreq);
  }
}
