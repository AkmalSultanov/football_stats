#FOOTBALL STATS PROJECT
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import requests 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

window = tk.Tk()
window.title("Football Stats Project")
window.geometry("800x700")

url = "https://api.football-data.org/v4/competitions/PL/standings"
headers = {"X-Auth-Token": "ENTER YOUR API KEY HERE"}

response = requests.get(url, headers=headers)
data = response.json()

# print(response.status_code)
# print(data)

league = data['competition']['name']
#need to work on getting the team names
teams = data['standings']['table']['team']['name']
season = data['filters']['season']
print(season)

window.mainloop()

