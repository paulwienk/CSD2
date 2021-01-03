#define _USE_MATH_DEFINES

#include "sine.h"
#include <math.h>


void Sine::tick() {
    updatePhase();

    // calculations for the sine wave by Ciska Vriezenga.
    sample = (sin(M_PI * 2 * phase)) * amplitude;
}