import sqlite3
import click

from database.initialize import DB_FILE, initialize_database

@click.command()
@click.option("--task", help="Update a task")
@click.option("--new-task", help="New description for the task")
@click.option("--new-time", help="New scheduled time (HH:MM)")
@click.option("--new-lead", help="New lead time in minutes (default is 20 minutes).")

def update(task, new_task, new_time, new_lead):
    """Update a task"""
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            update_query = "UPDATE tasks SET"
            update_values = []

            if new_task:
                update_query += " description = ?,"
                update_values.append(new_task)
                print(f"Task '{task}' updated successfully to '{new_task}")

            if new_time:
                update_query += " scheduled_time = ?,"
                update_values.append(new_time)
                print(f"Time for task: '{task}' updated successfully to '{new_time}'")

            if new_lead:
                update_query += " lead_time = ?,"
                update_values.append(new_lead)
                print(f"Lead for task: '{task}' updated successfully to {new_lead} minutes")

            if not any(new_task or new_time or new_lead):
                print("No valid update option provided.")
                return

            update_query = update_query.rstrip(',')

            update_query += " WHERE description = ?"
            update_values.append(task)

            cursor.execute(update_query, tuple(update_values))
            db.commit()
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")

if __name__ == '__main__':
    update()





