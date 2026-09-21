import sqlite3
from datetime import datetime
from pathlib import Path

DB = Path(__file__).parent / "journal.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute( 
        """
        CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        sentiment TEXT NOT NULL,
        emotions TEXT NOT NULL,
        score REAL NOT NULL,
        timestamp TEXT NOT NULL)"""
    )
    conn.commit()
    conn.close()

def save_entry(text,sentiment,emotion,score):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    time = datetime.now().isoformat()
    cursor.execute( 
        """
        INSERT INTO entries(text,sentiment,emotion,score,timestamp)
        VALUES (?,?,?,?,?)"""
        ,(text,sentiment,emotion,score,time)
    )
    conn.commit()
    conn.close()


def get_entries():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row ##Return into tuple is an inconvinience,as i want name based acces to the columns
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM entries ORDER BY timestamp DESC")
    entries = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return entries