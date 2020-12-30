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

int main(int argc,char **argv)
{

  // create a JackModule instance
  JackModule jack;

  // init the jack, use program name as JACK client name
  jack.init("example.exe");
  double samplerate = jack.getSamplerate();
  Sine sine(0, samplerate);
  Square square(0, samplerate);
  Saw saw(880, samplerate);




  //assign a function to the JackModule::onProces
  // lambda
  jack.onProcess = [&sine, &square, &saw] (float *inBuf, float *outBuf, int nframes) {

    static float amplitude = 0.15;

    for(unsigned int i = 0; i < nframes; i++) {
      outBuf[i] = sine.getSample() * amplitude;
      sine.tick();
      outBuf[i] += square.getSample() * amplitude;
      square.tick();
      outBuf[i] += saw.getSample() * amplitude;
      saw.tick();
    }



    return 0;
  };

  jack.autoConnect();

  bool keepMelodyThreadActive = true;

  // maak melody thread (start meteen)
  auto melodyThread = std::thread {
      [&]() {
          while (keepMelodyThreadActive) {
              saw.setAmplitude (0.0);
              std::this_thread::sleep_for (100ms);
              saw.setAmplitude (1.0);
              std::this_thread::sleep_for (100ms);

          }
      }
  };


  //keep the program running and listen for user input, q = quit
  std::cout << "\n\nPress 'q' when you want to quit the program.\n";
  bool running = true;
  while (running)
  {
    switch (std::cin.get())
    {
      case 'q':
        running = false;
        jack.end();
        break;
    }
  }

    // als je klaar bent vanaf the UI (via 'quit' command bijvoorbeeld)
    keepMelodyThreadActive = false;

    // wacht totdat de thread klaar is voordat het programma stopt
    melodyThread.join();

  //end the program
  return 0;
} // main()
