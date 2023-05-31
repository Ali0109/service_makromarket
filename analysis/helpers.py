import calendar
from . import exceptions


def get_start_end_month_by_year_month(year, month):
    year = int(year)
    month = int(month)
    if month > 12 or month < 1:
        raise exceptions.DateErrorException()
    _, last_day = calendar.monthrange(year, month)
    date_created_start = f"{year}-{month}-01"
    date_created_end = f"{year}-{month}-{last_day}"
    return {"start": date_created_start, "end": date_created_end}
