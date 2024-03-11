import machine
import dht
import time
import bluetooth

# Define DHT11 pin
dht_pin = machine.Pin(2, machine.Pin.IN)

# Define Bluetooth characteristics
bt = bluetooth.BLE()

# Function to read temperature and humidity from DHT11
def read_dht():
    d = dht.DHT11(dht_pin)
    d.measure()
    temp_c = d.temperature()
    humidity = d.humidity()
    return temp_c, humidity

# Main loop to read data and send via Bluetooth
while True:
    temp, humidity = read_dht()
    data = {'temperature': temp, 'humidity': humidity}
    
    # Send data as a JSON string
    bt.gatts_write(0, json.dumps(data))
    
    time.sleep(2)  # Adjust the delay based on your needs
