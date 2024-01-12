from .get_existing_value import get_existing_value
from .print_update_message import print_update_message

def apply_new_lead(cursor, task, new_lead, update_query, update_values):
    if new_lead:
        existing_lead = int(get_existing_value(cursor, "lead_time", task))
        new_lead = int(new_lead)
        if existing_lead == new_lead:
            print(f"\033[38;5;208m• Nothing to update. Task with description '{task}' already has a lead time {new_lead}")
        else:
            update_query += " lead_time = ?,"
            update_values.append(new_lead)
            print_update_message("Lead time", task, new_lead)
    return update_query, update_values
