//
// Created by paulw on 21-12-2020.
//

#define _USE_MATH_DEFINES
#include "saw.h"
#include <math.h>

// modulo function by Wouter Ensink
template <typename T>
inline constexpr T modulo (T dividend, const T divisor) noexcept
{
    while (dividend >= divisor)
        dividend -= divisor;

    return dividend;
}

Saw::Saw(float frequency, double samplerate) : frequency(frequency),
                                                     samplerate(samplerate), amplitude(1.0), sample(0), phase(0)
{
    std::cout << "Saw - constructor\n";
}



Saw::~Saw() {
    std::cout << "Saw - destructor\n";
}


float Saw::getSample() {
    return sample;
}

// rekent de volgende sample uit
void Saw::tick() {
    auto phaseIncrement = frequency / samplerate;
    phase = modulo (phase + phaseIncrement, 1.0);
    sample = (phase * 2) - 1;

}

//getters and setters
void Saw::setFrequency(float frequency)
{
    // TODO add check to see if parameter is valid
    this->frequency = frequency;
}

float Saw::getFrequency()
{
    return frequency;
}