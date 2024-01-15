import sqlite3
import click


from database.initialize import DB_FILE, initialize_database


from .columns.new_task import apply_new_task
from .columns.new_time import apply_new_time
from .columns.new_lead import validate_and_apply_lead

from ..utils.task_lower import lowercase




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

            task = lowercase(task)
                
            cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (task ,))
            exists = cursor.fetchone()

            if not exists:
                print(f"\033[38;5;208m• Task with description '{task}' does not exist. No updates performed.")
                return  
          
            
            update_query = "UPDATE tasks SET"
            update_values = []
            
            update_query, update_values = apply_new_task(cursor, task , new_task, update_query, update_values)
            update_query, update_values = apply_new_time(cursor, task , new_time, update_query, update_values)
            update_query, update_values = validate_and_apply_lead(cursor, task , new_lead, new_time, update_query, update_values)

            if update_values:
                update_query = update_query.rstrip(',')
                update_query += " WHERE description = ?"
                update_values.append(task)

                cursor.execute(update_query, tuple(update_values))
                db.commit()

    except sqlite3.Error as e:
        print(f"\033[91m✘ Error updating task: {e}")

if __name__ == '__main__':
    update()
