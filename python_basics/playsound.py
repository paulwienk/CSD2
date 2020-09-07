import os
import simpleaudio as sa
path = os.path.basename(__file__)
path = __file__.replace(path, 'kick.wav')

wave_obj = sa.WaveObject.from_wave_file(path)
play_obj = wave_obj.play()
play_obj.wait_done()