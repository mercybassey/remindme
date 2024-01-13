from datetime import timedelta

def is_valid_lead_time(current_time, scheduled_time, lead_time):
    lead_duration = scheduled_time - current_time

    return lead_duration >= timedelta(minutes=lead_time)



