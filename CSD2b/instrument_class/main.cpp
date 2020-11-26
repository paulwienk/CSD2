#include <iostream>
#include <string>
#include "instrument_class.h"


// main function with 2 objects which generates 2 different sounds
int main ()
{
    Instrument myInstrument("pweeeeep");
    Instrument myInstrument2("flflflflfl");
    myInstrument.play();
    myInstrument2.play();
}
