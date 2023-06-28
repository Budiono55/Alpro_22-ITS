import tkinter as tk
import csv
import matplotlib.pyplot as plt
import numpy as np

def calculate():
    try:
        # Mengambil nilai-nilai dari input
        kecepatan_tembak = float(entry_velocity.get())
        sudut_tembak = float(entry_sudut_tembak.get())
        gravitasi = 9.8
        
        # Menghitung ketinggian maksimum
        ketinggian_maksimum = (kecepatan_tembak**2 * np.sin(np.radians(sudut_tembak))) / 2*gravitasi #rumus masih ngasal
        
        # Menghitung jarak maksimum
        jarak_maksimum = (kecepatan_tembak ** 2 * np.sin(2 * np.radians(sudut_tembak))) / gravitasi #rumus masih ngasal
        
        # Menampilkan hasil pada label
        label_height.config(text=f"ketinggian maksimum: {ketinggian_maksimum:.2f} m")
        label_distance.config(text=f"jarak maksimum: {jarak_maksimum:.2f} m")
        
        # Membuat array jarak dan ketinggian
        jarak = np.linspace(0, ketinggian_maksimum, num=100)
        ketinggian = kecepatan_tembak * np.sin(np.radians(sudut_tembak)) * jarak - 0.5 * gravitasi * jarak ** 2
        
        # Membuat grafik
        plt.plot(jarak, ketinggian)
        plt.xlabel('jarak tempuh (m)')
        plt.ylabel('KETINGGIAN (m)')
        plt.title('GRAFIK GERAK PELURU')
        plt.grid(True)
        plt.show()
        
        # Menyimpan data perhitungan dalam file CSV
        with open('data_perhitungan.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'Vertical Position'])
            for t, pos in zip(jarak, ketinggian):
                writer.writerow([t, pos])
        
    except ValueError:
        label_height.config(text="INPUT YANG ANDA MASUKKAN KURANG TEPAT!")
        label_distance.config(text="")
        
# Membuat window
window = tk.Tk()
window.title("KALKULATOR GERAK PELURU")

# Membuat label dan input untuk kecepatan awal
label_kecepatan = tk.Label(window, text="kecepatan tembak (m/s):")
label_kecepatan.pack()
entry_velocity = tk.Entry(window)
entry_velocity.pack()

# Membuat label dan input untuk sudut
label_sudut_tembak = tk.Label(window, text="sudut tembak (degrees):")
label_sudut_tembak.pack()
entry_sudut_tembak = tk.Entry(window)
entry_sudut_tembak.pack()


# Tombol untuk menghitung
button_calculate = tk.Button(window, text="HITUNG!!!", command=calculate)
button_calculate.pack()

# Label untuk menampilkan hasil perhitungan
label_height = tk.Label(window)
label_height.pack()
label_distance = tk.Label(window)
label_distance.pack()

window.mainloop()
