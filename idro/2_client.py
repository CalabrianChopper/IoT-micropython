import tkinter as tk
import requests
import json

# Funzione per accendere il LED
def turn_on_led():
    try:
        requests.get("http://192.168.4.1/?LED=1")
        update_data()
    except requests.exceptions.RequestException as e:
        print("Errore durante l'accensione del LED:", e)

# Funzione per spegnere il LED
def turn_off_led():
    try:
        requests.get("http://192.168.4.1/?LED=0")
        update_data()
    except requests.exceptions.RequestException as e:
        print("Errore durante lo spegnimento del LED:", e)

# Funzione per aggiornare i dati di temperatura, umidità e stato del LED
def update_data():
    try:
        response = requests.get("http://192.168.4.1/data")
        data = response.json()
        temperature_label.config(text=f"Temperatura: {data['temperature']} °C")
        humidity_label.config(text=f"Umidità: {data['humidity']} %")
        led_state_label.config(text=f"LED: {data['led_state']}")
    except requests.exceptions.RequestException as e:
        print("Errore durante l'aggiornamento dei dati:", e)

# Creazione della finestra principale
root = tk.Tk()
root.title("Controllo LED e Sensori ESP32")

# Etichetta della temperatura
temperature_label = tk.Label(root, text="Temperatura: -- °C")
temperature_label.pack(pady=5)

# Etichetta dell'umidità
humidity_label = tk.Label(root, text="Umidità: -- %")
humidity_label.pack(pady=5)

# Etichetta dello stato del LED
led_state_label = tk.Label(root, text="LED: --")
led_state_label.pack(pady=5)

# Pulsante per accendere il LED
led_on_button = tk.Button(root, text="Accendi LED", command=turn_on_led)
led_on_button.pack(pady=5)

# Pulsante per spegnere il LED
led_off_button = tk.Button(root, text="Spegni LED", command=turn_off_led)
led_off_button.pack(pady=5)

# Pulsante per aggiornare i dati
update_button = tk.Button(root, text="Aggiorna Dati", command=update_data)
update_button.pack(pady=5)

# Avvio della finestra principale
root.mainloop()
