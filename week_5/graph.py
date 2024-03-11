# pip install matplotlib
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random

window = Tk()

window.title("Sensors")
window.geometry('600x400')

times = [0]
temperatures = [68]  # Initial temperature

# Matplotlib figure for plotting
fig, ax = plt.subplots()
line, = ax.plot(times, temperatures)
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Temperature')
ax.set_ylim(50, 100)  # Set y-axis limits

# Tkinter canvas for embedding matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=1, columnspan=2)

# Tkinter label for displaying current temperature
lbl = Label(window, text="Temperature: {}".format(temperatures[-1]))
lbl.grid(column=0, row=0)

def update_plot():
    # Generate a random temperature between 50 and 100
    new_temp = random.uniform(50, 100)
    
    # Get the current time in seconds
    current_time_seconds = time.time() - times[0]
    
    # Update data
    times.append(current_time_seconds)
    temperatures.append(new_temp)
    
    # Update label
    lbl.configure(text="Temperature: {:.1f}".format(new_temp))
    
    # Update plot
    line.set_xdata(times)
    line.set_ydata(temperatures)
    
    # Adjust plot limits
    ax.relim()
    ax.autoscale_view()
    
    # Redraw canvas
    canvas.draw()
    
    # Introduce a delay for a smoother graph
    time.sleep(0.1)  # Adjust the sleep duration as needed

# Button to trigger temperature update
btn = Button(window, text="Update Temperature", command=update_plot)
btn.grid(column=0, row=2, columnspan=2)

window.mainloop()
