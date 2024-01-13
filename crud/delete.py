import click
import sqlite3
from database.initialize import initialize_database, DB_FILE

from .utils.task_lower import lowercase

@click.command()
@click.option("--task", prompt="Task to delete", help="Delete a task")
def delete(task):
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()

            task = lowercase(task)
            
            cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (task,))
            exists = cursor.fetchone()

            if not exists:
                print(f"\033[38;5;208m• Nothing to delete. Task with description '{task}' does not exist.")
                return

            cursor.execute('DELETE FROM tasks WHERE description = ?', (task,))
            db.commit()

        print(f"\033[92m✔ Task '{task}' deleted successfully")

    except sqlite3.Error as e:
        print(f"\033[91m✘ Error deleting task: {e}")

if __name__ == '__main__':
    delete()
