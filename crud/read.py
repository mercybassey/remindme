import sqlite3
from tabulate import tabulate
import click

from database.initialize import DB_FILE, initialize_database

@click.command()
@click.option("--all", default=False, is_flag=True, help="Get all tasks.")
def get(all):
    """Read and display tasks."""
    try:
        initialize_database()

        with sqlite3.connect(DB_FILE) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()

            if not tasks:
                print("No tasks found.")
            else:
                headers = ["ID", "Description", "Scheduled Time", "Lead Time"]
                print(tabulate(tasks, headers=headers, tablefmt="pretty"))

    except sqlite3.Error as e:
        print(f"Error reading tasks: {e}")

if __name__ == '__main__':
    get()
