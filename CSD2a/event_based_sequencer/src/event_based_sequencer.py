import simpleaudio as sa
import time


# loading samples
hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")

# define BPM
try:
    bpm = input("What is the BPM?: ")
    bpm = int(bpm)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()

# converts given BPM in MS
bpm_in_ms = (60000 / bpm) * 0.5


# timing class written by Wouter Ensink
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


# makes the event with arguments timestamp, instrument and the name of the instrument
def make_event(timestamp, instrument, instrumentname):
    return {
        'timestamp': timestamp,
        'instrument': instrument,
        'instrumentname': instrumentname,
    }


# makes the sequence (hard coded)
def make_sequence():
    rhythm = [make_event(0, kick, "kick"),
              make_event(2, snare, "snare"),
              make_event(4, kick, "kick"),
              make_event(6, snare, "snare"),
              make_event(8, kick, "kick"),
              make_event(9, kick, "kick"),
              make_event(10, snare, "snare"),
              make_event(11, kick, "kick"),
              make_event(12, kick, "kick"),
              make_event(14, snare, "snare")]

    # hihat on every tick
    for i in range(16):
        rhythm.append(make_event(i, hihat, "hihat"))

    # sorting the timestamps
    rhythm.sort(key=lambda x: x['timestamp'])

    return rhythm


# handles event
def handle_event(event):
    event['instrument'].play()


# function to print the sequence in the right order
def print_sequence(sequence):
    sequence.sort(key=lambda x: x['timestamp'])
    print('\n'.join(f'{e}' for e in sequence))


# function to play the sequence with the right time interval
def play_sequence(sequence):
    clock = Clock(bpm_in_ms)
    clock.start()
    for i in range(16):
        for e in sequence:
            if e['timestamp'] == i:
                handle_event(e)
        clock.block_until_next_tick()


sequence = make_sequence()
print_sequence(sequence)
play_sequence(sequence)
