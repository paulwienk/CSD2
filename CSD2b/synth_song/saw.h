//
// Created by paulw on 21-12-2020.
//

#ifndef SYNTH_SONG_SAW_H
#define SYNTH_SONG_SAW_H
#include <iostream>

class Saw
{
public:
    //Constructor and destructor
    Saw(float frequency, double samplerate);
    ~Saw();

    //return the current sample
    float getSample();
    // go to next sample
    void tick();

    //getters and setters
    void setFrequency(float frequency);
    float getFrequency();

    //NOTE - do we need a setter for phase? for now -> not using one

private:
    double samplerate;
    float amplitude;
    double frequency;
    double phase;
    // contains the current sample
    float sample;
};


#endif //SYNTH_SONG_SAW_H
