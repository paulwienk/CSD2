#ifndef SYNTH_SONG_MELODYGENERATOR_H
#define SYNTH_SONG_MELODYGENERATOR_H

class MelodyGenerator
{
public:
    MelodyGenerator() {}

    std::vector<int> notes = {60, 62, 64, 60, 60, 62, 64, 60, 64, 65, 67, 67, 64, 65, 67, 67,
                              67, 69, 67, 65, 64, 64, 60, 60, 67, 69, 67, 65, 64, 64, 60, 60,
                              60, 60, 55, 55, 60, 60, 60, 60, 60, 60, 55, 55, 60, 60, 60, 60};
};

#endif //SYNTH_SONG_MELODYGENERATOR_H