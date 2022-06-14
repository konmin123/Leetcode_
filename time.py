from datetime import datetime, timedelta


def current_time():
    return (datetime.now() + timedelta(hours=24))



print(current_time())