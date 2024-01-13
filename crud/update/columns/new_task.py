from ..utils.get_existing_value import get_existing_value
from ..utils.print_update_message import print_update_message

def apply_new_task(cursor, task, new_task, update_query, update_values):
    if new_task:
        cursor.execute("SELECT 1 FROM tasks WHERE description = ?", (new_task,))
        exists = cursor.fetchone()

        if exists is not None:
            print(f"\033[38;5;208m• Task with description '{new_task}' already exists. No updates performed.")
            return update_query, update_values

        existing_description = get_existing_value(cursor, "description", task)
        if existing_description == new_task:
            print(f"\033[38;5;208m• Nothing to update. Task with description '{task}' already has the description '{new_task}'")
        else:
            update_query += " description = ?,"
            update_values.append(new_task)
            print_update_message("Description", task, new_task)
    return update_query, update_values
