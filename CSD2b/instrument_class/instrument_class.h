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
