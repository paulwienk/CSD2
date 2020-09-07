from pydub import AudioSegment
from pydub.playback import play

file_name = "kick.wav"

# ask for the file name (has to be in the right folder)
file_text = input ("What file would you like to play: ")
file_name = str(file_text)


# asks for the number of times the file is being played
try: 
    test_text = input ("How many times would you like to hear the audio: ")
    test_number = int(test_text)

except ValueError:
    print("This isn't a number.")

n = test_number

# plays audio the exact number of times you gave as the input
audio = AudioSegment.from_file(file_name)
play(audio * n) 

