from __future__ import print_function
import time
import board
import ssl
import time
import sys

import paho.mqtt.client as mqtt
import uuid

# SPDX-FileCopyrightText: Copyright (c) 2022 Edrig
#
# SPDX-License-Identifier: MIT
import board
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
"""
	Reading distance from the laser based VL53L1X
	This example prints the distance to an object. If you are getting weird
	readings, be sure the vacuum tape has been removed from the sensor.
"""
def change_dB(raw_data):
	return raw_data*2

def change_Hz(raw_data):
	max_hz = 22000
	return abs(max_hz/raw_data)


def runExample():
	## Gyro and accelaromator
	i2c = board.I2C()  # uses board.SCL and board.SDA
	sensor = LSM6DS3(i2c)

	## JOYSTICK
	"""
	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()

	if myJoystick.connected == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.version)
	"""

    ## MQTT
	client = mqtt.Client(str(uuid.uuid1()))
	client.tls_set(cert_reqs=ssl.CERT_NONE)
	client.username_pw_set('idd', 'device@theFarm')

	client.connect('farlab.infosci.cornell.edu', port=8883)

	topic_heartbeat = 'IDD/IntoOto/Heartbeat'
	topic_gyro = 'IDD/IntoOto/Gyro'

	while True:
		ax, ay, az = sensor.acceleration
		gx, gy, gz = sensor.gyro
		client.publish(topic_gyro, '{:.1f} {:.1f}'.format(change_dB(ax), change_Hz(ay)))

        #print("ax: {:10.4f}, ay: {:10.4f}, az: {:10.4f}".format(ax, ay, az))
		#print("ax: {:10.4f}, ay: {:10.4f}, az: {:10.4f}, gx: {:10.4f}, gy: {:10.4f}, gz: {:10.4f}".format(ax, ay, az, gx, gy, gz))

		"""
		if myJoystick.button == 0:
			print('pushed')
			client.publish(topic_heartbeat, '108')
		"""
		time.sleep(.2)

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)