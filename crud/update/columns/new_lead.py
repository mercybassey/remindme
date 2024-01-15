from datetime import datetime

from crud.utils.lead_time_validation import is_valid_lead_time
from ..utils.get_existing_value import get_existing_value
from ..utils.print_update_message import print_update_message

def convert_time_str_to_datetime(time_str):
    if time_str:
        return datetime.strptime(time_str, "%H:%M")
    else:
        return None

def validate_and_apply_lead(cursor, task, new_lead, new_time, update_query, update_values):
    if new_lead:
        try:
            new_lead = int(new_lead)
        except ValueError:
            print("\033[91m✘ Lead time must be an integer\033[0m")
            return update_query, update_values

        existing_lead = int(get_existing_value(cursor, "lead_time", task))
        new_lead = int(new_lead)

        existing_time = convert_time_str_to_datetime(get_existing_value(cursor, "scheduled_time", task))
        current_time = convert_time_str_to_datetime(datetime.now().strftime("%H:%M"))

        if existing_time and not is_valid_lead_time(current_time, existing_time, new_lead):
            print("\033[91m✘ Invalid lead time. Lead time must be a positive duration from the current time to the scheduled time\033[0m")
            return update_query, update_values

        if existing_lead == new_lead:
            print(f"\033[38;5;208m• Nothing to update. Task with description '{task}' already has a lead time {new_lead}")
        else:
            update_query += " lead_time = ?,"
            update_values.append(new_lead)
            print_update_message("Lead time", task, new_lead)

    return update_query, update_values
