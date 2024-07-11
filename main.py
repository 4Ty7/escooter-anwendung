import json
import tkinter as tk
from tkinter import Toplevel, Label, Button, PhotoImage

# Konfigurationsdateien laden
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('local.json', 'r', encoding='utf-8') as localization_file:
    localization = json.load(localization_file)

# Konfigurationswerte zuweisen
base_rate = config['base_rate']
per_minute_rate = config['per_minute_rate']
per_km_rate = config['per_km_rate']
icon_path = config['icon_path']
logo_path = config.get('logo_path', 'logo.png')

def calculate_price_by_duration(duration_minutes):
    total_price = base_rate + (per_minute_rate * duration_minutes)
    return total_price

def calculate_price_by_distance(distance_km):
    total_price = base_rate + (per_km_rate * distance_km)
    return total_price

def show_custom_message(title, message):
    msg_window = Toplevel(root)
    msg_window.title(title)

    try:
        msg_window.iconphoto(False, tk.PhotoImage(file=icon_path))
    except Exception as e:
        print(f"Error loading icon: {e}")

    label = Label(msg_window, text=message)
    label.pack(padx=20, pady=10)

    button = Button(msg_window, text=localization["ok_button_text"], command=msg_window.destroy)
    button.pack(pady=10)

def calculate_by_duration():
    try:
        duration = float(entry_duration.get())
        price = calculate_price_by_duration(duration)
        message = localization["price_by_duration_message"].format(duration=int(duration), price=f"{price:.2f} €")
        show_custom_message(localization["price_calculation_title"], message)
    except ValueError:
        show_custom_message(localization["error_title"], localization["invalid_duration_message"])

def calculate_by_distance():
    try:
        distance = float(entry_distance.get())
        price = calculate_price_by_distance(distance)
        message = localization["price_by_distance_message"].format(distance=distance, price=f"{price:.2f} €")
        show_custom_message(localization["price_calculation_title"], message)
    except ValueError:
        show_custom_message(localization["error_title"], localization["invalid_distance_message"])

def open_duration_window():
    duration_window = Toplevel(root)
    duration_window.title(localization["calculate_price_by_duration_title"])
    try:
        duration_window.iconphoto(False, tk.PhotoImage(file=icon_path))
    except Exception as e:
        print(f"Error loading icon: {e}")

    label_duration = Label(duration_window, text=localization["usage_duration_label"])
    label_duration.pack(padx=10, pady=5)

    global entry_duration
    entry_duration = tk.Entry(duration_window)
    entry_duration.pack(padx=10, pady=5)

    button_duration = Button(duration_window, text=localization["calculate_button_text"], command=calculate_by_duration)
    button_duration.pack(padx=10, pady=10)

def open_distance_window():
    distance_window = Toplevel(root)
    distance_window.title(localization["calculate_price_by_distance_title"])
    try:
        distance_window.iconphoto(False, tk.PhotoImage(file=icon_path))
    except Exception as e:
        print(f"Error loading icon: {e}")

    label_distance = Label(distance_window, text=localization["usage_distance_label"])
    label_distance.pack(padx=10, pady=5)

    global entry_distance
    entry_distance = tk.Entry(distance_window)
    entry_distance.pack(padx=10, pady=5)

    button_distance = Button(distance_window, text=localization["calculate_button_text"], command=calculate_by_distance)
    button_distance.pack(padx=10, pady=10)

# Erstellen des Hauptfensters
root = tk.Tk()
root.title(localization["welcome_message"].split('\n')[0])
try:
    root.iconphoto(False, tk.PhotoImage(file=icon_path))
except Exception as e:
    print(f"Error loading icon: {e}")

# Fenstergröße festlegen und Maximierung deaktivieren
root.resizable(False, False)
root.geometry('500x500')

# Logo anzeigen
try:
    logo_image = tk.PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo_image)
    logo_label.pack(pady=10)
except Exception as e:
    print(f"Error loading logo: {e}")

welcome_label = Label(root, text=localization["welcome_message"], font=("Arial", 14))
welcome_label.pack(padx=20, pady=20)

button_open_duration = Button(root, text=localization["calculate_price_by_duration_title"], command=open_duration_window)
button_open_duration.pack(pady=10)

button_open_distance = Button(root, text=localization["calculate_price_by_distance_title"], command=open_distance_window)
button_open_distance.pack(pady=10)

# Gruppe: C6 Label unten links hinzufügen
group_label = Label(root, text="Gruppe: C6", anchor='w')
group_label.place(x=10, y=470)

# Hauptfenster starten
root.mainloop()
