#define _USE_MATH_DEFINES

#include "square.h"
#include <math.h>


void Square::tick() {
    updatePhase();

    // calculations for the square wave.
    // if the phase is below 0.5, the sample is at the highest amplitude level: 1.
    // if the phase is above 0.5, the sample is at the lowest amplitude level: -1.
    // this creates a simple square wave.
    if (phase < 0.5) { sample = 1 * amplitude; }
    else { sample = -1 * amplitude; }
}