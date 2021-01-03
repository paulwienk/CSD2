#ifndef SYNTH_SONG_SAW_H
#define SYNTH_SONG_SAW_H
#include <iostream>
#include "oscillator.h"

class Saw : public Oscillator
{
public:
    //Constructor and destructor
    Saw(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}
    ~Saw() override {}

    void tick() override;
};


#endif