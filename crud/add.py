import click
import sqlite3

from database.initialize import initialize_database, DB_FILE

@click.command()

@click.option("--task", prompt="Task", help="Add a new task")
@click.option("--time", prompt="Scheduled Time (HH:MM)", help="Scheduled time for the task")
@click.option("--lead", default=20, help="Lead time in minutes (default is 20 minutes).")

def add(task, time, lead):
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO tasks (description, scheduled_time, lead_time) VALUES (?, ?, ?)', (task, time, lead))
            db.commit()

        print(f"Task '{task}' added successfully")
    except sqlite3.Error as e:
        print(f"Error adding task: {e}")

if __name__ == '__main__':
    add()
