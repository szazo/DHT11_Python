import RPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 5
instance = dht22.DHT22(pin=5)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %f C" % result.temperature)
        print("Humidity: %f %%" % result.humidity)

    time.sleep(1)
