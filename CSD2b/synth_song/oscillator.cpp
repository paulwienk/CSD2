#define _USE_MATH_DEFINES

#include <math.h>
#include "oscillator.h"

// modulo function by Wouter Ensink
template<typename T>
inline constexpr T modulo(T dividend, const T divisor) noexcept {
    while (dividend >= divisor)
        dividend -= divisor;

    return dividend;
}

// zodat de phase tussen 0 en 1 blijft en dat de phase ook verandert
void Oscillator::updatePhase() {
    // phase wordt dus steeds hoger
    phase = modulo(phase + phaseIncrement, 1.0);
}

// returnt de huidige sample
float Oscillator::getSample() {
    return sample;
}


//getters and setters
void Oscillator::setFrequency(float frequency) {
    this->frequency = frequency;
    // phaseIncrement wordt aangepast op basis van de nieuwe frequentie
    phaseIncrement = frequency / sampleRate;
}


void Oscillator::setAmplitude(float amp) {
    amplitude = amp;
}