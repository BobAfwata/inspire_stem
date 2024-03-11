# pip install ujson

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import ujson

window = Tk()

window.title("DHT11 Sensor Data")
window.geometry('600x400')

# Matplotlib figure for plotting
fig, ax = plt.subplots()
line_temp, = ax.plot([], [], label='Temperature')
line_humidity, = ax.plot([], [], label='Humidity')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Value')
ax.legend()

# Tkinter canvas for embedding matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=1, columnspan=2)

# Function to update the plot with new data
def update_plot(ser):
    try:
        line = ser.readline().decode('utf-8').rstrip()
        data = ujson.loads(line)
        times.append(time.time() - times[0])
        temperatures.append(data['temperature'])
        humidities.append(data['humidity'])
        line_temp.set_xdata(times)
        line_temp.set_ydata(temperatures)
        line_humidity.set_xdata(times)
        line_humidity.set_ydata(humidities)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()
    except Exception as e:
        print(f"Error updating plot: {e}")

# Tkinter label for displaying current values
lbl = Label(window, text="Temperature: \nHumidity: ")
lbl.grid(column=0, row=0)

# Button to start receiving data
ser = serial.Serial('COM3', 115200)  # Change the port accordingly
times = [0]
temperatures = [0]
humidities = [0]

def start_reading():
    while True:
        update_plot(ser)

# Button to trigger data reception
btn = Button(window, text="Start Reading", command=start_reading)
btn.grid(column=0, row=2, columnspan=2)

window.mainloop()
