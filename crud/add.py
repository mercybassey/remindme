import click
import sqlite3
from datetime import datetime

from database.initialize import initialize_database, DB_FILE
from .utils.lead_time_validation import is_valid_lead_time

from .utils.task_lower import lowercase

@click.command()
@click.option("--task", prompt="Task", help="Add a new task", required=True)
@click.option("--time", prompt="Scheduled Time (HH:MM)", help="Scheduled time for the task", required=True)
@click.option("--lead", prompt="Lead Time", help="Lead time in minutes.", required=True)
def add(task, time, lead):
    try:
        initialize_database()

        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            print("\033[91m✘ Invalid time format. Please use a valid time of 24 hours\033[0m")
            return

        current_time = datetime.now().strftime("%H:%M")

        task = lowercase(task)

        if not is_valid_lead_time(datetime.strptime(current_time, "%H:%M"), datetime.strptime(time, "%H:%M"), int(lead)):
            print("\033[91m✘ Invalid lead time. Lead time must be a positive duration from the current time to the scheduled time\033[0m")
            return

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            
            cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (task,))
            exists = cursor.fetchone()

            if exists:
                print(f"\033[91m✘ Task with description '{task}' already exists. Only tasks with distinct descriptions are allowed")
                return

            cursor.execute('INSERT INTO tasks (description, scheduled_time, lead_time) VALUES (?, ?, ?)', (task, time, lead))
            db.commit()

        print(f"\033[92m✔ Task '{task}' added successfully")
    except sqlite3.Error as e:
        print(f"\033[91m✘ Error adding task: {e}")

if __name__ == '__main__':
    add()

