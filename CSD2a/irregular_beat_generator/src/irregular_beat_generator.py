import simpleaudio as sa
import time
import random
from threading import Thread

# load samples
hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")


# set bpm
bpm = 120


# converts given BPM in MS
def bpm_to_ms(bpm):
    return (60000 / bpm) * 0.5


tick_time_ms = bpm_to_ms(bpm)


# function to handle the commands during the sequence
def next_command():
    global sequence, tick_time_ms, beats
    command = input(' -> ')
    # make 16 5
    # time signature 5/4 en dan zelf beats berekenen
    # make <nummer> <nummer>
    # ^beats\s\d+$
    # beats_pattern = regex.compile(r'^beats\s\d+$')
    if command[:4] == 'make':
        beats = int(command[5:7])
        pulses = int(command[8])
        sequence = make_sequence(beats, pulses)
    if command[:5] == 'tempo':
        bpm = int(command[6:])
        tick_time_ms = bpm_to_ms(bpm)


# Clock class by Wouter Ensink
class Clock:
    def __init__(self, tick_time_ms: float):
        self.current_time = 0
        self.tick_time_seconds = tick_time_ms * 0.001
        self.target_time = 0

    def start(self) -> None:
        self.current_time = time.time()
        self.target_time = self.current_time + self.tick_time_seconds

    def update_tick_time_ms(self, tick_time_ms: float) -> None:
        self.tick_time_seconds = tick_time_ms * 0.001

    def block_until_next_tick(self) -> None:
        while self.current_time < self.target_time:
            self.current_time = time.time()
            time.sleep(0.001)
        self.target_time += self.tick_time_seconds


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


# algorithm for a euclidean sequence, blackbox
def euclidean_rhythm(beats, pulses):
    rests = beats - pulses
    result = [1] * pulses
    pivot = 1
    interval = 2

    while rests > 0:
        if pivot > len(result):
            pivot = 1
            interval += 1

        result.insert(pivot, 0)

        pivot += interval
        rests -= 1

    return result


# function that makes the sequence (for example [1, 0, 0, 1, 0, 1, 0])
def make_sequence(beats, pulses):
    euclidean_sequence = euclidean_rhythm(beats, pulses)
    sequence_len = len(euclidean_sequence)
    rhythm = []

    # hihat on every tick
    for i in range(sequence_len):
        rhythm.append(make_event(i, hihat, "hihat"))

    # play a kick on the 1
    for index, item in enumerate(euclidean_sequence):
        if item == 1:
            rhythm.append(make_event(index, kick, "kick"))
        if item == random.choice([0, 2]):
            rhythm.append(make_event(index, snare, "snare"))

    return rhythm


# function that plays the sequence in a loop
def play_sequence():
    global sequence
    clock = Clock(tick_time_ms)
    clock.start()

    while True:
        for i in range(beats):
            i = (i + 1) % beats

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
beats, p = 16, 4
sequence = make_sequence(beats, p)
play_sequence()
