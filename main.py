import click
from crud import add, delete, update


@click.group()
def main():
    """Reminder CLI Utility"""

main.add_command(add.add)
main.add_command(delete.delete)
main.add_command(update.update)

if __name__ == '__main__':
    main()
