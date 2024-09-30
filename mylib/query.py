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

def delete(gameweek):
    """Delete a records from the MatchResultsDB table based on the GAMEWEEK"""
    conn = sqlite3.connect("MatchResultsDB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MatchResultsDB WHERE Round = ?", (gameweek,))
    conn.commit()
    conn.close()
    return "Success"

# Create a New Record
def create(gameweek, date, team1, team2, score):
    """Insert a new record into the MatchResultsDB table"""
    conn = sqlite3.connect("MatchResultsDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO MatchResultsDB (Round, Date, "Team 1", "Team 2", FT)
        VALUES (?, ?, ?, ?, ?)
        """,
        (gameweek, date, team1, team2, score),
    )
    conn.commit()
    conn.close()
    return "Success"

