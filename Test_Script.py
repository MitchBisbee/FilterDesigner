import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define a function to update the plot based on the input values
def update_plot(fig, xdata, ydata, ax, canvas):
    ax.clear()
    ax.plot(xdata, ydata)
    canvas.draw()

# Create a new Tkinter window
root = tk.Tk()
root.title("Tab Bar with Matplotlib Plot and Data Input Boxes")

# Create a tab bar
tab_bar = ttk.Notebook(root)
tab_bar.grid(row=0, column=0, sticky='nsew')

# Create the first tab
tab1_frame = tk.Frame(tab_bar)
tab_bar.add(tab1_frame, text='Tab 1')

# Create input boxes for the first tab
xdata_entry1 = tk.Entry(tab1_frame)
xdata_entry1.grid(row=1, column=0)
ydata_entry1 = tk.Entry(tab1_frame)
ydata_entry1.grid(row=2, column=0)
update_button1 = tk.Button(tab1_frame, text='Update Plot', command=lambda: update_plot(fig1, xdata, ydata, ax1, canvas1))
update_button1.grid(row=3, column=0)

# Create a Matplotlib figure and plot on the first tab
fig1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = fig1.add_subplot(111)
xdata = [1, 2, 3, 4, 5]
ydata = [10, 5, 20, 30, 10]
ax1.plot(xdata, ydata)
canvas1 = FigureCanvasTkAgg(fig1, master=tab1_frame)
canvas1.get_tk_widget().grid(row=0, column=1, rowspan=4, sticky='nsew')

# Create the second tab
tab2_frame = tk.Frame(tab_bar)
tab_bar.add(tab2_frame, text='Tab 2')

# Create input boxes for the second tab
xdata_entry2 = tk.Entry(tab2_frame)
xdata_entry2.grid(row=1, column=0)
ydata_entry2 = tk.Entry(tab2_frame)
ydata_entry2.grid(row=2, column=0)
update_button2 = tk.Button(tab2_frame, text='Update Plot', command=lambda: update_plot(fig2, xdata, ydata, ax2, canvas2))
update_button2.grid(row=3, column=0)

# Create a Matplotlib figure and plot on the second tab
fig2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = fig2.add_subplot(111)
xdata = [1, 2, 3, 4, 5]
ydata = [5, 30, 10, 20, 10]
ax2.plot(xdata, ydata)
canvas2 = FigureCanvasTkAgg(fig2, master=tab2_frame)
canvas2.get_tk_widget().grid(row=0, column=1, rowspan=4, sticky='nsew')

# Configure the grid weights
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
tab1_frame.rowconfigure(0, weight=1)
tab1_frame.columnconfigure(0, weight=1)
tab2_frame.rowconfigure(0, weight=1)
tab2_frame.columnconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()
