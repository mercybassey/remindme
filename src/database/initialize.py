import sqlite3

DB_FILE = 'tasks.db'

def initialize_database():
    try:
        with sqlite3.connect(DB_FILE) as db:
            db.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, description TEXT, scheduled_time TEXT, lead_time INTEGER)')
    except sqlite3.Error as e:
        print("Error connecting to database")

