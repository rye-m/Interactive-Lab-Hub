#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qwiic_proximity_ex1.py
#
# Simple Example for the Qwiic Proximity Device
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2019
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 1
#
# - Setup the device
# - Output the proximity value
from __future__ import print_function
import numpy
import time
import sys
from aupyom import Sampler, Sound
from aupyom.util import example_audio_file

# SPDX-FileCopyrightText: Copyright (c) 2022 Edrig
#
# SPDX-License-Identifier: MIT
import board
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3


def runExample():

    #load sound
    sampler = Sampler()
    s1 = Sound.from_file("./music/techno120.mp3")
    sampler.play(s1)
	
    # start sensoring
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sensor = LSM6DS3(i2c)


    # Creeate sound
    freq = 440.0
    sr = 22050
    t = 10.0

    #s2 = Sound(numpy.sin(2 * numpy.pi * freq * numpy.linspace(0, t, sr * t)), sr)
    #sampler.play(s1)

    while True:
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro

        #print("ax: {:10.4f}, ay: {:10.4f}, az: {:10.4f}".format(ax, ay, az))
        print("ax: {:10.4f}, ay: {:10.4f}, az: {:10.4f}, gx: {:10.4f}, gy: {:10.4f}, gz: {:10.4f}".format(ax, ay, az, gx, gy, gz))

        
        # Accelameter
        # Pitch
        if ax <= -3:
            s1.pitch_shift = -5
        elif ax <= 3:
            s1.pitch_shift = 0
        else:
            s1.pitch_shift = +5
        
        # Speed
        if ay <= -5:
            s1.stretch_factor = 0.5
        elif ay <= 5:
            s1.stretch_factor = 1.0
        else:
            s1.stretch_factor = 1.5
        """
        # Volume
        if ay <= 3:
            s1.pitch_shift = 10
        elif ay <= 5:
            s1.pitch_shift = 0
        else:
            s1.pitch_shift = -10
        
        #Gyro
        # Pitch
        if gx <= 3:
            s1.pitch_shift = -5
        elif gx <= 5:
            s1.pitch_shift = 0
        else:
            s1.pitch_shift = +5
        
        # Speed
        if gy <= -0.5:
            s1.stretch_factor = 0.5
        elif gy <= 0.5:
            s1.stretch_factor = 1.0
        else:
            s1.stretch_factor = 1.5
        
        # Volume
        if ay <= 3:
            s1.pitch_shift = 10
        elif ay <= 5:
            s1.pitch_shift = 0
        else:
            s1.pitch_shift = -10
        """
        time.sleep(.2)

if __name__ == "__main__":

    print("Program has just started.")
    runExample()

