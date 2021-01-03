#ifndef SYNTH_SONG_OSCILLATOR_H
#define SYNTH_SONG_OSCILLATOR_H


class Oscillator
{
public:
    Oscillator(double frequency, double sampleRate) : frequency(frequency), sampleRate(sampleRate) {}
    virtual ~Oscillator() {}
    //return the current sample
    float getSample();

    //getters and setters
    void setAmplitude(float);
    void setFrequency(float frequency);
    float getFrequency();

    virtual void tick() {}

protected:
    double sampleRate;
    double frequency;
    float amplitude = 1.0;
    double phase = 0.0;
    float sample = 0.0;

    double phaseIncrement = frequency / sampleRate;

    void updatePhase();
};

#endif //SYNTH_SONG_OSCILLATOR_H
