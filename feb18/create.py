import sqlite3
import pandas as pd 

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

conn.commit()
conn.close()