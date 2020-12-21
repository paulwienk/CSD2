// deels ciska deels paul

#define _USE_MATH_DEFINES
#include "square.h"
#include <math.h>


// modulo function by Wouter Ensink
template <typename T>
inline constexpr T modulo (T dividend, const T divisor) noexcept
{
    while (dividend >= divisor)
        dividend -= divisor;

    return dividend;
}

Square::Square(float frequency, double samplerate) : frequency(frequency),
                                                 samplerate(samplerate), amplitude(1.0), sample(0), phase(0)
{
    std::cout << "Square - constructor\n";
}



Square::~Square() {
    std::cout << "Square - destructor\n";
}


float Square::getSample() {
    return sample;
}

void Square::tick() {
    auto phaseIncrement = frequency / samplerate;
    phase = modulo (phase + phaseIncrement, 1.0);
    if (phase < 0.5) {sample = 1;}
    else {sample = -1;}
}

//getters and setters
void Square::setFrequency(float frequency)
{
    // TODO add check to see if parameter is valid
    this->frequency = frequency;
}

float Square::getFrequency()
{
    return frequency;
}
