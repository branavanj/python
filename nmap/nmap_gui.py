import subprocess
import tkinter as tk

def run_nmap():
    ip_address = entry_ip_address.get()
    nmap_args = entry_nmap_args.get()
    command = f"nmap {nmap_args} {ip_address}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    output_text.delete('1.0', tk.END)  # Efface le contenu précédent
    output_text.insert(tk.END, result.stdout)

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Nmap GUI")

# Ajouter les éléments d'interface utilisateur
label_ip_address = tk.Label(root, text="Adresse IP:")
label_ip_address.pack()

entry_ip_address = tk.Entry(root)
entry_ip_address.pack()

label_nmap_args = tk.Label(root, text="Arguments Nmap:")
label_nmap_args.pack()

entry_nmap_args = tk.Entry(root)
entry_nmap_args.pack()

button_run = tk.Button(root, text="Exécuter Nmap", command=run_nmap)
button_run.pack()

output_text = tk.Text(root)
output_text.pack()

root.mainloop()
