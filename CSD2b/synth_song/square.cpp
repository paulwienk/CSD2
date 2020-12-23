#define _USE_MATH_DEFINES
#include "square.h"
#include <math.h>


void Square::tick()
{
    updatePhase();
    if (phase < 0.5) {sample = 1;}
    else {sample = -1;}
}

