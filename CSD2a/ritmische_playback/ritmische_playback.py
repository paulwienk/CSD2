import time
import os
import simpleaudio as sa
path = os.path.basename(__file__)
path = __file__.replace(path, 'kick.wav')

# gives the number of times the file is being played
try: 
    num_playback_times = input("How many times would you like to hear the audio: ")
    num_playback_times = int(num_playback_times)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")


# gives the note durations as a float 
try: 
    note_duration = input('Enter note durations seperated by spaces: ').split(' ') 
    note_duration = [float(n) for n in note_duration] 

# gives error when input is not a float or int
except ValueError:
    print("This isn't a number.")
    exit()


print(note_duration)

try: 
    bpm = input ("What is the BPM?: ")
    bpm = int(bpm)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    exit()

# de interval tijd in sec
for i in note_duration:
    interval_time = 60 / bpm * i
    print(interval_time)

'''
while True:
	for t in note_duration:
		print(t)
		time.sleep(interval_time)




# plays the file the number of times given
for i in range(num_playback_times):
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

'''
