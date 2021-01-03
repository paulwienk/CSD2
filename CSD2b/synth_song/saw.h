#pragma once

#include <iostream>
#include "oscillator.h"

class Saw : public Oscillator {
public:
    //Constructor & constructor from base class
    Saw(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}

    // laat oscillator steeds een sample verdergaan. wordt bij elke sample steeds aangeroepen
    void tick() override;
};