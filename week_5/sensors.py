import machine
import dht
import time
import ujson
import ubluetooth

# Define DHT11 pin
dht_pin = machine.Pin(2, machine.Pin.IN)

# Define Bluetooth characteristics
bt_uart = ubluetooth.UART(1, 115200)

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
    bt_uart.write(ujson.dumps(data) + '\n')
    time.sleep(2)  # Adjust the delay based on your needs
