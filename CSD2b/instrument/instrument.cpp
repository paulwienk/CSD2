#include <iostream>
#include <string>


class Instrument
{
public:
    Instrument(std::string sound);
    ~Instrument();
    void play();

private:
    std::string playsound;
};


void Instrument::play()
{
    std::cout << playsound << "\n";
}

//direct initialization
Instrument::Instrument(std::string sound) : playsound(sound) {}


Instrument::~Instrument() {}


int main ()
{
    Instrument myInstrument("pweeeeep");
    Instrument myInstrument2("flflflflfl");
    myInstrument.play();
    myInstrument2.play();
}
