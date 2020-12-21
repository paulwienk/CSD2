//
// Created by paulw on 21-12-2020.
//

#include "square.h"
#define _USE_MATH_DEFINES
#include <math.h>

Square::Square(float frequency, double samplerate) : frequency(frequency),
                                                 samplerate(samplerate), amplitude(1.0), sample(0), phase(0)
{
    std::cout << "Square - constructor\n";
}



Square::~Square() {
    std::cout << "Square - destructor\n";
}


float Square::getSample() {
    return sample;
}

void Square::tick() {
    // NOTE - frequency / SAMPLERATE can be implemented in a more efficient way
    phase += frequency / samplerate;
    sample = sin(M_PI * 2 * phase);
}

//getters and setters
void Square::setFrequency(float frequency)
{
    // TODO add check to see if parameter is valid
    this->frequency = frequency;
}

float Square::getFrequency()
{
    return frequency;
}
