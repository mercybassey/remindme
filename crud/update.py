import sqlite3
import click

from database.initialize import DB_FILE, initialize_database

def get_existing_value(cursor, column, task):
    cursor.execute(f"SELECT {column} FROM tasks WHERE description = ?", (task,))
    return cursor.fetchone()[0]

def print_update_message(description, task, new_value):
    print(f"{description} for task '{task}' updated successfully to '{new_value}'")

@click.command()
@click.option("--task", help="Update a task")
@click.option("--new-task", help="New description for the task")
@click.option("--new-time", help="New scheduled time (HH:MM)")
@click.option("--new-lead", help="New lead time in minutes")

def update(task, new_task, new_lead, new_time):
    """Update a task"""
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            
            cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (task,))
            exists = cursor.fetchone()

            if not exists:
                print(f"Task with description '{task}' does not exist. No updates performed.")
                return
            
            update_query = "UPDATE tasks SET"
            update_values = []

            if new_task:
                existing_description = get_existing_value(cursor, "description", task)
                if existing_description == new_task:
                    print(f"Nothing to update. Task with description '{task}' already has the description '{new_task}'")
                else:
                    update_query += " description = ?,"
                    update_values.append(new_task)
                    print_update_message("Description", task, new_task)

            if new_time:
                existing_scheduled_time = get_existing_value(cursor, "scheduled_time", task)
                if existing_scheduled_time == new_time:
                    print(f"Nothing to update. Task with description '{task}' already has time set to '{new_time}'")
                else:
                    update_query += " scheduled_time = ?,"
                    update_values.append(new_time)
                    print_update_message("Time", task, new_time)

            if new_lead:
                existing_lead = int(get_existing_value(cursor, "lead_time", task))
                new_lead = int(new_lead)
                if existing_lead == new_lead:
                    print(f"Nothing to update. Task with description '{task}' already has a lead time {new_lead}")
                else:
                    update_query += " lead_time = ?,"
                    update_values.append(new_lead)
                    print_update_message("Lead time", task, new_lead)

            if update_values:
                update_query = update_query.rstrip(',')
                update_query += " WHERE description = ?"
                update_values.append(task)

                cursor.execute(update_query, tuple(update_values))
                db.commit()

    except sqlite3.Error as e:
        print(f"Error updating task: {e}")

if __name__ == '__main__':
    update()
