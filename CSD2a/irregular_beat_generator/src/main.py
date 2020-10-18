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

# set bpm
bpm = 120
numerator = 4
denominator = 4
ticks_per_quarternote = 4
keep_running = True


def ticks_per_denominator():
    denominators_in_quarter = denominator / 4
    return ticks_per_quarternote / denominators_in_quarter


def ticks_per_bar():
    return ticks_per_denominator() * numerator


# converts given BPM in MS
def bpm_to_ms(bpm):
    return 60000 / (bpm * ticks_per_quarternote)


first_sequence = euclidean_rhythm(ticks_per_bar(), denominator)
tick_time_ms = bpm_to_ms(bpm)

print("Welcome to Paul's Beat Generator!")
print("")
print("Here are a few commands to get you started:")
print("- type 'ts' to set a new time signature (numerator and denominator)")
print("- type 'bpm' to set a new BPM")
print("- type 'exit' or 'quit' to quit the generator")
print("")
print("Current time signature: 4/4")
print("Current BPM: 120")
print("Current sequence:"), print(first_sequence)
print("")
print("Enjoy!")


# function to handle the commands during the sequence
def next_command():
    global sequence, tick_time_ms, numerator, keep_running, denominator, bpm
    command = input(' -> ')

    if command not in ['ts', 'bpm', 'exit', 'quit']:
        print("Wrong input. Try again.")

    if command == 'ts':
        while True:
            try:
                numerator = int(input("Set numerator: "))
                if numerator <= 1:
                    print("Numerator has to be higher than 1. Try again.")
                    continue

                break

            except ValueError:
                print("Numerator has to be a number. Try again.")
                continue

        while True:
            try:
                denominator = int(input("Set denominator: "))
                if denominator not in [2, 4, 8, 16, 32, 64]:
                    print("Denominator has to be a power of 2 (2, 4, 8, 16 ...). Try again.")
                    continue

                make_sequence()
                print_sequence()
                break

            except ValueError:
                print("Denominator has to be a number. Try again.")
                continue

        sequence = make_sequence()

    if command == 'bpm':
        while True:
            try:
                bpm = int(input("Set BPM: "))
                if bpm <= 1:
                    print("BPM has to be higher than 1. Try again.")
                    continue

            except ValueError:
                print("BPM has to be a number. Try again.")
                continue

            break

        tick_time_ms = bpm_to_ms(bpm)

    if command in ['exit', 'quit']:
        keep_running = False
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


euclidean_sequence = 0


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


def make_midi_file(list):
    mid = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
    # automatically)

    channel = 9
    pitch = 35
    time = 0  # In beats
    duration = 0.5  # In beats
    tempo = bpm  # In BPM
    volume = 100  # 0-127, as per the MIDI standard
    track = 0
    mid.addTempo(track, time, tempo)

    for i in list:
        mid.addNote(track, channel, pitch, duration, tempo, volume)

    with open("ja.midi", "wb") as output_file:
        mid.writeFile(output_file)


make_midi_file(euclidean_sequence)


t = Thread(target=user_interface_thread)
t.start()
sequence = make_sequence()
play_sequence()