import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import numpy as np

root = Tk()
root.title('Parabolic Function')
root.resizable(False, False)
root.geometry("500x500")

def plot():
    
	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),
				dpi = 100)
    
	# list of squares
	y = [i**2 for i in range(101)]
    
	# adding the subplot
	plot1 = fig.add_subplot(111)
    
	# plotting the graph
	plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,
							master = root)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,
								root)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()

plot_button = tk.Button(master = root,
					command = plot,
					height = 2,
					width = 10,
					text = "Plot")

plot_button.pack()

#plot_save csv
plot_csv = tk.Button(master= root,
                  command= plot,
                  height=2,
                  width=5,
                  text= "Simpan OUTPUT")
plot_csv.pack()

root.mainloop()