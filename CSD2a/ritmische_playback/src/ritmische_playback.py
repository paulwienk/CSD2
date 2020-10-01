import time
import os
import simpleaudio as sa

path = os.path.basename(__file__)
path = __file__.replace(path, 'kick.wav')


# gives the number of times the file is being played
try:
    num_playback_times = input("How many times would you like to hear the audio: ")
    num_playback_times = int(num_playback_times)

# gives error when input is not an integer or not exactly 1 number
except ValueError:
    print("Wrong input")
    exit()


# gives the note durations as a float 
try:
    note_duration = input('Enter note durations seperated by spaces: ').split(' ')
    note_duration = [float(n) for n in note_duration]


# gives error when input is not a float or int
except ValueError:
    print("Wrong input")
    exit()


try:
    bpm = input("What is the BPM?: ")
    bpm = int(bpm)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()


# time between sample in seconds
interval_time = [60 / bpm * i for i in note_duration]


for t in interval_time[:num_playback_times]:
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    time.sleep(t)








