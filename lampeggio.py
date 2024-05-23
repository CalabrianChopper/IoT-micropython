import machine
import time

LED = machine.Pin(22, machine.Pin.OUT)

while True:
    LED.value(1)
    time.sleep(1)
    LED.value(0)
    time.sleep(1)