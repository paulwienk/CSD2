// template by Daniel Shiffman, adjusted by Paul Wienk

// locate CREPE pitch detection model url
const model_url = 'https://cdn.jsdelivr.net/gh/ml5js/ml5-data-and-models/models/pitch-detection/crepe/';

let pitch, mic;
let currentFrequency = 0.0;
let canvasWidth = 360;
let canvasHeigth = 640;
let goalLineDifference = 10;
let randomNote, goalNote, goalFrequency;

// define notes with their frequencies
let notes = [
  {
    note: 'A3',
    frequency: 220.0
  },
  {
    note: 'B3',
    frequency: 246.9
  },
  {
    note: 'C3',
    frequency: 130.8
  },
  {
    note: 'D3',
    frequency: 146.8
  },
  {
    note: 'E3',
    frequency: 164.8
  },
  {
    note: 'F3',
    frequency: 174.6
  },
  {
    note: 'G3',
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

  // picks a random object from the notes array
  randomNote = int(random(notes.length - 1));

  // takes the right note and frequency of that object
  goalNote = notes[randomNote].note
  goalFrequency = -notes[randomNote].frequency
}

function changeOctave()
{
  goalFrequency = -notes[randomNote].frequency * 2
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
  text(goalNote, width / 2, goalFrequency - 30)
}

function draw()
{
  background(130);

  // flips the coördinate system so coördinate 0 is in the lower left corner
  // therefore some drawing variables are negative
  translate(0, 640);

  // show the current frequency that is heard
  textAlign(CENTER, CENTER);
  fill(255);
  textSize(32);
  text(currentFrequency.toFixed(1), width / 2, height - 700);

  octaveShift = createButton('octave shift');
  octaveShift.position(0, 0);
  octaveShift.mousePressed(changeOctave);

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
