# gui.py

import tkinter as tk
from tkinter import messagebox
from hamming import calculate_hamming_code, introduce_error, detect_and_correct

last_code = ""
last_corrupted = ""

def process():
    data = entry.get()
    if not set(data).issubset({'0', '1'}):
        messagebox.showerror("Hata", "Lütfen sadece 0 ve 1 giriniz.")
        return
    global last_code
    last_code = calculate_hamming_code(data)
    code_label.config(text=f"Hamming Kodu: {last_code}")

def create_error():
    global last_corrupted
    corrupted, index = introduce_error(last_code)
    last_corrupted = corrupted
    corrupted_label.config(text=f"Hatalı Kod: {corrupted} (bit {index})")

def correct_error():
    corrected, pos = detect_and_correct(last_corrupted)
    corrected_label.config(text=f"Düzeltilmiş Kod: {corrected} (bit {pos} düzeltildi)")


root = tk.Tk()
root.title("Hamming SEC-DED Simülatörü")

tk.Label(root, text="Veri Uzunluğu Seç:").pack()
bit_size = tk.StringVar(root)
bit_size.set("8")
bit_dropdown = tk.OptionMenu(root, bit_size, "8", "16", "32")
bit_dropdown.pack()

def generate_random_data():
    import random
    size = int(bit_size.get())
    binary_data = ''.join(random.choice('01') for _ in range(size))
    entry.delete(0, tk.END)
    entry.insert(0, binary_data)

tk.Button(root, text="Rastgele Veri Oluştur", command=generate_random_data).pack()

tk.Label(root, text="Veri (binary):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Kodu Hesapla", command=process).pack()
code_label = tk.Label(root, text="Hamming Kodu: ")
code_label.pack()

tk.Button(root, text="Hata Ekle", command=create_error).pack()
corrupted_label = tk.Label(root, text="Hatalı Kod: ")
corrupted_label.pack()

tk.Button(root, text="Hata Düzelt", command=correct_error).pack()
corrected_label = tk.Label(root, text="Düzeltilmiş Kod: ")
corrected_label.pack()

root.mainloop()
