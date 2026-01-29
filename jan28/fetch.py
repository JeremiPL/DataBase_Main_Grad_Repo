import sqlite3
import pandas as pd 

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = """
    SELECT teamID, sum(HR) as seasonHR
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    ORDER BY seasonHR desc
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ["teamID", "seasonHR"])
print(records_df)