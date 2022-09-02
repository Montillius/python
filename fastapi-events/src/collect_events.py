import datetime as _dt
from typing import Iterator, Dict

def _date_range(start_date: _dt.date, end_date: _dt.date)-> Iterator[_dt.date]
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)
        
def create_events_dict() -> Dict:
    events = dict()
    star_date = _dt.date(2020, 1, 1)