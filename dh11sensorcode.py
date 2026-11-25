from time import sleep
from machine import Pin
import dht
sensor = dht.DHT11(Pin(4))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp_c = sensor.temperature()
        humidity = sensor.humidity()
        temp_f = temp_c * (9 / 5) + 32

        print(f"Temperature: {temp_c} C ({temp_f:.1f} F) | Humidity: {humidity}%")
    except OSError:
        print("error")