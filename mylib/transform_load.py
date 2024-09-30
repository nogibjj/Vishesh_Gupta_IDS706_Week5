"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv

def load(dataset="data/match_results.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    data_to_insert = list(payload)[1:]  # Skip the header if present

    conn = sqlite3.connect("MatchResultsDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS MatchResultsDB")
    c.execute(
        """
        CREATE TABLE MatchResultsDB (
            Round INTEGER,
            Date TEXT,
            "Team 1" TEXT,
            "Team 2" TEXT,
            FT TEXT
        )
        """
    )
    # insert
    c.executemany(
        """
        INSERT INTO MatchResultsDB (
            Round, 
            Date, 
            "Team 1", 
            "Team 2", 
            FT
            ) 
            VALUES (?, ?, ?, ?, ?)
        """,
        data_to_insert,
    )
    conn.commit()
    conn.close()
    return "MatchResultsDB.db"