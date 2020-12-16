#include <iostream>
#include <string>
#include "instrument_class.h"

// play function which prints the sounds
void Instrument::play()
{
    std::cout << playsound << "\n";
}


// direct initialization for the constructor
Instrument::Instrument(std::string sound) : playsound(sound) {}


Instrument::~Instrument() {}
