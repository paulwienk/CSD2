#pragma once

// class that generated a (hardcoded) melody
class MelodyGenerator {
public:
    MelodyGenerator() {}


    // array that plays Brother John or Frère Jacques or Vader Jacob or whatever
    std::vector<int> notes = {60, 62, 64, 60, 60, 62, 64, 60, 64, 65, 67, 67, 64, 65, 67, 67,
                              67, 69, 67, 65, 64, 64, 60, 60, 67, 69, 67, 65, 64, 64, 60, 60,
                              60, 60, 55, 55, 60, 60, 60, 60, 60, 60, 55, 55, 60, 60, 60, 60};
};