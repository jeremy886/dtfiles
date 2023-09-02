from machine import Pin, Timer
import utime
from micropython_lcd import LCD
from dht20 import DHT20, I2C


# Code for DHT20
i2c0_sda = Pin(8)
i2c0_scl = Pin(9)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
dht20 = DHT20(0x38, i2c0)

# Code for LCD
display = LCD()
display.init()

while True:
    measurements = dht20.measurements
    # print(f"Temperature: {measurements['t']} °C, humidity: {measurements['rh']} %RH")
    display.set_line(0)
    display.set_string(f"Temp: {measurements['t']:0.2f} C")
    display.set_line(1)
    display.set_string(f"Humi: {measurements['rh']:0.2f} %RH")
    utime.sleep(1)
    



