#pragma once

#include <iostream>
#include "oscillator.h"

// square class, derived from base class Oscillator
class Square : public Oscillator {
public:
    Square(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}

    void tick() override;
};


