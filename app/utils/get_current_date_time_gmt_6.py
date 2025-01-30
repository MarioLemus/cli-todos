from zoneinfo import ZoneInfo
from datetime import datetime

def current_date_time():
    gmt_6 = ZoneInfo('America/El_Salvador')
    current_date_time = datetime.now(gmt_6)
    current_date = current_date_time.date()
    current_time = current_date_time.time()
    return {'time': current_time.isoformat(), 'date': current_date.isoformat()}


