from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import hashlib
import binascii
def browse_file(entry_var):
    file_path = filedialog.askopenfilename()
    entry_var.set(file_path)

def calculate_hash():
    file_path1 = file_var.get()
    file_path2 = file_var2.get()
    algorithm = algorithm_var.get()
    hash_values = []

    if file_path1 and file_path2 and algorithm:
        file_paths = [file_path1,file_path2]
        hash_entrys = [hash_entry1,hash_entry2]

        for file_path, hash_entry in zip(file_paths, hash_entrys):
            hash_value = calculate_file_hash(file_path, algorithm)
            hash_entry.delete(0, tk.END)
            hash_entry.insert(0, hash_value)

            hash_values.append(hash_value)

        if hash_values[0] == hash_values[1]:
            messagebox.showinfo("Uyarı", "Hash değerleri eşittir. Dosyalar doğrulandı.")
        else:
            messagebox.showinfo("Uyarı", "Hash değerleri farklıdır. Dosyalar doğrulanamadı.")




    else:
        result_label.config(text="Dosya ve algoritma seçimi yapınız.")




def calculate_file_hash(file_path, algorithm):
    with open(file_path, "rb") as file:
        hash_object = hashlib.new(algorithm)
        while chunk := file.read(8192):
            hash_object.update(chunk)
        return hash_object.hexdigest()

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Dosya Hash Hesaplayıcı")

# Pencere boyutlarını ayarla (genişlik x yükseklik)
root.geometry("1500x400")
# Pencerenin boyutlarını sabit yap
root.resizable(width=False, height=False)


# Arka plan rengini ayarla
root.configure(bg="#f0f0f0")

# Değişkenler
file_var = tk.StringVar()
file_var2 = tk.StringVar()

algorithm_var = tk.StringVar(value="md5")

# Başlık etiketi
title_label = tk.Label(root, text="Dosya Hash Hesaplayıcı", font=("Helvetica", 16), bg="#f0f0f0", pady=10)
title_label.grid(row=0, column=0, columnspan=3)

# 1.Dosya seçimi
file_label = tk.Label(root, text="Dosya Seçin:", font=("Helvetica", 12), bg="#f0f0f0")
file_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_file = tk.Entry(root, textvariable=file_var, state="disabled", width=40)
entry_file.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

browse_button = tk.Button(root, text="Gözat", command=lambda: browse_file(file_var))
browse_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)


# 2.Dosya seçimi

entry_file2 = tk.Entry(root, textvariable=file_var2, state="disabled", width=40)
entry_file2.grid(row=1, column=5, padx=10, pady=5, sticky=tk.W)
browse_button2 = tk.Button(root, text="Gözat", command=lambda: browse_file(file_var2))
browse_button2.grid(row=1, column=6, padx=0, pady=0, sticky=tk.W)




# Hash değeri gösterme alanı

result_label = tk.Label(root, text="Hash:", font=("Helvetica", 12), bg="#f0f0f0")
result_label.grid(row=2, column=0, padx=10 , pady=5)

hash_entry1 = tk.Entry(root, width=40)
hash_entry1.grid(row=2, column=1, padx=10, pady=15, sticky=tk.W)


# 2.Hash değeri gösterme alanı

result_label2 = tk.Label(root, text="Hash:", font=("Helvetica", 12), bg="#f0f0f0")
result_label2.grid(row=2, column=4, padx=10 , pady=5)

hash_entry2 = tk.Entry(root, width=40)
hash_entry2.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)





# Hash algoritması seçimi
algorithm_label = tk.Label(root, text="Hash Algoritması:", font=("Helvetica", 12,"bold"), bg="#f0f0f0")
algorithm_label.grid(row=3, column=0,padx=10, pady=55, sticky=tk.W)

algorithm_md5 = tk.Radiobutton(root, text="MD5", variable=algorithm_var, value="md5", bg="#f0f0f0")
algorithm_md5.grid(row=3, column=1, padx=10, pady=0, sticky=tk.W)

algorithm_sha256 = tk.Radiobutton(root, text="SHA256", variable=algorithm_var, value="sha256", bg="#f0f0f0")
algorithm_sha256.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

algorithm_sha1 = tk.Radiobutton(root, text="SHA1", variable=algorithm_var, value="sha1", bg="#f0f0f0")
algorithm_sha1.grid(row=5, column=1, padx=10, pady=20, sticky=tk.W)



# Hash hesaplama butonu
calculate_button = tk.Button(root, text="Hash Hesapla ve doğrula", command=calculate_hash, bg="#4CAF50", fg="white")
calculate_button.grid(row=4, column=1, columnspan=4, pady=10 ,padx=30)





    


# Pencereyi göster
root.mainloop()
