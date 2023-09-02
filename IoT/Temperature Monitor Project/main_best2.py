import anvil.pico
import uasyncio as a
from machine import Pin, I2C
from utime import sleep
from dht20 import DHT20
from micropython_lcd import LCD



@anvil.pico.callable(is_async=True)
async def pico_fn(n):
    # Output will go to the Pico W serial port
    print(f"Called local function with argument: {n}")

    # Blink the LED and then double the argument and return it.
    for i in range(10):
        led.toggle()
        await a.sleep_ms(150)

    temperature = measurements['t']
    # We use the LED to indicate server calls and responses.
    return temperature


async def connect():
    anvil.pico.connect(UPLINK_KEY)
    

async def show_data():
    while True:
        display.set_line(0)
        display.set_string(f"Temp: {measurements['t']:0.2f} C")
        display.set_line(1)
        display.set_string(f"Humi: {measurements['rh']:0.2f} %RH")
        await a.sleep_ms(1000)  # Pause 1s
        

async def main():

    # Set up DHT20
    i2c0_sda = Pin(8)
    i2c0_scl = Pin(9)
    i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
    dht20 = DHT20(0x38, i2c0)
    measurements = dht20.measurements

    # Set up LCD
    display = LCD()
    display.init()

    # Set up Pico
    led = Pin("LED", Pin.OUT, value=1)
    UPLINK_KEY = "server_WKLM5FBVV7HHV6QJEBK5DVLU-BW6F2ZC6GB3WGN2C"

    a.create_task(show_data())
    print(f"Temperature: {measurements['t']} °C, humidity: {measurements['rh']} %RH")
    a.create_task(connect())
    
a.run(main())






