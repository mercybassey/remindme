from datetime import datetime

def validate_time_format(time):
    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False