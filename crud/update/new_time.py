from .get_existing_value import get_existing_value
from .print_update_message import print_update_message

def apply_new_time(cursor, task, new_time, update_query, update_values):
    if new_time:
        existing_scheduled_time = get_existing_value(cursor, "scheduled_time", task)
        if existing_scheduled_time == new_time:
            print(f"\033[38;5;208m• Nothing to update. Task with description '{task}' already has time set to '{new_time}'")
        else:
            update_query += " scheduled_time = ?,"
            update_values.append(new_time)
            print_update_message("Time", task, new_time)
    return update_query, update_values
