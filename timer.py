from machine import Pin, Timer

led = Pin(22, Pin.OUT)

timer = Timer(0)

timer.init(period=1000, mode=Timer.PERIODIC, callback = lambda t: led.value(not led.value()))

