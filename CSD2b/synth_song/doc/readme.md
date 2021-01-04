# Synth Song
by Paul Wienk


A program that plays a sequence of MIDI notes from a synthesizer by choice. 
The synthesizers that can be chosen while playing the sequence are 'sine', 'square', 'saw' and 'ring modulation'.

The waveforms are derived from their base class Oscillator, which contains all parameters they need. 
The Synthesizer class is based on multiple synthesizers, which contains the waveforms and creates sound as the result.

In the program, you can switch between multiple synthesizers by the commands that are visible in the help text. 
To quit the program, you simply type 'quit'. 

# Source reference
- 'mingw-std-threads' by meganz for including <thread> in Windows
- 'midi-note-to-freq.md' by YuxiUx for the MIDI conversion to frequency
- Wouter Ensink for the modulo function
- Marc Groenewegen / Ciska Vriezenga for the jack_module 





