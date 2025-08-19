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
window.title("⚽ Football Stats Analyzer")
window.geometry("900x700")
window.configure(bg='#f8f9fa')  

style = ttk.Style()
style.theme_use('clam')  

# Configuring styles
style.configure('TLabel', font=('Arial', 11), background='#f8f9fa', foreground='#2c3e50')
style.configure('TButton', font=('Arial', 11, 'bold'), padding=12, background='#3498db', foreground='white')
style.configure('TEntry', font=('Arial', 11), padding=8, fieldbackground='#ffffff')
style.configure('Title.TLabel', font=('Arial', 14, 'bold'), background='#f8f9fa', foreground='#2c3e50')

style.map('TButton', 
          background=[('active', '#2980b9'), ('pressed', '#1c638e')],
          foreground=[('active', 'white'), ('pressed', 'white')])

# Header
title_label = ttk.Label(window, text="⚽ Football Stats Analyzer", style='Title.TLabel')
title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10), padx=20)

subtitle_label = ttk.Label(window, text="Select a league and enter a team name to analyze performance", 
                          style='TLabel')
subtitle_label.grid(row=1, column=0, columnspan=4, pady=(0, 20), padx=20)

# League selection 
league_frame = ttk.Frame(window, padding=15)
league_frame.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky='ew')

league_label = ttk.Label(league_frame, text="Select League:", style='TLabel')
league_label.grid(row=0, column=0, padx=(0, 10), sticky='w')

leagues_dict = {
    "CL": "Champions League",
    "BL1": "Bundesliga",
    "BSA": "Campeonato Brasileiro Série A",
    "PD": "Primera Division",
    "FL1": "Ligue 1",
    "PL": "Premier League",
    "SA": "Serie A",
    "PPL": "Primeira Liga",
    "DED": "Eredivisie"
}

# Drop down menu for leagues
clicked_league = tk.StringVar()
clicked_league.set("Select a football league")
drop_options = [f"{code} - {name}" for code, name in leagues_dict.items()]
drop = OptionMenu(league_frame, clicked_league, *drop_options)
drop.config(font=('Arial', 10), bg='#3498db', fg='white', width=25)
drop.grid(row=0, column=1, padx=10)

# Team input 
team_frame = ttk.Frame(window, padding=15)
team_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky='ew')

team_label = ttk.Label(team_frame, text="Enter Team Name:", style='TLabel')
team_label.grid(row=0, column=0, padx=(0, 10), sticky='w')

team_input = ttk.Entry(team_frame, width=30, font=('Arial', 11))
team_input.grid(row=0, column=1, padx=10)

api = input("Enter your api key: ")

table_frame = ttk.Frame(window)
table_frame.grid(row=4, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')

table = ttk.Treeview(table_frame, columns=('Pos', 'Team', 'Points'), show='headings')
table.heading('Pos', text='Position')
table.heading('Team', text='Team Name')
table.heading('Points', text='Points')

# Scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

table.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

def button_click():
    selected = clicked_league.get()          
    updated_league = selected.split(" - ")[0]  

    url = f"https://api.football-data.org/v4/competitions/{updated_league}/standings"
    headers = {"X-Auth-Token": api}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if "standings" not in data:  
        messagebox.showerror("Error", "Could not fetch data for this league")
        return

    listed_teams = [team["team"]["name"] for team in data["standings"][0]["table"]]
    extracted_team = team_input.get()
    
    if extracted_team not in listed_teams:
        messagebox.showerror("Error", f"Could not find '{extracted_team}' in the league '{selected}'")
        return
    else:
        existing_teams = [table.item(item)['values'][1] for item in table.get_children()]
        if extracted_team in existing_teams:
            messagebox.showinfo("Info", f"{extracted_team} is already in the table")
            return
        
        for team_data in data['standings'][0]['table']:
            if team_data['team']['name'] == extracted_team:
                position = team_data['position']
                points = team_data['points']
                table.insert('', 'end', values=(position, extracted_team, points))
                break


button = ttk.Button(team_frame, text="🚀 Analyze Team", command=button_click)
button.grid(row=0, column=2, padx=10)

# Configure grid weights for responsive layout
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

# Add some spacing
for i in range(6):
    window.grid_rowconfigure(i, pad=10)

window.mainloop()