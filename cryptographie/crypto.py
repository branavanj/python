import tkinter as tk
from tkinter import filedialog
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Random import get_random_bytes
import os

def encrypt_file(file_path, password):
    salt = get_random_bytes(AES.block_size)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(open(file_path, 'rb').read())
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + cipher.iv + encrypted_data)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    salt = data[:AES.block_size]
    iv = data[AES.block_size:AES.block_size+AES.block_size]
    encrypted_data = data[AES.block_size+AES.block_size:]
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_data)

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def encrypt_button_click():
    file_path = file_entry.get()
    password = password_entry.get()
    if file_path and password:
        encrypt_file(file_path, password)
        status_label.config(text="Fichier chiffré avec succès!")

def decrypt_button_click():
    file_path = file_entry.get()
    password = password_entry.get()
    if file_path and password:
        decrypt_file(file_path, password)
        status_label.config(text="Fichier déchiffré avec succès!")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chiffrement et Déchiffrement de Fichier")

# Zone de saisie du chemin du fichier
file_label = tk.Label(root, text="Chemin du fichier:")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()
browse_button = tk.Button(root, text="Parcourir", command=browse_file)
browse_button.pack()

# Zone de saisie du mot de passe
password_label = tk.Label(root, text="Mot de passe:")
password_label.pack()
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack()

# Boutons d'action
encrypt_button = tk.Button(root, text="Chiffrer le fichier", command=encrypt_button_click)
encrypt_button.pack()
decrypt_button = tk.Button(root, text="Déchiffrer le fichier", command=decrypt_button_click)
decrypt_button.pack()

# Étiquette d'état
status_label = tk.Label(root, text="")
status_label.pack()

# Lancement de la boucle principale de l'application
root.mainloop()
