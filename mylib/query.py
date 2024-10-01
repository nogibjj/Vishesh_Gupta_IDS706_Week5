import sqlite3

def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("MatchResultsDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MatchResultsDB LIMIT 5")
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
    cursor.execute("SELECT * FROM MatchResultsDB WHERE Round = ?", (gameweek,))
    print("Since we have deleted that gameweek it should be empty")
    print(cursor.fetchall())
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
    cursor.execute("SELECT * FROM MatchResultsDB WHERE Round = ?", (gameweek,))
    print("We should either have a new gameweek or an extra row in existing gameweeks")
    print(cursor.fetchall())
    conn.close()
    return "Success"

