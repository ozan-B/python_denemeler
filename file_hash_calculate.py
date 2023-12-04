import tkinter as tk
from tkinter import filedialog
import hashlib
import os

def hash_file(file_path, algorithm):
    """
    Belirtilen dosyanın hash değerini hesaplayan fonksiyon.
    """
    hasher = hashlib.new(algorithm)

    with open(file_path, 'rb') as file:
        chunk = 0
        while chunk := file.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()



def calculate_hash():
    """
    Dosya hash'ini hesaplayan fonksiyon ve hash değerini gösteren Entry'yi güncelleyen kısım.
    """
    file_path = file_var.get()  # Kullanıcının seçtiği dosya yolu
    algorithm = algorithm_var.get()  # Kullanıcının seçtiği hash algoritması

    if os.path.exists(file_path):  # Dosya var mı diye kontrol et
        file_hash = hash_file(file_path, algorithm)  # Dosyanın hash'ini hesapla
        result_label.config(text=f"{algorithm.upper()} Hash: {file_hash}")  # Sonucu göster
        hash_entry.delete(0, tk.END)  # Entry'nin içeriğini temizle
        hash_entry.insert(tk.END, file_hash)  # Yeni hash'i Entry'ye ekle
    else:
        result_label.config(text="Dosya bulunamadı!")  # Dosya bulunamadığında hata mesajını göster
        hash_entry.delete(0, tk.END)  # Entry'nin içeriğini temizle

def browse_file():
    """
    Kullanıcının dosya seçmesini sağlayan fonksiyon.
    """
    file_path = filedialog.askopenfilename()  # Dosya seçim penceresini aç
    file_var.set(file_path)  # Seçilen dosya yolunu güncelle

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Dosya Hash Hesaplayıcı")

# Değişkenler
file_var = tk.StringVar()  # Dosya yolunu tutmak için StringVar
algorithm_var = tk.StringVar(value="md5")  # Hash algoritmasını tutmak için StringVar (başlangıçta md5 olarak ayarlı)

# Arayüz öğeleri
tk.Label(root, text="Dosyayı Seçin:").pack()
tk.Entry(root, textvariable=file_var, state="disabled", width=40).pack(side=tk.LEFT)
tk.Button(root, text="Gözat", command=browse_file).pack(side=tk.LEFT)

tk.Label(root, text="Hash Algoritması:").pack()
tk.Radiobutton(root, text="MD5", variable=algorithm_var, value="md5").pack(anchor=tk.W)
tk.Radiobutton(root, text="SHA256", variable=algorithm_var, value="sha256").pack(anchor=tk.W)
tk.Radiobutton(root, text="SHA1", variable=algorithm_var, value="sha1").pack(anchor=tk.W)

tk.Button(root, text="Hash Hesapla", command=calculate_hash).pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Hash değerini göstermek için bir Entry ekle
hash_entry = tk.Entry(root, width=40)
hash_entry.pack()

# Pencereyi göster
root.mainloop()
