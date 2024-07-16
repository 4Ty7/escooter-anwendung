import json
import tkinter as tk
from tkinter import Toplevel, Label, Button, PhotoImage

# Konfigurationsdateien laden
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('local.json', 'r', encoding='utf-8') as localization_file:
    localization = json.load(localization_file)

# Konfigurationswerte zuweisen
Grundgebuehr = config['Grundgebuehr']
Pro_Minute = config['Pro_Minute']
Pro_Kilometer = config['Pro_Kilometer']
icon_path = config['icon_path']
logo_path = config.get('logo_path', 'logo.png')

def calculate_price_by_duration(duration_minutes):
    total_price = Grundgebuehr + (Pro_Minute * duration_minutes)
    return total_price

def calculate_price_by_distance(distance_km):
    total_price = Grundgebuehr + (Pro_Kilometer * distance_km)
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

    button = Button(msg_window, text=localization["ok_button"], command=msg_window.destroy)
    button.pack(pady=10)

def calculate_by_duration():
    try:
        duration = float(entry_duration.get())
        price = calculate_price_by_duration(duration)
        message = localization["Preis_nach_Minute_Satz"].format(duration=int(duration), price=f"{price:.2f} €")
        show_custom_message(localization["Kalkulation"], message)
    except ValueError:
        show_custom_message(localization["Fehlernachricht"], localization["Ungültiger_Eintrag_Dauer"])

def calculate_by_distance():
    try:
        distance = float(entry_distance.get())
        price = calculate_price_by_distance(distance)
        message = localization["Preis_bei_Kilometer_Satz"].format(distance=distance, price=f"{price:.2f} €")
        show_custom_message(localization["Kalkulation"], message)
    except ValueError:
        show_custom_message(localization["Fehlernachricht"], localization["Ungültiger_Eintrag_Kilometer"])

def open_duration_window():
    duration_window = Toplevel(root)
    duration_window.title(localization["Preis_Minute"])
    try:
        duration_window.iconphoto(False, tk.PhotoImage(file=icon_path))
    except Exception as e:
        print(f"Error loading icon: {e}")

    label_duration = Label(duration_window, text=localization["Dauer_Minuten"])
    label_duration.pack(padx=10, pady=5)

    global entry_duration
    entry_duration = tk.Entry(duration_window)
    entry_duration.pack(padx=10, pady=5)

    button_duration = Button(duration_window, text=localization["Berechnung"], command=calculate_by_duration)
    button_duration.pack(padx=10, pady=10)

def open_distance_window():
    distance_window = Toplevel(root)
    distance_window.title(localization["Preis_Kilometer"])
    try:
        distance_window.iconphoto(False, tk.PhotoImage(file=icon_path))
    except Exception as e:
        print(f"Error loading icon: {e}")

    label_distance = Label(distance_window, text=localization["Dauer_Kilometer"])
    label_distance.pack(padx=10, pady=5)

    global entry_distance
    entry_distance = tk.Entry(distance_window)
    entry_distance.pack(padx=10, pady=5)

    button_distance = Button(distance_window, text=localization["Berechnung"], command=calculate_by_distance)
    button_distance.pack(padx=10, pady=10)

# Erstellen des Hauptfensters
root = tk.Tk()
root.title(localization["Willkommen"].split('\n')[0])
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

welcome_label = Label(root, text=localization["Willkommen"], font=("Arial", 14))
welcome_label.pack(padx=20, pady=20)

button_open_duration = Button(root, text=localization["Preis_Minute"], command=open_duration_window)
button_open_duration.pack(pady=10)

button_open_distance = Button(root, text=localization["Preis_Kilometer"], command=open_distance_window)
button_open_distance.pack(pady=10)

# Gruppe: C6 Label unten links hinzufügen
group_label = Label(root, text="Gruppe: C6", anchor='w')
group_label.place(x=10, y=470)

# Hauptfenster starten
root.mainloop()
