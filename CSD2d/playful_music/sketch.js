// by Paul Wienk

// TO DO:
// - filtering
// - multithreading
// - smoother adsr
// - button clicking

let currentColor = 0;
let currentThickness = 6;
let currentFreq = 396;
let mouseReleased = false;
let lengthLine = 0;

let drawingCanvasWidth = 1000;
let drawingCanvasHeight = 600;
let drawingCanvasStartX = 80;
let drawingCanvasStartY = 0;


const adsr = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

const filter = new Tone.Filter(350, "lowpass").toDestination();

const autoFilter = new Tone.AutoFilter("8n").toDestination().start();

const oscillator = new Tone.Oscillator(currentFreq, "sine")

oscillator.chain(adsr, filter, autoFilter, Tone.Destination);


function setup()
{
  createCanvas(1200, 600);
  background(30);

  fill(104);
  rect(drawingCanvasStartX, drawingCanvasStartY,
       drawingCanvasWidth, drawingCanvasHeight);

  // create clear button to clear the casnvas
  clearLines = createButton('Clear');
  clearLines.position(10, 500);
  clearLines.mousePressed(clearCanvas)

  smallThickness = createButton('Small');
  smallThickness.position(1100, 0);
  smallThickness.mousePressed(changeThicknessToSmall)

  mediumThickness = createButton('Medium');
  mediumThickness.position(1100, 50);
  mediumThickness.mousePressed(changeThicknessToMedium)

  largeThickness = createButton('Large');
  largeThickness.position(1100, 100);
  largeThickness.mousePressed(changeThicknessToLarge)

  blackButton = createButton('Black');
  blackButton.position(10, 0);
  blackButton.mousePressed(changeColorToBlack);

  blueButton = createButton('Blue');
  blueButton.position(10, 50);
  blueButton.mousePressed(changeColorToBlue);

  redButton = createButton('Red');
  redButton.position(10, 100);
  redButton.mousePressed(changeColorToRed);

  greenButton = createButton('Green');
  greenButton.position(10, 150);
  greenButton.mousePressed(changeColorToGreen);

  yellowButton = createButton('Yellow');
  yellowButton.position(10, 200);
  yellowButton.mousePressed(changeColorToYellow);

  whiteButton = createButton('White');
  whiteButton.position(10, 250);
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

  if ((mouseIsPressed === true) &&
      (mouseX > drawingCanvasStartX) &&
      (mouseX < drawingCanvasStartX + drawingCanvasWidth) &&
      (mouseY > drawingCanvasStartY) &&
      (mouseY < drawingCanvasStartY + drawingCanvasHeight))
  {
    line(mouseX, mouseY, pmouseX, pmouseY);
    lengthLine++;
  }

  if (mouseReleased === true)
  {
    var lengthLineMax = max(lengthLine) / 20;

    oscillator.start();

		oscillator.frequency.value = currentFreq;
		adsr.triggerAttackRelease(lengthLineMax);

    lengthLine = 0;
    mouseReleased = false;
    console.log("start release", lengthLineMax, currentFreq);
  }
}
