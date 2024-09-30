"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

def load(dataset="data/match_results.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("MatchResultsDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS MatchResultsDB")
    c.execute(
        """
        CREATE TABLE MatchResultsDB (
            GAMEWEEK INTEGER PRIMARY KEY,
            DATE TEXT,
            TEAM_1 TEXT,
            TEAM_2 TEXT,
            SCORE TEXT,
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO MatchResultsDB (
            Round, 
            Date, 
            Team 1, 
            Team 2, 
            FT
            ) 
            VALUES (?, ?, ?, ?, ?)
        """,
        payload,
    )
    conn.commit()
    conn.close()
    return "MatchResultsDB.db"