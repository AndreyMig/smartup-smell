# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *





class LedManager():

    # LED strip configuration:
	LED_COUNT      = 60      # Number of LED pixels.
	LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
	LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
	LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
	LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
	LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


    def colortrail(strip, wait_ms=200):
		for i in range(strip.numPixels()):
			for j in range(i):
				strip.setPixelColor(j, Color(0,0,0))
				strip.show()
			strip.setPixelColor(i, Color(250,0,0))
			strip.show()
			time.sleep(wait_ms/1000.0)
