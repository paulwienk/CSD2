import simpleaudio as sa
import time
import random
from threading import Thread

hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")

# ask for bpm with error handling

bpm = 90


def bpm_to_ms(bpm):
    return (60000 / bpm) * 0.5


# converts given BPM in MS
tick_time_ms = bpm_to_ms(bpm)

'''
def input_bpm():
    global tick_time_ms
    while True:
        try:
            bpm = int(input("What is the BPM?: "))
            tick_time_ms = bpm_to_ms(bpm)

        # gives error when input is not an integer
        except ValueError:
            print("This isn't a number. Try again")
            continue

        else:
            break


# ask for number of beats with error handling
def input_beats():
    while True:
        try:
            euclidean_beats = int(input("How many beats? "))
            if euclidean_beats <= 0:
                print("Number of beats can't be 0. Try again.")
                continue

        # gives error when input is not an integer
        except ValueError:
            print("This isn't a number. Try again")
            continue

        else:
            break


euclidean_beats = 16


# ask for number of pulses with error handling
def input_pulses():
    while True:
        try:
            euclidean_pulses = int(input("How many pulses? "))
            if euclidean_pulses <= 0:
                print("Number of pulses can't be 0. Try again.")
                continue
            if euclidean_beats < euclidean_pulses:
                print("Number of beats has to be higher than the number of pulses. Try again.")
                continue

        # gives error when input is not an integer
        except ValueError:
            print("This isn't a number. Try again.")
            continue

        else:
            break


euclidean_pulses = 4
'''


def handle_next_command():
    global sequence, tick_time_ms, beats
    command = input(' -> ')
    # make 16 5
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


def make_event(timestamp, instrument, instrumentname):
    return {
        'timestamp': timestamp,
        'instrument': instrument,
        'instrumentname': instrumentname,
    }


def handle_event(event):
    event['instrument'].play()


# algorithm for a euclidean sequence
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


def make_sequence(beats, pulses):
    euclidean_sequence = euclidean_rhythm(beats, pulses)
    sequence_len = len(euclidean_sequence)
    rhythm = []

    # hihat on every tick
    for i in range(sequence_len):
        rhythm.append(make_event(i, hihat, "hihat"))

    for index, item in enumerate(euclidean_sequence):
        if item == 1:
            rhythm.append(make_event(index, kick, "kick"))
        if item == random.choice([0, 2]):
            rhythm.append(make_event(index, snare, "snare"))

    return rhythm


def play_sequence():
    global sequence
    clock = Clock(tick_time_ms)
    clock.start()
    '''print(euclidean_sequence)'''
    

    while True:
        for i in range(beats):
            i = (i + 1) % beats
            '''if i == 0:
                print(euclidean_sequence)'''

            for e in sequence:
                if e['timestamp'] == i:
                    handle_event(e)

            clock.update_tick_time_ms(tick_time_ms)
            clock.block_until_next_tick()
           
            


def user_interface_thread():
    while True:
        handle_next_command()


t = Thread(target=user_interface_thread)
t.start()
beats, p = 16, 4
sequence = make_sequence(beats, p)
play_sequence()
