#include <iostream>
#include <string>


// class of the instrument
class Instrument
{
public:
    Instrument(std::string sound);
    ~Instrument();
    void play();

private:
    std::string playsound;
};


// play function which prints the sounds
void Instrument::play()
{
    std::cout << playsound << "\n";
}


// direct initialization for the constructor
Instrument::Instrument(std::string sound) : playsound(sound) {}


Instrument::~Instrument() {}


// main function with 2 objects which generates 2 different sounds
int main ()
{
    Instrument myInstrument("pweeeeep");
    Instrument myInstrument2("flflflflfl");
    myInstrument.play();
    myInstrument2.play();
}
