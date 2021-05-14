// by Paul Wienk

// TO DO:
// - filtering
// - smoother adsr

let currentColor = "black";
let currentLineColor = 0;
let currentLineThickness = 6;
let mouseReleased = false;
let lengthLine = 0;

let drawingCanvasWidth = 1000;
let drawingCanvasHeight = 600;
let drawingCanvasTopLeftX = 80;
let drawingCanvasTopLeftY = 0;

const adsrBlack = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 1.0,
"sustain": 1.0,
"release": 10.0
}).toDestination();

const adsrBlue = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

const adsrRed = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

const adsrGreen = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

const adsrYellow = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

const adsrWhite = new Tone.AmplitudeEnvelope({
"attack": 2.0,
"decay": 0.2,
"sustain": 0.8,
"release": 10.0
}).toDestination();

// effect constructors
const reverb = new Tone.Reverb().toMaster();
const panner = new Tone.Panner().toMaster();
const autoPanner = new Tone.AutoPanner().toMaster();
const autoFilter = new Tone.AutoFilter().toMaster();
const volume = new Tone.Volume(-20).toMaster();

// oscillator constructors
const oscillatorBlack = new Tone.Oscillator(396, "sine");
const oscillatorBlue = new Tone.Oscillator(417, "sine");
const oscillatorRed = new Tone.Oscillator(528, "sine");
const oscillatorGreen = new Tone.Oscillator(639, "sine");
const oscillatorYellow = new Tone.Oscillator(741, "sine");
const oscillatorWhite = new Tone.Oscillator(852, "sine");

// effect routing
oscillatorBlack.chain(adsrBlack, autoPanner, autoFilter, Tone.Master);
oscillatorBlue.chain(adsrBlue, autoPanner, autoFilter, Tone.Master);
oscillatorRed.chain(adsrRed, autoPanner, autoFilter, Tone.Master);
oscillatorGreen.chain(adsrGreen, autoPanner, autoFilter, Tone.Master);
oscillatorYellow.chain(adsrYellow, autoPanner, autoFilter, Tone.Master);
oscillatorWhite.chain(adsrWhite, autoPanner, autoFilter, Tone.Master);


function setup()
{
  createCanvas(1200, 600);
  background(30);

  // drawing canvas
  fill(104);
  rect(drawingCanvasTopLeftX, drawingCanvasTopLeftY,
       drawingCanvasWidth, drawingCanvasHeight);

  // create clear button to clear the canvas
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
  background(30);
  fill(104);
  rect(drawingCanvasTopLeftX, drawingCanvasTopLeftY,
       drawingCanvasWidth, drawingCanvasHeight);
}

function changeThicknessToSmall()
{
  currentLineThickness = 1;
}

function changeThicknessToMedium()
{
  currentLineThickness = 6;
}

function changeThicknessToLarge()
{
  currentLineThickness = 12;
}

function changeColorToBlack()
{
  currentLineColor = 0;
  currentColor = "black";
}

function changeColorToBlue()
{
  currentLineColor = color(0, 0, 255);
  currentColor = "blue";
}

function changeColorToRed()
{
  currentLineColor = color(255, 0, 0);
  currentColor = "red";
}

function changeColorToGreen()
{
  currentLineColor = color(0, 255, 0);
  currentColor = "green";
}

function changeColorToYellow()
{
  currentLineColor = color(255, 255, 0);
  currentColor = "yellow";
}

function changeColorToWhite()
{
  currentLineColor = 255;
  currentColor = "white";
}

function mouseClicked()
{
  mouseReleased = true;
}

function draw()
{
  stroke(currentLineColor);
  strokeWeight(currentLineThickness);

  let xValue = mouseX / 80;
  let yValue = mouseY / 80;
  let randomAutoFilterFrequency = random(1.0, 10.0);
  let randomAutoPannerFrequency = random(1.0, 10.0);
  let randomDecay = random(1.0, 10.0)

  if ((mouseIsPressed === true) &&
      (mouseX > drawingCanvasTopLeftX) &&
      (mouseX < drawingCanvasTopLeftX + drawingCanvasWidth) &&
      (mouseY > drawingCanvasTopLeftY) &&
      (mouseY < drawingCanvasTopLeftY + drawingCanvasHeight))
  {
    line(mouseX, mouseY, pmouseX, pmouseY);
    lengthLine++;
  }

  if ((mouseReleased === true) &&
      (mouseX > drawingCanvasTopLeftX) &&
      (mouseX < drawingCanvasTopLeftX + drawingCanvasWidth) &&
      (mouseY > drawingCanvasTopLeftY) &&
      (mouseY < drawingCanvasTopLeftY + drawingCanvasHeight))
  {
    // lengthLineMax takes the highest value of lengthLine, which is the time in
    // seconds of the duration the mouse is pressed to draw te line
    let lengthLineMax = max(lengthLine) / 20;

    reverb.wet = 1;
    reverb.decay = randomDecay;

    autoFilter.frequency.value = randomAutoFilterFrequency;
    autoFilter.start();

    autoPanner.frequency.value = randomAutoPannerFrequency;
    autoPanner.start();

    if (currentColor === "black")
    {
    oscillatorBlack.start();
    adsrBlack.triggerAttackRelease(lengthLineMax);
    }

    if (currentColor === "blue")
    {
    oscillatorBlue.start();
    adsrBlue.triggerAttackRelease(lengthLineMax);
    }

    if (currentColor === "red")
    {
    oscillatorRed.start();
    adsrRed.triggerAttackRelease(lengthLineMax);
    }

    if (currentColor === "green")
    {
    oscillatorGreen.start();
    adsrGreen.triggerAttackRelease(lengthLineMax);
    }

    if (currentColor === "yellow")
    {
    oscillatorYellow.start();
    adsrYellow.triggerAttackRelease(lengthLineMax);
    }

    if (currentColor === "white")
    {
    oscillatorWhite.start();
    adsrWhite.triggerAttackRelease(lengthLineMax);
    }

    lengthLine = 0;
    mouseReleased = false;
    console.log("start release", lengthLineMax);
  }
}
