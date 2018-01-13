from datetime import datetime, timedelta

def split_time(num_ranges):
    interval = timedelta(hours=1)
    now = datetime.now()
    intervals = [now]
    time = now.replace(microsecond=0, second=0, minute=0)
    intervals.append(time)
    for i in range(num_ranges):
        time = time - interval
        intervals.append(time)
    return intervals
