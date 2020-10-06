import sys
import threading
import time
import simpleaudio as sa

hihat = sa.WaveObject.from_wave_file("hihat.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
kick = sa.WaveObject.from_wave_file("kick.wav")


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


def make_event(timestamp, instrument, instrumentname):
    return {
        'timestamp': timestamp,
        'instrument': instrument,
        'instrumentname': instrumentname,
    }


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

    for i in range(16):
        rhythm.append(make_event(i, hihat, "hihat"))

    rhythm.sort(key=lambda x: x['timestamp'])

    return rhythm


def handle_event(event):
    event['instrument'].play()


print('\n'.join(f'{e}' for e in make_sequence()))


# bpm als argument meegeven??
def play_sequence(sequence):
    clock = Clock(500)
    clock.start()
    for i in range(16):
        for e in sequence:
            if e['timestamp'] == i:
                handle_event(e)
        clock.block_until_next_tick()


play_sequence(make_sequence())
