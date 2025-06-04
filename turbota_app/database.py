import sqlite3

def get_db():
    conn = sqlite3.connect("psychologist.db")
    return conn