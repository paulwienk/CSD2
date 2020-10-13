import simpleaudio as sa
import time
import random
import regex
from threading import Thread
from clock import Clock
from euclidean_rhythm import euclidean_rhythm


# load samples
hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")

# set bpm
bpm = 120
numerator = 4
denominator = 4
keep_running = True
ticks_per_quarternote = 4


# converts given BPM in MS
def bpm_to_ms(bpm):
    return 60000 / (bpm * ticks_per_quarternote)


tick_time_ms = bpm_to_ms(bpm)


# function to handle the commands during the sequence
def next_command():
    global sequence, tick_time_ms, numerator, keep_running, denominator
    command = input(' -> ')

    if command == 'ts':
        numerator = int(input("Set numerator: "))
        denominator = int(input("Set denominator: "))
        sequence = make_sequence()
    if command == 'bpm':
        bpm = int(input("Set BPM: "))
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


# function that makes the sequence (for example [1, 0, 0, 1, 0, 1, 0])
def make_sequence():
    euclidean_sequence = euclidean_rhythm(ticks_per_bar(), 5)
    sequence_len = len(euclidean_sequence)
    rhythm = []
    print(ticks_per_bar())

    # play a kick on the 1
    for index, item in enumerate(euclidean_sequence):
        if item == 1:
            rhythm.append(make_event(index, kick, "kick"))
        if item == random.choice([0, 2]):
            rhythm.append(make_event(index, snare, "snare"))

    return rhythm


def ticks_per_denominator():
    denominators_in_quarter = denominator / 4
    return ticks_per_quarternote / denominators_in_quarter


def ticks_per_bar():
    return ticks_per_denominator() * numerator


total_ticks = numerator * ticks_per_quarternote


# function that plays the sequence in a loop
def play_sequence():
    global sequence
    clock = Clock(tick_time_ms)
    clock.start()

    while keep_running:
        for i in range(total_ticks):
            i = (i + 1) % total_ticks

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


t = Thread(target=user_interface_thread)
t.start()
sequence = make_sequence()
play_sequence()