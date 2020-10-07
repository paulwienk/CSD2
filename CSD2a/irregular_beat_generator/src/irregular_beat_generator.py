import simpleaudio as sa
import time

hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")


try:
    bpm = input("What is the BPM?: ")
    bpm = int(bpm)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()

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


def make_sequence():
    rhythm = []

    # hihat on every tick
    for i in range(16):
        rhythm.append(make_event(i, hihat, "hihat"))

    # sorting the timestamps
    rhythm.sort(key=lambda x: x['timestamp'])

    return rhythm


def handle_event(event):
    event['instrument'].play()


try:
    euclidean_beats = input("How many beats? ")
    euclidean_beats = int(euclidean_beats)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()


try:
    euclidean_pulses = input("How many pulses? ")
    euclidean_pulses = int(euclidean_pulses)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()


def euclidean_rhythm(beats, pulses):
    if pulses is None or pulses < 0:
        pulses = 0
    if beats is None or beats < 0:
        beats = 0
    if pulses > beats:
        beats, pulses = pulses, beats
    if beats == 0:
        return []

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
print(euclidean_sequence)


def play_sequence(sequence):
    clock = Clock(bpm_in_ms)
    clock.start()
    for i in range(16):
        for e in sequence:
            if e['timestamp'] == i:
                handle_event(e)
        clock.block_until_next_tick()


sequence = make_sequence()
play_sequence(sequence)


