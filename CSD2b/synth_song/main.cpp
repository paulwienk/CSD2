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


#define PI_2 6.28318530717959


using namespace std::chrono_literals;

//van internet
float mtof(int midiNote) {
    float a = 440; //frequency of A (common value is 440Hz)
    return (a / 32.0) * pow(2, ((midiNote - 9.0) / 12.0));
}

int main(int argc, char **argv) {

    // create a JackModule instance
    JackModule jack;

    // init the jack, use program name as JACK client name
    jack.init("example.exe");
    double samplerate = jack.getSamplerate();
    Sine sine(0, samplerate);
    Square square(0, samplerate);
    Saw saw(0, samplerate);

    Oscillator* osc = &sine;

    //assign a function to the JackModule::onProces
    // lambda
    jack.onProcess = [&osc](float *inBuf, float *outBuf, int nframes) {

        static float amplitude = 0.15;

        for (unsigned int i = 0; i < nframes; i++) {
            outBuf[i] = osc->getSample() * amplitude;
            osc->tick();
        }

        return 0;
    };

    jack.autoConnect();

    bool keepMelodyThreadActive = true;

    std::vector<int> notes = {60, 62, 64, 65, 67, 69, 71, 72};

    // maak melody thread (start meteen)
    auto melodyThread = std::thread {
            [&]() {
                while (keepMelodyThreadActive) {
                    for (auto note : notes) {
                        osc->setAmplitude(1.0);
                        osc->setFrequency(mtof(note));
                        std::this_thread::sleep_for(200ms);
                        osc->setAmplitude(0.0);
                        std::this_thread::sleep_for(100ms);
                    }
                }
            }
    };


    //keep the program running and listen for user input, q = quit
    std::cout << "\n\nPress 'q' when you want to quit the program.\n";
    bool running = true;
    while (running) {
        std::string input;
        std::getline(std::cin, input);

        if (input == "sine") {
            osc = &sine;
            std::cout << "Set to sine\n";
        }

        if (input == "square") {
            osc = &square;
            std::cout << "Set to square\n";
        }

        if (input == "saw") {
            osc = &saw;
            std::cout << "Set to saw\n";
        }

        if (input == "quit") {
            running = false;
        }

        input.clear();
    }

    // als je klaar bent vanaf the UI (via 'quit' command bijvoorbeeld)
    keepMelodyThreadActive = false;

    // wacht totdat de thread klaar is voordat het programma stopt
    melodyThread.join();

    //end the program
    return 0;
} // main()
