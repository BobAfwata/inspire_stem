import machine
import dht
import time
import ujson
import ubluetooth

# Initialize DHT sensor
dht_pin = machine.Pin(2, machine.Pin.IN)
dht_sensor = dht.DHT11(dht_pin)

# Bluetooth initialization
bt = ubluetooth.BLE()

def read_sensor_data():
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return {'temperature': temp, 'humidity': humidity}

# Function to send sensor data over Bluetooth
def send_sensor_data():
    data = read_sensor_data()
    serialized_data = ujson.dumps(data)
    print("Sending data:", serialized_data)
    bt.gatts_notify(0, 1, serialized_data)

while True:
    send_sensor_data()
    time.sleep(2)  # Adjust the delay based on your needs

