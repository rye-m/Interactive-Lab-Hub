# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 
import qwiic
import time
"""
# Setting up the sensor
print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")
"""
# Import an audio file 
sound = AudioSegment.from_file(file = "music/Time2Shine.wav", 
                                  format = "wav") 

"""
while True:
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		ToF.stop_ranging()

		distanceInches = distance / 25.4
		distanceFeet = distanceInches / 12.0

		if 0 <= distance < 80:
			octaves = -0.5
		elif 80 <= distance <160:
			octaves = +0
		else :
			octaves = +0.5

		new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
		sound_lowpitch = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

		# Play the audio file
		play(sound)
	
		print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))

	except Exception as e:
		print(e)
		
"""

# Change speed
sound_2x = sound.speedup(playback_speed=2.0, crossfade=0)

# Shift the pitch
octaves = -0.5
new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
sound_lowpitch = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

 
# Play the audio file
play(sound)