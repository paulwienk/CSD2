# Paul's Beat Generator
# Written by Paul Wienk

import random
from threading import Thread

import simpleaudio as sa

from clock import Clock
from euclidean import euclidean_rhythm
from midiutil.MidiFile import MIDIFile

# load samples
hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")

# default values to begin the first sequence
bpm = 120
numerator = 4
denominator = 4
ticks_per_quarternote = 4
keep_running = True


# function to determine the amount of ticks in a sequence based on the given numerator
def ticks_per_denominator():
    denominators_in_quarter = denominator / 4
    return ticks_per_quarternote / denominators_in_quarter


def ticks_per_bar():
    return ticks_per_denominator() * numerator


# converts given BPM in MS
def bpm_to_ms(bpm):
    return 60000 / (bpm * ticks_per_quarternote)


euclidean_sequence = 0
first_sequence = euclidean_rhythm(ticks_per_bar(), denominator)
tick_time_ms = bpm_to_ms(bpm)

# text for clear user interface
print("Welcome to Paul's Beat Generator!")
print("\nHere are a few commands to get you started:")
print("- type 'ts' to set a new time signature (numerator and denominator)")
print("- type 'bpm' to set a new BPM")
print("- type 'exit' or 'quit' to quit the generator")
print("- type 'midi' to save the beat as a MIDI file")
print("\nCurrent time signature: 4/4")
print("Current BPM: 120")
print("Current sequence:"), print(first_sequence)
print("\nEnjoy!")


# function to make sure the input is above 0
def ask_for_number(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Number must be higher than 0")

        except ValueError:
            print("Input must be a number. Try again.")


# function to handle the commands during the sequence
def next_command():
    global sequence, tick_time_ms, numerator, keep_running, denominator, bpm
    command = input('\n -> ')

    # checks if one of the rights commands is given
    if command not in ['ts', 'TS', 'Ts',
                       'bpm', 'BPM', 'Bpm',
                       'exit', 'Exit', 'EXIT',
                       'midi', 'Midi', 'MIDI']:
        print("Wrong input. Try again.")

    # sets a new time signature with error handling
    if command in ['ts', 'TS', 'Ts']:
        while True:
            numerator = ask_for_number("Set numerator: ")
            if numerator <= 1:
                print("Numerator has to be higher than 1. Try again.")
                continue

            if numerator >= 100:
                print('Numerator has to be lower than 100. Try again.')
                continue

            break

        while True:
            denominator = ask_for_number("Set denominator: ")
            if denominator not in [2, 4, 8, 16, 32, 64]:
                print("Denominator has to be a power of 2 (2, 4, 8, 16 ...). Try again.")
                continue

            make_sequence()
            print_sequence()
            break

        sequence = make_sequence()

    # sets a new bpm with error handling
    if command in ['bpm', 'BPM', 'Bpm']:
        while True:
            bpm = ask_for_number("Set BPM: ")
            if bpm <= 1:
                print("BPM has to be higher than 1. Try again.")
                continue
            if bpm >= 400:
                print("BPM has to be lower than 400. Try again.")
                continue

            break

        tick_time_ms = bpm_to_ms(bpm)

    # saves the generated beat to a MIDI file with error handling
    if command in ["midi", "MIDI", "Midi"]:
        while True:
            try:
                answer = str(input("Would you like to save the beat as a MIDI file? (yes/no): "))
                if answer == "yes":
                    make_midi_file(sequence)
                    print("MIDI file saved as 'sequence'")
                    break

                if answer == "no":
                    break

                if answer not in ["yes", "no"]:
                    print("Input has to be 'yes' or 'no'. Try again")

            except ValueError:
                print("Input has to be 'yes' or 'no'. Try again")

    # quits the generator
    if command in ['exit', 'Exit', 'EXIT']:
        keep_running = False
        print("\nThank you for using Paul's Beat Generator!")
        exit()


# function to make the event with the timestamp, instrument and instrument name
def make_event(timestamp, instrument, instrumentname):
    return {
        'timestamp': timestamp,
        'instrument': instrument,
        'instrumentname': instrumentname,
    }


# function that handles the given event
def handle_event(event):
    event['instrument'].play()


# function that makes the sequence (for example [1, 0, 0, 1, 0, 1, 0])
def make_sequence():
    global euclidean_sequence

    euclidean_sequence = euclidean_rhythm(ticks_per_bar(), denominator)
    rhythm = []

    for index, item in enumerate(euclidean_sequence):
        # play a kick on the 1
        if item == 1:
            rhythm.append(make_event(index, kick, "kick"))
        # play a snare on the 0 with a 20% chance of happening
        if item == random.choice([0, 2, 3, 4, 5]):
            rhythm.append(make_event(index, snare, "snare"))
        # play a hihat on the 0 or 1 with a 66% chance of happening
        if item == random.choice([0, 1, 2]):
            rhythm.append(make_event(index, hihat, "hihat"))

    return rhythm


# function used to print the sequence every time you change the time signature
def print_sequence():
    print(euclidean_sequence)


# function that plays the sequence in a loop
def play_sequence():
    global sequence
    clock = Clock(tick_time_ms)
    clock.start()

    while keep_running:
        for i in range(int(ticks_per_bar())):
            i = (i + 1) % int(ticks_per_bar())

            if not keep_running:
                return

            for e in sequence:
                if e['timestamp'] == i:
                    handle_event(e)

            clock.update_tick_time_ms(tick_time_ms)
            clock.block_until_next_tick()


# thread to handle multiple functions at the same time
def user_interface_thread():
    while True:
        next_command()


# function to create the MIDI sequence
def make_midi_file(list):
    mid = MIDIFile(1)

    # set default values
    channel = 9
    pitch = 35
    time = 0
    duration = 0.5
    tempo = bpm
    volume = 100
    track = 0
    mid.addTempo(track, time, tempo * 4)

    # for loop which checks if the instrument name is the same in sequence
    for i in list:
        if i['instrumentname'] == 'kick':
            pitch = 35
        elif i['instrumentname'] == 'snare':
            pitch = 39
        elif i['instrumentname'] == 'hihat':
            pitch = 42

        # adds midi note to midi file
        mid.addNote(track, channel, pitch, i['timestamp'], duration, volume)
        time = time + 1

    # creates the final midi file
    with open("sequence.midi", "wb") as output_file:
        mid.writeFile(output_file)


t = Thread(target=user_interface_thread)
t.start()
make_sequence()
sequence = make_sequence()
play_sequence()