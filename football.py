#FOOTBALL STATS PROJECT
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import requests 
import json
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

window = tk.Tk()
window.title("Football Stats Project")
window.geometry("800x700")

style = ttk.Style(window)
style.configure('TLabel', font=('Arial', 12), background='#f0f0f0')
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=8)

stock_Label = ttk.Label(window, text="Enter a football team")
stock_Label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

stock_input = ttk.Entry(window)
stock_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")


url = "https://api.football-data.org/v4/competitions/PL/standings"
headers = {"X-Auth-Token": "aaacb7a9d68845869673a0145b323b79"}

response = requests.get(url, headers=headers)
data = response.json()

# print(response.status_code)
# print(data)
listed_teams = []
league = data['competition']['name']
for team in data['standings'][0]['table']:
    teams = team['team']['name']
    listed_teams.append(teams)

def button_click():
    print("Button has been clicked")

button = ttk.Button(window, text="Visualize", command=button_click)
button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

season = data['filters']['season']
# print(json.dumps(data, indent=4))


window.mainloop()

