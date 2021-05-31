// template by Daniel Shiffman, adjusted by Paul Wienk

const model_url = 'https://cdn.jsdelivr.net/gh/ml5js/ml5-data-and-models/models/pitch-detection/crepe/';
let pitch, mic;
let freq = 0;
let canvasWidth = 360;
let canvasHeigth = 640;
let randomNote, goalNote, goalFrequency;

let notes = [
  {
    note: 'A',
    frequency: 440.0
  },
  {
    note: 'B',
    frequency: 493.9
  },
  {
    note: 'C',
    frequency: 261.6
  },
  {
    note: 'D',
    frequency: 293.7
  },
  {
    note: 'E',
    frequency: 329.6
  },
  {
    note: 'F',
    frequency: 349.2
  },
  {
    note: 'G',
    frequency: 392.0
  },
];

function setup()
{
  createCanvas(canvasWidth, canvasHeigth);
  audioContext = getAudioContext();
  mic = new p5.AudioIn();
  mic.start(detectPitch);

  randomNote = int(random(notes.length - 1));
  goalNote = notes[randomNote].note
  goalFrequency = notes[randomNote].frequency
}

function detectPitch()
{
  console.log('listening');
  pitch = ml5.pitchDetection(
    model_url,
    audioContext,
    mic.stream,
    modelLoaded
  );
}

function createGoalLine()
{
  line(0, goalFrequency + 10, canvasWidth, goalFrequency + 10)
  line(0, goalFrequency - 10, canvasWidth, goalFrequency - 10)
  text(goalNote, width / 2, goalFrequency - 30)
}

function draw()
{
  background(130);
  textAlign(CENTER, CENTER);
  fill(255);
  textSize(32);
  text(freq.toFixed(1), width / 2, height - 50);

  line(0, freq, canvasWidth, freq);
  createGoalLine()
}

function modelLoaded()
{
  console.log('model loaded');
  pitch.getPitch(gotPitch);
}

function gotPitch(error, frequency)
{
  if (error)
  {
    console.error(error);
  }

  else
  {
    //console.log(frequency);
    if (frequency)
    {
      freq = frequency;
    }

    pitch.getPitch(gotPitch);
  }
}
