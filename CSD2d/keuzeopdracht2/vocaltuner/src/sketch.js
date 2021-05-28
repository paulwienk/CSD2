let mic;
let threshold = 0.2;

function setup()
{
  createCanvas(300, 400)
  setupAudio()
}

function draw(){
  background(0);
  fill(255);

  amplitude = mic.getLevel() * 1000;

  if (amplitude >= threshold)
  {
    console.log(amplitude);
  }

}

function setupAudio() {
	userStartAudio();
	mic = new p5.AudioIn();
	mic.start();
  getAudioContext().resume();
}
