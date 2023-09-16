from datetime import datetime, timedelta, timezone


def get_taipei_timezone():
    return timezone(timedelta(hours=8))


def get_current():
    current = datetime.now(tz=get_taipei_timezone())
    current = current.replace(second=0, microsecond=0)
    return current


def str2date(string: str):
    date = datetime.fromisoformat(string)
    date = date.replace(second=0, microsecond=0, tzinfo=get_taipei_timezone())
    return date
