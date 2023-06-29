import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import numpy as np


GRAVITASI = 9.8
KECEPATAN_TEMBAK = 0.0
SUDUT = 0.0

root = Tk()
root.title('Parabolic Function')
root.resizable(False, False)
root.geometry("750x750")



def KETINGGIAN_MAX(KECEPATAN_TEMBAK, SUDUT):
    #rumus masih ngasal
    KM_result = (KECEPATAN_TEMBAK**2 * (np.sin(np.radians(SUDUT))**2)) / 2*GRAVITASI
    return KM_result

def JARAK_MAX(KECEPATAN_TEMBAK, SUDUT):
    #rumus ngasal banget
    JM_result = (KECEPATAN_TEMBAK**2 * np.sin(2*np.radians(SUDUT))) / GRAVITASI
    return JM_result


# Membuat label dan input untuk kecepatan awal
label_kecepatan = tk.Label(root, text="kecepatan tembak (m/s):")
label_kecepatan.pack()
entry_velocity = tk.Entry(root)
entry_velocity.pack()



# Membuat label dan input untuk sudut
label_sudut_tembak = tk.Label(root, text="sudut tembak (degrees):")
label_sudut_tembak.pack()
entry_sudut_tembak = tk.Entry(root)
entry_sudut_tembak.pack()

#result tab
KM_res = tk.Label(root, text= "Kecepatan Max")
KM_res.pack()
KM_entry = tk.Entry(root)
KM_entry.pack()

JM_res = tk.Label(root, text= "Jarak Maksimum")
JM_res.pack()
JM_entry = tk.Entry(root)
JM_entry.pack()



def OUTPUT():
    # CSV data ------------------------------------------------------------------------------------------------
    print("haii")

def plot():
    # Result of calculation code ------------------------------------------------------------------------------
    KECEPATAN_TEMBAK = float(entry_velocity.get())
    SUDUT = float(entry_sudut_tembak.get())
    
    KM_results = KETINGGIAN_MAX(KECEPATAN_TEMBAK, SUDUT)
    KM_label = tk.Label(root, text=f"Max height: {KM_results:.2f}")    

    KM_label.pack()
    KM_entry.delete(0, END)
    KM_entry.insert(0,KM_results)
    
    JM_results = JARAK_MAX(KECEPATAN_TEMBAK, SUDUT)
    JM_label = tk.Label(root, text=f"Max distance: {JM_results:.2f}")
    
    JM_label.pack()
    JM_entry.delete(3, END)
    JM_entry.insert(3,JM_results)

    CalcRes = [KM_results, JM_results]
    
    # Plotting CODE --------------------------------------------------------------------------------------------
    fig = Figure(figsize=(5,5), dpi=100)
    
    x = np.linspace(0, 10, 1000)
    y = KECEPATAN_TEMBAK * np.sin(np.radians(SUDUT)) * (x - 0.5) * GRAVITASI * (x ** 2)
    # y= x**2 + 2*x + 2

    plot1 = fig.add_subplot(111)
    plot1.plot(x,y, color= 'b')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    canvas.get_tk_widget().pack()

    return CalcRes

# plot button
plot_button = tk.Button(master = root,
					command = plot,
					height = 2,
					width = 10,
					text = "Result")

plot_button.pack()

#plot_save csv
plot_csv = tk.Button(master= root,
                  command= OUTPUT,
                  height=2,
                  width=10,
                  text= "Simpan OUTPUT")
plot_csv.pack()

root.mainloop()