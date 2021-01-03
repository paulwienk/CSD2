#pragma once

#include <iostream>
#include "oscillator.h"

// sine class, derived from base class Oscillator
class Sine : public Oscillator {
public:
    Sine(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}

    void tick() override;
};



