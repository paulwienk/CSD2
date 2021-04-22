function setup() {
  createCanvas(1200, 600)
  background(104)
}

function draw() {
  stroke(255)
  strokeWeight(8)

  if (mouseIsPressed === true) {
    line(mouseX, mouseY, pmouseX, pmouseY)
    console.log(pmouseX)
  }
}
