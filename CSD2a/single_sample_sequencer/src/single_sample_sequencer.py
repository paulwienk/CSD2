import time
import os


path = os.path.basename(__file__)
path = __file__.replace(path, 'kick.wav')

bpm = 90

try:
    bpm_change = input("The BPM is 90. Would you like to change it (yes/no): ")
    bpm_change = str(bpm_change)
    if bpm_change == "yes":
        try:
            bpm = input("What BPM?: ")
            bpm = int(bpm)

        except ValueError:
            print("This isn't a number.")
            exit()


# gives error when input is not a string
except ValueError:
    print("This isn't a string.")
    exit()

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


# set durations (0.25, 0.5, 1 for example) to timestamps (0, 1, 3, 7 for example)
def durations_to_timestamps(durations):
    added = [i * 4 for i in durations]

    answer = [0]
    for i in added:
        answer.append(i + answer[- 1])

    return answer


timestamps_list = durations_to_timestamps(note_duration)

# get the difference between elements in timestamp_list
timestamps_difference = [j - i for i, j in zip(timestamps_list[:-1], timestamps_list[1:])]


# set timestamps (0, 1, 3, 7 for example) to time in milliseconds
def timestamps_to_ms(timestamps):
    ms = [(i * 0.25) * 60 / bpm for i in timestamps]

    answer = [0]
    for i in ms:
        answer.append(i + answer[- 1])

    return answer


timestamps_answer = timestamps_to_ms(timestamps_difference)

# get the difference between elements in timestamps_answer (in milliseconds) for the playback in time.sleep
timestamps_answer_difference = [j - i for i, j in zip(timestamps_answer[:-1], timestamps_answer[1:])]

print(timestamps_answer)

for t in timestamps_answer_difference[:num_playback_times]:
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    time.sleep(t)
