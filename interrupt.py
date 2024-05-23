from machine import Timer, Pin

led = Pin(22, Pin.OUT)
but = Pin(0, Pin.OUT)

def buttons_irq():
    print("Triggered")
    
time = Timer(0)

timer.init(period=1000, mode=Timer.PERIODIC, callback = lambda t: led.value(not led.value()))

but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)