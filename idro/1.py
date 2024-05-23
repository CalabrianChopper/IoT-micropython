#****************************
#Librerie necessaria
#****************************
import network
from machine import Pin
import time
import socket
import dht
#****************************
#Configurazione LED
#****************************
led = Pin(22, Pin.OUT)
led.off()
#****************************
#Configurazione Access Point
#****************************
ssid = "ESP32_AP_SUCA"
password = "123456789"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = ssid, password = password)
while not ap.active():
    pass

print("Configurazione", ap.ifconfig())
#print("IP a cui connettersi: ", ap.ifconfig([0]))
#****************************
#Configurazione Socket Comun.
#AF_INET usa IPv4
#SOCK_STREAM usa TCP
#SOCK_DGRAM usa UDP
#****************************
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 80))
s.listen(5)
#****************************
#Configurazione DHT11
#****************************
global d
d = dht.DHT11(Pin(23))
time.sleep(5) 
#****************************
#Funzione Web Page
#****************************
def web_page():
    for i in range(5):  # Prova fino a 5 volte
        try:
            d.measure()
            break  
        except OSError as e:
            print("Errore al tentativo {}: {}".format(i + 1, e))
            time.sleep(2)  
    t = d.temperature()
    h = d.humidity()
    
    if led.value()==1:
        led_state = 'ON'
        print('led is ON')
    elif led.value()==0:
        led_state = 'OFF'
        print('led is OFF')
        
    html_page = """   
    <html>   
        <head>   
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="refresh" content="1">
        </head>   
        <body>   
            <center><h2>ESP32 Web Server in MicroPython </h2></center>   
            <center>   
                <form>   
                     <button type='submit' name="LED" value='1'> LED ON </button>   
                     <button type='submit' name="LED" value='0'> LED OFF </button>   
                </form>
            <center><h2>Temperatura e Umidità della tua torretta</h2></center>   
            <center><p>Temperature is <strong>""" + str(t) + """ C.</strong>.</p></center>   
            <center><p>Humidity is <strong>""" + str(h) + """ %.</strong>.</p></center>   
            </center>   
            <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>   
        </body>   
    </html>"""   
    return html_page  

while True:
    # Socket accept() 
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
    
    # Socket receive()
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OKn')
    conn.send('Content-Type: text/htmln')
    conn.send('Connection: close\n')
    conn.sendall(response)
    
    # Socket close()
    conn.close()