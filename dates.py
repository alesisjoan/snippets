from datetime import datetime, timedelta
from calendar import monthrange
def _get_orden():
    day = datetime.today().day
    lastday = monthrange(int(_get_year()), int(_get_month()))[1]
    if 10 < day <= 15:
        return '2'
    if (lastday - 5) < day <= lastday:
        return '1'
    return '-1'


def _get_year():
    return str((datetime.today() + timedelta(6)).year)  # hoy + 6 dias
def _get_month():
    return str((datetime.today() + timedelta(6)).month).zfill(2)
def _get_periodo():
    return _get_year() + _get_month()


