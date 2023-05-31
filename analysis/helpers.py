import calendar
import datetime

from . import exceptions


def get_start_end_by_month(year, month) -> dict:
    year = int(year)
    month = int(month)
    if month > 12 or month < 1:
        raise exceptions.DateErrorException()
    _, last_day = calendar.monthrange(year, month)
    date_created_start = f"{year}-{month}-01"
    date_created_end = f"{year}-{month}-{last_day}"
    return {"start": date_created_start, "end": date_created_end}


def get_start_end_by_day(year, month, day) -> dict:
    year = int(year)
    month = int(month)
    day = int(day)
    _, last_day = calendar.monthrange(year, month)
    if month > 12 or month < 1 or day > last_day:
        raise exceptions.DateErrorException()
    current_day = datetime.date(year, month, day)
    next_day = current_day + datetime.timedelta(days=1)
    return {"now": current_day, 'next': next_day}
