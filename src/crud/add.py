import click
import sqlite3

from src.database.initialize import initialize_database, DB_FILE

@click.command()
@click.option("--task", prompt="Task", help="Add a new task", length=50)
@click.option("--time", prompt="Scheduled Time (HH:MM)", help="Scheduled time for the task")
@click.option("--lead", default=20, help="Lead time in minutes (default is 20 minutes).")


def add_task(task, time, lead):
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO tasks (task, time, lead) VALUES (?, ?, ?)', (task, time, lead))
            db.commit()

        print(f"Task '{task}' added successfully")
    except sqlite3.Error as e:
        print(f"Error adding tadk: {e}")

if __name__ == '__main__':
    add_task()