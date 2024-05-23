from machine import Pin, SoftI2C
import dht
import time
import ssd1306

#Protocollo: I2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled = ssd1306.SSD1306_I2C(128, 32, i2c)

sensor_data = dht.DHT11(Pin(15))

def call_dht():
    sensor_data.measure()
    temp = sensor_data.temperature()
    hum = sensor_data.humidity()
    print("Temperature - ", temp, "Humidity - ", hum)
    .21
    
while True:
    call_dht()
    oled.text("ciao", 0, 0)
    oles.text(str(temp), 0, 0
    oled.show()
    time.sleep(20)

