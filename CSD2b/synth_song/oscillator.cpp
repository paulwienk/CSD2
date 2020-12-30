#define _USE_MATH_DEFINES
#include <math.h>
#include "oscillator.h"

// modulo function by Wouter Ensink
template <typename T>
inline constexpr T modulo (T dividend, const T divisor) noexcept
{
    while (dividend >= divisor)
        dividend -= divisor;

    return dividend;
}


float Oscillator::getSample() {
    return sample;
}


void Oscillator::updatePhase()
{
    phase = modulo (phase + phaseIncrement, 1.0);
}

//getters and setters
void Oscillator::setFrequency(float frequency)
{
    // TODO add check to see if parameter is valid
    this->frequency = frequency;
}


float Oscillator::getFrequency()
{
    return frequency;
}

void Oscillator::setAmplitude(float amp)
{
    amplitude = amp;
}