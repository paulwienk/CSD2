// main template by Ciska Vriezenga


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

// to make the milliseconds work in line 71
using namespace std::chrono_literals;

int main(int argc, char **argv) {

    // create a JackModule instance
    JackModule jack;

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();

    // creating objects of the synthesizers
    SquareSynthesizer squareSynthesizer(samplerate);
    SineSynthesizer sineSynthesizer(samplerate);
    SawSynthesizer sawSynthesizer(samplerate);
    RmSynthesizer rmSynthesizer(samplerate);

    // by default
    Synthesizer *synth = &sineSynthesizer;

    //assign a function to the JackModule::onProces
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

    // creating an object of the melody generator
    MelodyGenerator melodyGenerator;
    auto notes = melodyGenerator.notes;


    // creating melody thread
    auto melodyThread = std::thread{
            [&]() {
                while (keepMelodyThreadActive) {

                    // range based for loop
                    for (auto note : notes) {

                        // pointer to the noteOn function of the active synthesizer.
                        // the noteOn contains 'note', which is the next note in the array.
                        synth->noteOn(note);
                        std::this_thread::sleep_for(200ms);
                        synth->noteOff();
                        std::this_thread::sleep_for(100ms);

                        if (!keepMelodyThreadActive)
                            return;

                    }
                }
            }
    };


    //keep the program running and listen for user input
    std::cout << "\n\nWelcome to Paul's Synth Song!\n\n";
    std::cout << "Type 'sine', 'saw' or 'square' to activate the eponymous synthesizer.\n";
    std::cout << "Type 'rm' to activate a ring modulated synthesizer.\n\n";
    std::cout << "Type 'quit' to exit the program.\n\n";
    bool running = true;
    while (running) {
        std::string input;
        std::getline(std::cin, input);

        if (input == "sine") {
            synth = &sineSynthesizer;
            std::cout << "Set to sine\n\n";
        } else if (input == "square") {
            synth = &squareSynthesizer;
            std::cout << "Set to square\n\n";
        } else if (input == "saw") {
            synth = &sawSynthesizer;
            std::cout << "Set to saw\n\n";
        } else if (input == "rm") {
            synth = &rmSynthesizer;
            std::cout << "Set to ring modulation\n\n";
        } else if (input == "quit") {
            running = false;
        }

            // everything except the commands above returns an error
        else {
            std::cout << "Wrong input. Try again\n\n";
        }


    }

    // setting the thread to non-active after you quit the program
    keepMelodyThreadActive = false;
    melodyThread.join();

    //end the program
    return 0;
}
