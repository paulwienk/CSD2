#pragma once

#include <iostream>
#include "oscillator.h"

class Sine : public Oscillator {
public:
    //Constructor and destructor
    Sine(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}


    void tick() override;
};



