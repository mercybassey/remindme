from ..utils.get_existing_value import get_existing_value
from ..utils.print_update_message import print_update_message

from crud.utils.validate_time import check_time_format


def apply_new_time(cursor, task, new_time, update_query, update_values):
    existing_scheduled_time = get_existing_value(cursor, "scheduled_time", task)

    if existing_scheduled_time is None:
        print(f"\033[38;5;208m• Task with description '{task}' does not exist. No updates performed.")
        return update_query, update_values
    
    if new_time is None:
        return update_query, update_values
    
    if not check_time_format(new_time):
        return update_query, update_values


    if new_time is not None and existing_scheduled_time != new_time:
        update_query += " scheduled_time = ?,"
        update_values.append(new_time)
        print_update_message("Time", task, new_time)

    return update_query, update_values
