#ifndef SYNTH_SONG_SQUARE_H
#define SYNTH_SONG_SQUARE_H
#include <iostream>
#include "oscillator.h"

class Square : public Oscillator
{
public:
    //Constructor and destructor
    Square(double frequency, double sampleRate) : Oscillator(frequency, sampleRate) {}
    ~Square() override {}

    void tick() override;
};


#endif
