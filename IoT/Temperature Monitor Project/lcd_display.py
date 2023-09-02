from machine import Pin, Timer
import utime
from micropython_lcd import LCD

display = LCD()
display.init()

display.set_line(0)
display.set_string("Hello world!")
display.set_line(1)
display.set_string("I am Pi Pico!!")