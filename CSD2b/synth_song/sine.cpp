#define _USE_MATH_DEFINES
#include "sine.h"
#include <math.h>


void Sine::tick()
{
    updatePhase();
    sample = (sin(M_PI * 2 * phase)) * amplitude;
}