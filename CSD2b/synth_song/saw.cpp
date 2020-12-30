#define _USE_MATH_DEFINES
#include "saw.h"
#include <math.h>


void Saw::tick()
{
    updatePhase();
    sample = ((phase * 2) - 1) * amplitude;
}