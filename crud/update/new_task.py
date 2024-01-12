from .get_existing_value import get_existing_value
from .print_update_message import print_update_message

def apply_new_task(cursor, task, new_task, update_query, update_values):
    if new_task:
        existing_description = get_existing_value(cursor, "description", task)
        if existing_description == new_task:
            print(f"\033[38;5;208m• Nothing to update. Task with description '{task}' already has the description '{new_task}'")
        else:
            update_query += " description = ?,"
            update_values.append(new_task)
            print_update_message("Description", task, new_task)
    return update_query, update_values
