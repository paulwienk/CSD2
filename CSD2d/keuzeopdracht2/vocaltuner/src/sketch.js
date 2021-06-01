// template by Daniel Shiffman, adjusted by Paul Wienk

// locate CREPE pitch detection model url
const model_url = 'https://cdn.jsdelivr.net/gh/ml5js/ml5-data-and-models/models/pitch-detection/crepe/';

let pitch, mic, randomNote, goalNote, goalFrequency;
let currentFrequency = 0.0;
let canvasWidth = 360;
let canvasHeigth = 640;
let goalLineDifference = 10;
let currentOctave = 3;

// define notes with their frequencies
let notes = [
  {
    note: 'A',
    frequency: 220.0
  },
  {
    note: 'B',
    frequency: 246.9
  },
  {
    note: 'C',
    frequency: 130.8
  },
  {
    note: 'D',
    frequency: 146.8
  },
  {
    note: 'E',
    frequency: 164.8
  },
  {
    note: 'F',
    frequency: 174.6
  },
  {
    note: 'G',
    frequency: 196.0
  },
];

function setup()
{
  createCanvas(canvasWidth, canvasHeigth);

  // setting up the mic
  audioContext = getAudioContext();
  mic = new p5.AudioIn();
  mic.start(detectPitch);

  octaveShiftUp = createButton('octave shift up');
  octaveShiftUp.position(5, 0);
  octaveShiftUp.mousePressed(shiftOctaveUp);

  octaveShiftDown = createButton('octave shift down');
  octaveShiftDown.position(233, 0);
  octaveShiftDown.mousePressed(shiftOctaveDown);

  // picks a random object from the notes array
  randomNote = int(random(notes.length - 1));

  // takes the right note and frequency of that object
  goalNote = notes[randomNote].note
  goalFrequency = -notes[randomNote].frequency
}

// shift octave one up
function shiftOctaveUp()
{
  goalFrequency = goalFrequency * 2
  currentOctave = currentOctave + 1;
}

// shift octave one down
function shiftOctaveDown()
{
  goalFrequency = goalFrequency / 2
  currentOctave = currentOctave - 1;
}

// detects the pitch based on the CREPE model
function detectPitch()
{
  console.log('listening...');
  pitch = ml5.pitchDetection(model_url, audioContext, mic.stream, modelLoaded);
}

// define the goal line
function createGoalLine()
{
  line(0, goalFrequency + goalLineDifference, canvasWidth, goalFrequency + goalLineDifference)
  line(0, goalFrequency - goalLineDifference, canvasWidth, goalFrequency - goalLineDifference)
  text(goalNote, width / 2.15, goalFrequency - 30)
  text(currentOctave, width / 1.85, goalFrequency - 30 )
}

function draw()
{
  background(130);

  // flips the coördinate system so coördinate 0 is in the lower left corner
  // therefore some values of drawing variables are negative
  translate(0, 640);

  // show the current frequency that is heard
  textAlign(CENTER, CENTER);
  fill(255);
  textSize(32);
  text(currentFrequency.toFixed(1), width / 2, -30);

  // draw the line of the current frequency that is heard
  stroke(0);
  line(0, -currentFrequency, canvasWidth, -currentFrequency);

  // draw the goal line
  stroke(255);
  createGoalLine();
}

// loads the CREPE pitch detection model
function modelLoaded()
{
  console.log('model loaded');
  pitch.getPitch(gotPitch);
}

// gets the right pitch from the model
function gotPitch(error, frequency)
{
  if (error)
  {
    console.error(error);
  }

  else
  {

    if (frequency)
    {
      currentFrequency = frequency;
    }

    pitch.getPitch(gotPitch);
  }
}
