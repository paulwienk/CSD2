import os
import simpleaudio as sa

print(f'{os.getcwd()}/{__file__}')
wave_obj = sa.WaveObject.from_wave_file("D:\hku\jaar2\CSD2\python_basics\kick.wav")
play_obj = wave_obj.play()
play_obj.wait_done()