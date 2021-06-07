// template by Daniel Shiffman, adjusted by Paul Wienk

// locate CREPE pitch detection model url
const model_url = 'https://cdn.jsdelivr.net/gh/ml5js/ml5-data-and-models/models/pitch-detection/crepe/';

let pitch, mic, randomNote, goalNote, goalFrequency;
let currentFrequency = 0.0;
let canvasWidth = 360;
let canvasHeigth = 640;
let goalLineDifference = 10;
let currentOctave = 3;
let timer = 0;
let insideGoalRange = false;
let currentFrequencyLineColor = [255, 30, 0];
let pitchHistory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

// define notes with their frequencies and note names
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

// loading voice overs of the notes
function preload()
{
  voiceOverA = loadSound('assets/voiceover_a.mp3');
  voiceOverB = loadSound('assets/voiceover_b.mp3');
  voiceOverC = loadSound('assets/voiceover_c.mp3');
  voiceOverD = loadSound('assets/voiceover_d.mp3');
  voiceOverE = loadSound('assets/voiceover_e.mp3');
  voiceOverF = loadSound('assets/voiceover_f.mp3');
  voiceOverG = loadSound('assets/voiceover_g.mp3');
}

function setup()
{
  createCanvas(canvasWidth, canvasHeigth);

  // setting up the mic
  audioContext = getAudioContext();
  mic = new p5.AudioIn();
  mic.start(detectPitch);

  // creating buttons
  octaveShiftUp = createButton('octave shift up');
  octaveShiftUp.position(5, 0);
  octaveShiftUp.mousePressed(shiftOctaveUp);

  octaveShiftDown = createButton('octave shift down');
  octaveShiftDown.position(5, 25);
  octaveShiftDown.mousePressed(shiftOctaveDown);

  goalRangeClose = createButton('goal range close');
  goalRangeClose.position(235, 25);
  goalRangeClose.mousePressed(goalLinesClose);

  goalRangeOpen = createButton('goal range open');
  goalRangeOpen.position(235, 0);
  goalRangeOpen.mousePressed(goalLinesOpen);

  newNote = createButton('new note');
  newNote.position(5, 600);
  newNote.mousePressed(createNewNote);

  // picks a random object from the notes array
  randomNote = int(random(notes.length - 1));

  // takes the right note and frequency of that object
  goalNote = notes[randomNote].note
  goalFrequency = -notes[randomNote].frequency

  // play the voice over of the first goal note
  playVoiceOver();

  // triggering the pitch history every 100 ms
  setInterval(pitchUpdate, 100);
}

// detects the pitch based on the CREPE model
function detectPitch()
{
  console.log('listening...');
  pitch = ml5.pitchDetection(model_url, audioContext, mic.stream, modelLoaded);
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

// loads the CREPE pitch detection model
function modelLoaded()
{
  console.log('model loaded');
  pitch.getPitch(gotPitch);
}

// creating a buffer for the previous pitches and shifts it around
function pitchUpdate()
{
  pitchHistory[9] = -currentFrequency;
  pitchHistory.shift();
}

// define the goal line
function createGoalLine()
{
  // lower goal line
  line(0, goalFrequency + goalLineDifference, canvasWidth, goalFrequency + goalLineDifference);

  // upper goal line
  line(0, goalFrequency - goalLineDifference, canvasWidth, goalFrequency - goalLineDifference);

  // display the current note
  text(goalNote, width / 2.15, goalFrequency - 30);

  // display number of the current octave next to the current note
  text(currentOctave, width / 1.85, goalFrequency - 30);
}

// function to make the goal range narrower
function goalLinesClose()
{
  goalLineDifference = goalLineDifference - 1;
}

// function to make the goal range bigger
function goalLinesOpen()
{
  goalLineDifference = goalLineDifference + 1;
}

// function that check if the current frequency is inside the goal range
function checksIfInsideGoalRange()
{
  if (-currentFrequency <= goalFrequency + goalLineDifference &&
      -currentFrequency >= goalFrequency - goalLineDifference)
  {
    currentFrequencyLineColor = [0, 255, 0];
    insideGoalRange = true;
  }

  else
  {
    currentFrequencyLineColor = [255, 30, 255];
    insideGoalRange = false;
  }
}

// checks if your frequency is inside the goal lines for 3 seconds
function checksRightPitch()
{
  if (insideGoalRange === true && frameCount % 60 == 0)
  {
    timer++
    currentFrequencyLineColor = [0, 255, 0];
    console.log(timer);

    // if this happens, 3 seconds have passed and the next note starts
    if (timer === 3)
      {
        timer = 0;

        // creates new note
        createNewNote();
      }
  }

  // if you go outside the goal range, the timer will reset to 0
  if (insideGoalRange === false)
  {
    timer = 0;
  }
}

// function that checks the current note and plays the right voice over
function playVoiceOver()
{
  if (goalNote == 'A')
  {
    voiceOverA.play();
  }

  else if (goalNote == 'B')
  {
    voiceOverB.play();
  }

  else if (goalNote == 'C')
  {
    voiceOverC.play();
  }

  else if (goalNote == 'D')
  {
    voiceOverD.play();
  }

  else if (goalNote == 'E')
  {
    voiceOverE.play();
  }

  else if (goalNote == 'F')
  {
    voiceOverF.play();
  }

  else if (goalNote == 'G')
  {
    voiceOverG.play();
  }
}

// creates new note by redefining the note / frequency values
function createNewNote()
{
  randomNote = int(random(notes.length - 1));
  goalNote = notes[randomNote].note
  goalFrequency = -notes[randomNote].frequency

  // play voice over when the new note is created
  playVoiceOver();
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

function draw()
{
  background(40);

  // flips the coördinate system so coördinate 0 is in the lower left corner
  // therefore some values of drawing variables are negative
  translate(0, 640);

  // show the current frequency that is heard
  textAlign(CENTER, CENTER);
  fill(255);
  textSize(32);

  // display the current frequency at the bottom
  text(currentFrequency.toFixed(1), width / 2, -30);

  // draw the line of the current frequency that is heard
  stroke(currentFrequencyLineColor);
  line(canvasWidth / 2, -currentFrequency, canvasWidth, -currentFrequency);

  // draws the line of the previous detected pitches on the left of the current frequency line
  for (let i = 0; i < pitchHistory.length - 1; ++i)
    {
      let deltaX = canvasWidth / ((pitchHistory.length - 1) * 2)
      line(i * deltaX, pitchHistory[i], (i + 1) * deltaX, pitchHistory[i + 1]);
    }

  // draw the goal line
  stroke(255);
  createGoalLine();

  // draw the bar that tells you the progress of the time inside the goal range
  stroke(255);
  noFill();
  rect(250, -40, 90, 20);

  // draw the filling bar
  noStroke();
  fill(0, 255, 0);
  let fillBar = 30 * timer;
  rect(250, -40, fillBar, 20);

  checksRightPitch();
  checksIfInsideGoalRange();
}
