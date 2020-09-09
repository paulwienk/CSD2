import os
import simpleaudio as sa
path = os.path.basename(__file__)
path = __file__.replace(path, 'kick.wav')

# asks for the number of times the file is being played
try: 
    num_times = input ("How many times would you like to hear the audio: ")
    num_times = int(num_times)

# gives error when input is not an integer
except ValueError:
    print("This isn't a number.")
    
# plays the file the number of times given
for x in range(num_times):
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()