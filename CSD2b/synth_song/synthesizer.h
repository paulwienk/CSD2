#pragma once

class Synthesizer {
    virtual void noteOn(int midiNote);
    virtual void noteOff();

    float getSample();
    virtual void tick();
};

class SquareSynthesizer : public Synthesizer {
    void tick() override;
    void noteOn(int midiNote) override {
        square.setFrequency;
    }
    void noteOff() override;

    Square square;
};

//van internet
float mtof(int midiNote) {
    int a = 440; //frequency of A (common value is 440Hz)
    return (a / 32) * pow(2, ((midiNote - 9) / 12));
}


