import network
from machine import Pin
import uasyncio

# Set up Wi-Fi access point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32')
ap.config(authmode=3, password='123456789')

while ap.active() == False:
    pass

print("Access Point active")
print("IP Address:", ap.ifconfig()[0])

# Define LED pin and state
led_pin = 22
led_state = False
led = Pin(led_pin, Pin.OUT)

def toggle_led():
    global led_state
    led_state = not led_state
    led.value(led_state)

async def http_server_handler(request):
    # Check if the request path is /toggle
    if request.path == '/toggle':
        await toggle_led()
        return f"LED toggled to {led_state}"
    
    # Default response for other paths
    return "Welcome to ESP32 LED Control!"

# Create a simple HTML response
html_response = """
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 LED Control</title>
</head>
<body>
    <h1>ESP32 LED Control</h1>
    <p><a href="/toggle">Toggle LED</a></p>
</body>
</html>
"""

async def http_server_handler(request):
    # Check if the request path is /toggle
    if request.path == '/toggle':
        await toggle_led()
        return f"LED toggled to {led_state}"
    
    # Serve the HTML content for other paths
    return html_response

# Set up HTTP server
server = None
def start_http_server(server_address="0.0.0.0", port=80):
    global server
    server = await uasyncio.start_server(http_server_handler, server_address, port)

# Start the server in a separate coroutine
uasyncio.create_task(start_http_server())

while True:
    pass


async def http_server_handler(request):
    if request.path == '/toggle':
        await toggle_led()
        return f"LED toggled to {led_state}"

# Set up HTTP server
server = None
def start_http_server(server_address="0.0.0.0", port=80):
    global server
    server = await uasyncio.start_server(http_server_handler, server_address, port)

# Start the server in a separate coroutine
uasyncio.create_task(start_http_server())

while True:
    pass
