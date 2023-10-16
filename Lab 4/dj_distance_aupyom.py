from aupyom import Sampler, Sound
from aupyom.util import example_audio_file
import time

sampler = Sampler()

audio_file = "music/Time2Shine.wav"
s1 = Sound.from_file(audio_file)

sampler.play(s1)

time.sleep(5)
s1.pitch_shift = 5
print('pitch shifted')

time.sleep(5)
s1.pitch_shift = 15
print('pitch shifted')

time.sleep(5)
s1.pitch_shift = -8
print('pitch shifted')

