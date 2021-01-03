#pragma once

//van internet
float mtof(int midiNote) {
    float a = 440.0;
    return (a / 32.0) * pow(2.0, ((midiNote - 9.0) / 12.0));
}


class Synthesizer {
public:
    virtual ~Synthesizer() = default;
    virtual void noteOn(int midiNote) {}
    virtual void noteOff() {}

    virtual float getSample() {}
    virtual void tick() {}
};

class SquareSynthesizer : public Synthesizer {
public:
    SquareSynthesizer(double sampleRate) : square(1, sampleRate) {
        //zodat ie niet meteen aangaat
        square.setAmplitude(0.0);
    }

    void tick() override {
        square.tick();
    }

    float getSample() override {
        return square.getSample();
    }

    void noteOn(int midiNote) override {
        //setFrequency krijgt de frequency omgerekend naar midi mee als argument dmv mtof functie
        square.setFrequency(mtof(midiNote));
        square.setAmplitude(1.0);
    }

    void noteOff() override {
        square.setAmplitude(0.0);
    }

    Square square;
};