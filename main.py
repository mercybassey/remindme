import click
from crud import add, delete


@click.group()
def main():
    """Reminder CLI Utility"""

main.add_command(add.add)
main.add_command(delete.delete)

if __name__ == '__main__':
    main()
