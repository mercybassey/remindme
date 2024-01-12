import click
from crud import add, delete, read
from crud.update import update


@click.group()

def main():
    """Reminder CLI Utility"""

main.add_command(add.add)
main.add_command(delete.delete)
main.add_command(update.update)
main.add_command(read.get)


if __name__ == '__main__':
    main()
