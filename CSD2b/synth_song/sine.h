#ifndef _SINE_H_
#define _SINE_H_
#include <iostream>
#include "oscillator.h"

class Sine : public Oscillator
{
public:
    //Constructor and destructor
    Sine(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}
    ~Sine() override {}

    void tick() override;
};


#endif
