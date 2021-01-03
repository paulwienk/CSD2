#pragma once

// MIDI to frequency formula by YuxiUx
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


// creating a square synthesizer which plays a square wave
class SquareSynthesizer : public Synthesizer {
public:
    SquareSynthesizer(double sampleRate) : square(1, sampleRate) {
        square.setAmplitude(0.0);
    }

    void tick() override {
        square.tick();
    }

    float getSample() override {
        return square.getSample();
    }

    void noteOn(int midiNote) override {
        //setFrequency gets the midiNote, which is converted to hertz by the mtof function
        square.setFrequency(mtof(midiNote));
        square.setAmplitude(1.0);
    }

    void noteOff() override {
        square.setAmplitude(0.0);
    }

    Square square;
};


// creating a sine synthesizer which plays a sine wave
class SineSynthesizer : public Synthesizer {
public:
    SineSynthesizer(double sampleRate) : sine(1, sampleRate) {
        sine.setAmplitude(0.0);
    }

    void tick() override {
        sine.tick();
    }

    float getSample() override {
        return sine.getSample();
    }

    void noteOn(int midiNote) override {
        sine.setFrequency(mtof(midiNote));
        sine.setAmplitude(1.0);
    }

    void noteOff() override {
        sine.setAmplitude(0.0);
    }

    Sine sine;
};


// creating a saw synthesizer which plays a saw wave
class SawSynthesizer : public Synthesizer {
public:
    SawSynthesizer(double sampleRate) : saw(1, sampleRate) {
        saw.setAmplitude(0.0);
    }

    void tick() override {
        saw.tick();
    }

    float getSample() override {
        return saw.getSample();
    }

    void noteOn(int midiNote) override {
        saw.setFrequency(mtof(midiNote));
        saw.setAmplitude(1.0);
    }

    void noteOff() override {
        saw.setAmplitude(0.0);
    }

    Saw saw;
};


// creating a ring modulation based synthesizer which plays a tone based on ring modulation
class RmSynthesizer : public Synthesizer {
public:
    RmSynthesizer(double sampleRate) : carrier(1, sampleRate), modulator(1, sampleRate) {
        carrier.setAmplitude(0.0);
        modulator.setAmplitude(0.0);
    }

    Sine carrier;
    Sine modulator;
    double ratio = 0.05;
    float sample = 0;

    void tick() override {
        carrier.tick();
        modulator.tick();
        sample = modulator.getSample() * carrier.getSample();
    }

    float getSample() override {
        return sample;
    }

    void noteOn(int midiNote) override {
        carrier.setFrequency(mtof(midiNote));
        carrier.setAmplitude(1.0);
        modulator.setFrequency(mtof(midiNote) * ratio);
        modulator.setAmplitude(1.0);
    }

    void noteOff() override {
        carrier.setAmplitude(0.0);
        modulator.setAmplitude(0.0);
    }

};