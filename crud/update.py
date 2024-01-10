import sqlite3
import click

from database.initialize import DB_FILE, initialize_database

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
                cursor.execute("SELECT description FROM tasks WHERE description = ?", (task,))
                existing_description = cursor.fetchone()
                if existing_description[0] == new_task:
                    print(f"Nothing to update. Task with description '{task}' already has the description '{new_task}'")
                else:
                    update_query += " description = ?,"
                    update_values.append(new_task)
                    print(f"Task '{task}' updated successfully to '{new_task}'")


            if new_time:
                cursor.execute("SELECT scheduled_time FROM tasks WHERE description = ?", (task,))
                existing_sheduled_time = cursor.fetchone()
                if existing_sheduled_time[0] == new_time:
                    print(f"Nothing to update. Task with description '{task}' aleady has set to time '{new_time}'")
                else:
                    update_query += " scheduled_time = ?,"
                    update_values.append(new_time)
                    print(f"Time for task: '{task}' updated successfully to '{new_time}'")
                    
            if new_lead:
                cursor.execute("SELECT lead_time FROM tasks WHERE description = ?", (task,))
                existing_lead = cursor.fetchone()
                new_lead = int(new_lead)
                if (existing_lead[0]) == new_lead:
                    print(f"Nothing to update. Task with description '{task}' aleady has a lead time {new_lead}")
                else:
                    update_query += " lead_time = ?,"
                    update_values.append(new_lead)
                    print(f"Lead time for task: '{task}' updated successfully to {new_lead}")
                    

            if not any([new_task or new_time or new_lead]):
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









