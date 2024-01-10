import click
import sqlite3

from database.initialize import initialize_database, DB_FILE

@click.command()

@click.option("--task", prompt="Task", help="Add a new task", required=True)
@click.option("--time", prompt="Scheduled Time (HH:MM)", help="Scheduled time for the task", required=True)
@click.option("--lead", prompt="Lead Time", help="Lead time in minutes.", required=True)

def add(task, time, lead):
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            
            cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (task,))
            exists = cursor.fetchone()

            if exists:
                print(f"Task with description '{task}' already exists. Only tasks with distinct descriptions are allowed")
                return

            cursor.execute('INSERT INTO tasks (description, scheduled_time, lead_time) VALUES (?, ?, ?)', (task, time, lead))
            db.commit()

        print(f"Task '{task}' added successfully")
    except sqlite3.Error as e:
        print(f"Error adding task: {e}")

if __name__ == '__main__':
    add()
