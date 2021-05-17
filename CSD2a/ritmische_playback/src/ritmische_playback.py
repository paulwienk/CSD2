import simpleaudio as sa
import time
import random

hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")

# ask for bpm with error handling

bpm = 90


def input_bpm():
    while True:
        try:
            bpm = int(input("What is the BPM?: "))

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

# converts given BPM in MS
bpm_in_ms = (60000 / bpm) * 0.5


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


euclidean_sequence = euclidean_rhythm(euclidean_beats, euclidean_pulses)
sequence_len = len(euclidean_sequence)


def make_sequence():
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


def play_sequence(sequence):
    clock = Clock(bpm_in_ms)
    clock.start()
    '''print(euclidean_sequence)'''

    while True:
        for i in range(sequence_len):
            i = (i + 1) % sequence_len
            '''if i == 0:
                print(euclidean_sequence)'''

            for e in sequence:
                if e['timestamp'] == i:
                    handle_event(e)

            clock.block_until_next_tick()


def print_sequence(sequence):
    print('\n'.join(f'{e}' for e in sequence))


input_bpm()
sequence = make_sequence()
play_sequence(sequence)
print_sequence(sequence)







