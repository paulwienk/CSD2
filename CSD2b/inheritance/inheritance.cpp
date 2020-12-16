#include <string>
#include <iostream>
#include "inheritance.h"


int main()
{
    auto p = Piano();
    auto s = Synth();
    p.makeSound();
    s.makeSound();
    return 0;
}