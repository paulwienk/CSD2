#include <string>
#include <iostream>


class Oscillator
{
public:
    Oscillator(int freq, int sampleRate) : freq(freq), sampleRate(sampleRate) {}

    void makeSound();
    void melody();
    int freq;
    int sampleRate;
};

void Oscillator::makeSound() {

    std::cout << " freq and samplerate: " 
              << freq 
              << ", "
              << sampleRate
              << std::endl;
}


void melody() {}


class Sine : public Oscillator 
{
public:
    Sine() : Oscillator(440, 44100) {}

};


class Square : public Oscillator
{
public:
    Square() : Oscillator(570, 44100) {}
};


class Triangle : public Oscillator
{
public:
    Triangle() : Oscillator(780, 44100) {}
};


int main()
{
    auto si = Sine();
    auto sq = Square();
    si.makeSound();
    sq.makeSound();
    return 0;
}