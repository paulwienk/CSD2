#pragma once

#include <iostream>
#include "oscillator.h"

class Square : public Oscillator {
public:
    //Constructor and destructor
    Square(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}


    void tick() override;
};


