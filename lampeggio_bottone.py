from machine import Pin
import time

LED = machine.Pin(22, machine.Pin.OUT)
BUT = machine.Pin(0, machine.Pin.IN)

while True:
    but_status = BUT.value()
    if(but_status == False):
        LED.value(1)
    else:
        LED.value(0)