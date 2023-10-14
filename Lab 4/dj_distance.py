# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 
 
# Import an audio file 
# Format parameter only
# for readability 
wav_file = AudioSegment.from_file(file = "Sample.wav", 
                                  format = "wav") 
 
# Play the audio file
play(wav_file)