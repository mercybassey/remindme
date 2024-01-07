import click
from crud.add import add_task

@click.group()
def main():
    """Reminder CLI Utility"""

@main.command()
@click.option("--task", prompt="Task", help="Add a new task")
@click.option("--time", prompt="Scheduled Time (HH:MM)", help="Scheduled time for the task")
@click.option("--lead", default=20, help="Lead time in minutes (default is 20 minutes).")

def add(task, time, lead):
    """Add a new task"""
    add_task(task, time, lead)

if __name__ == '__main__':
    main()
