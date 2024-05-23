#****************************
#Librerie necessaria
#****************************
import network
from machine import Pin
import BlynkLib
import time
#****************************
#Configurazione Connessione
#****************************
timeout = 0 # WiFi Connection Timeout variable 

wifi = network.WLAN(network.STA_IF)

# Restarting WiFi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect("Vodafone-A56173671", "NGFKAXPRb4CyPqbR")

if not wifi.isconnected():
    print('connecting..')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if(wifi.isconnected()):
    print('Connected...')
    print('network config:', wifi.ifconfig())
#****************************
#Configurazione Blynk
#****************************
auth = "srmKKN4zNmg7gIcGpDefBU8cg9Ki2KCj"
#auth = "FF0XUb8mQ7G5AhFQfvvnVWK7Ge9lGmOB"
blynk = BlynkLib.Blynk(auth)

ledp = 22

led = Pin(ledp, Pin.OUT)

@blynk.on("V0")
def v2_h(value):
    if int(value[0] == 1):
         led.value(1)
    else:
        led.value(0)
        
while True:
    blynk.run()