
def validate_time_value(time_str):
    try:
        hour, minute = map(int, time_str.split(":"))
        if 0 <= hour < 24 and 0 <= minute < 60:
            return True
        else:
            return False
    except ValueError:
        return False

def check_time_format(time_str):
    if time_str.count(":") != 1:
        print(f"\033[91m✘ Valid time should be in hours:minutes format")
        return False
    elif validate_time_value(time_str) == False:
        print(f"\033[91m✘ The time {time_str} is invalid. Please use a time of 24 hours or less.")
        return False
    else:
        return True

