#define _WIN32_WINNT 0x0501

#include <iostream>
#include "mingw-std-threads/mingw.thread.h"
#include <chrono>
#include "jack_module.h"
#include "math.h"
#include "sine.h"
#include "square.h"
#include "saw.h"
#include "oscillator.h"
#include "melodyGenerator.h"
#include "synthesizer.h"


#define PI_2 6.28318530717959


using namespace std::chrono_literals;

int main(int argc, char **argv) {

    // create a JackModule instance
    JackModule jack;

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();

    SquareSynthesizer synth(samplerate);

    //assign a function to the JackModule::onProces
    // lambda
    jack.onProcess = [&synth](float *inBuf, float *outBuf, int nframes) {

        static float amplitude = 0.15;

        for (unsigned int i = 0; i < nframes; i++) {
            outBuf[i] = synth.getSample() * amplitude;
            synth.tick();
        }

        return 0;
    };

    jack.autoConnect();

    bool keepMelodyThreadActive = true;

    MelodyGenerator melodyGenerator;
    auto notes = melodyGenerator.notes;





    // maak melody thread (start meteen)
    auto melodyThread = std::thread {
            [&]() {
                while (keepMelodyThreadActive) {
                    for (auto note : notes) {
                        //osc->setAmplitude(1.0);
                        //osc->setFrequency(mtof(note));
                        synth.noteOn(note);
                        std::this_thread::sleep_for(200ms);
                        //osc->setAmplitude(0.0);
                        synth.noteOff();
                        std::this_thread::sleep_for(400ms);
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
/*
        if (input == "sine") {
            osc = &sine;
            std::cout << "Set to sine\n";
        }

        if (input == "square") {
            osc = &square;
            std::cout << "Set to square\n";
        }

        if (input == "saw") {
            synth = &saw;
            std::cout << "Set to saw\n";
        }
*/
        if (input == "quit") {
            running = false;
        }

        input.clear();
    }

    // als je klaar bent vanaf the UI (via 'quit' command)
    keepMelodyThreadActive = false;

    // wacht totdat de thread klaar is voordat het programma stopt
    melodyThread.join();

    //end the program
    return 0;
} // main()
