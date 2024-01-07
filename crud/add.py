import sqlite3

from database.initialize import initialize_database, DB_FILE

def add_task(task, time, lead):
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO tasks (description, scheduled_time, lead_time) VALUES (?, ?, ?)', (task, time, lead))
            db.commit()

        print(f"Task '{task}' added successfully")
    except sqlite3.Error as e:
        print(f"Error adding task: {e}")
