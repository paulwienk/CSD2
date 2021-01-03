#include <iostream>
#include <chrono>
#include "thread.h"
#include "jack_module.h"
#include "math.h"
#include "sine.h"
#include "square.h"
#include "saw.h"
#include "oscillator.h"
#include "melodyGenerator.h"
#include "synthesizer.h"


#define PI_2 6.28318530717959

// voor ms
using namespace std::chrono_literals;

int main(int argc, char **argv) {

    // create a JackModule instance
    JackModule jack;

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();

    SquareSynthesizer squareSynthesizer(samplerate);
    SineSynthesizer sineSynthesizer(samplerate);
    SawSynthesizer sawSynthesizer(samplerate);
    RmSynthesizer rmSynthesizer(samplerate);

    // by default
    Synthesizer *synth = &sineSynthesizer;

    //assign a function to the JackModule::onProces
    // lambda
    jack.onProcess = [&synth](float *inBuf, float *outBuf, int nframes) {

        static float amplitude = 0.15;

        for (int i = 0; i < nframes; i++) {
            outBuf[i] = synth->getSample() * amplitude;
            synth->tick();
        }

        return 0;
    };

    jack.autoConnect();

    bool keepMelodyThreadActive = true;

    MelodyGenerator melodyGenerator;
    auto notes = melodyGenerator.notes;


    // maak melody thread (start meteen)
    // [&] is een referentie naar alles inde bovenliggende scope
    auto melodyThread = std::thread{
            [&]() {
                while (keepMelodyThreadActive) {
                    // note is elke keer de volgende note in de notes array
                    // range based for loop
                    for (auto note : notes) {
                        synth->noteOn(note);
                        std::this_thread::sleep_for(200ms);
                        synth->noteOff();
                        std::this_thread::sleep_for(100ms);

                        if (!keepMelodyThreadActive)
                            return;
                        // thread stopt hier als de if wordt uitgevoerd
                    }
                }
            }
    };


    //keep the program running and listen for user input, q = quit
    std::cout << "\n\nPress 'quit' when you want to quit the program.\n";
    bool running = true;
    while (running) {
        std::string input;
        std::getline(std::cin, input);

        if (input == "sine") {
            synth = &sineSynthesizer;
            std::cout << "Set to sine\n";
        }

        if (input == "square") {
            synth = &squareSynthesizer;
            std::cout << "Set to square\n";
        }

        if (input == "saw") {
            synth = &sawSynthesizer;
            std::cout << "Set to saw\n";
        }

        if (input == "rm") {
            synth = &rmSynthesizer;
            std::cout << "Set to ring modulation\n";
        }

        if (input == "quit") {
            running = false;
        }

    }

    // als je klaar bent vanaf the UI (via 'quit' command)
    // dan is hij uit de loop hierboven
    keepMelodyThreadActive = false;

    // wacht totdat de thread klaar is voordat het programma stopt
    melodyThread.join();

    //end the program
    return 0;
} // main()
