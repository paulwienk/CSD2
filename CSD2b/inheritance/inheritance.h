#include <string>
#include <iostream>


class Instrument
{
public:
    Instrument(std::string instr, std::string sound) : nameInstr(instr), sound(sound) {}
    std::string nameInstr;
    std::string sound;
};

class KeyInstrument : public Instrument
{ 
public:
    KeyInstrument(std::string name, std::string sound, int keys) : Instrument(name, sound), numKeys(keys) {}

    void makeSound()

    {
        std::cout << "this " 
                  << nameInstr
                  << " has "
                  << numKeys 
                  << " keys and makes the following sound: " 
                  << sound 
                  << std::endl;

    }
    int numKeys;

};


class Piano : public KeyInstrument 
{
public:
    Piano() : KeyInstrument("piano", "pling", 88) {}
};


class Synth : public KeyInstrument
{
public:
    Synth() : KeyInstrument("synth", "njjeewwww", 88) {}
};