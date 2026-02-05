import sqlite3
import gradio as gr 
import pandas as pd 

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976;
    """

    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    #Make a list of playerIDs
    players = []
    for record in records:
        players.append(record[0])
    return players
    

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE yearID = 1976 AND teamID = 'PHI' AND playerID = ?
    """

    cursor.execute(query,[player]) #player replaces the questions mark above
    records = cursor.fetchall()
    conn.close()
    return records[0][0]

#print(f('schmimi01'))

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            phillies_dd = gr.Dropdown(choices = fetch_phillies(), value = None, label = "Player")
        with gr.Column():
            HRbox = gr.Number(label = "Home Runs")

    phillies_dd.change(fn = f, inputs = [phillies_dd], outputs = [HRbox])

iface.launch()
