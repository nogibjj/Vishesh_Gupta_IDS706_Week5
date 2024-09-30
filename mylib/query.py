import sqlite3

def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("MatchResultsDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MatchResultsDB")
    print("Top 5 rows of the MatchResultsDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"

# add more possible queries 