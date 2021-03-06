# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


    # LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_PIN2        = 17      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)





class LedManager():

	strip1 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		# Intialize the library (must be called once before other functions).
	strip1.begin()
	for i in range(strip1.numPixels()):
		strip1.setPixelColor(i, Color(0,0,0))
	strip1.show()

	#strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		# Intialize the library (must be called once before other functions).
	#strip2.begin()
	#for i in range(strip2.numPixels()):
#		strip2.setPixelColor(i, Color(0,0,0))
#	strip2.show

	def blink1_3(self):
		self.blinkLed1()
		time.sleep(1)
		self.blinkLed1()
		time.sleep(1)
		self.blinkLed1()

	def blink2_3():
		self.blinkLed2()
		self.blinkLed2()
		self.blinkLed2()



	def blinkLed1(self):
		for i in range(LedManager.strip1.numPixels()):
			LedManager.strip1.setPixelColor(i, Color(250,0,0))
		LedManager.strip1.show()
		
		for i in range(LedManager.strip1.numPixels()):
			LedManager.strip1.setPixelColor(i, Color(0,0,0))
		LedManager.strip1.show()

	def blinkLed2():
		for i in range(LedManager.strip2.numPixels()):
			LedManager.strip2.setPixelColor(i, Color(250,0,0))
		LedManager.strip2.show()
		for i in range(LedManager.strip2.numPixels()):
			LedManager.strip2.setPixelColor(i, Color(0,0,0))
		LedManager.strip2.show()

	def colortrail(wait_ms=1000):

		# Create NeoPixel object with appropriate configuration.
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		# Intialize the library (must be called once before other functions).
		strip.begin()

		for i in range(strip.numPixels()):
			for j in range(i):
				strip.setPixelColor(j, Color(0,0,0))
				strip.show()
			strip.setPixelColor(i, Color(250,0,0))
			strip.show()
			time.sleep(wait_ms/1000.0)

	def colortrail2( wait_ms=200):
		# Create NeoPixel object with appropriate configuration.
		strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		# Intialize the library (must be called once before other functions).
		strip2.begin()
		for i in range(strip2.numPixels()):
			for j in range(i):
				strip2.setPixelColor(j, Color(0,0,0))
				strip2.show()
			strip2.setPixelColor(i, Color(250,0,0))
			strip2.show()
			time.sleep(wait_ms/1000.0)
