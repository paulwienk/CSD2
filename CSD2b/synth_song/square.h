//
// Created by paulw on 21-12-2020.
//

#ifndef INC_03_SOUNDINGSINECLASS_SQUARE_H
#define INC_03_SOUNDINGSINECLASS_SQUARE_H
#include <iostream>

class Square
{
public:
    //Constructor and destructor
    Square(float frequency, double samplerate);
    ~Square();

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

#endif //INC_03_SOUNDINGSINECLASS_SQUARE_H
