from datetime import datetime, date
import re
from zoneinfo import ZoneInfo


def get_date(value: str) -> date:
    """
    Extracts a date from a string containing a JSON-like key-value pair.

    The function looks for a pattern like '"date":"YYYY-MM-DD"' in the input string,
    parses the date, and returns it as a `datetime.date` object. If the input is None
    or the expected date pattern is not found, it returns `date.min`.

    Args:
        value (str): A string potentially containing a "date" field in the format "YYYY-MM-DD".

    Returns:
        date: The extracted date, or `date.min` if no valid date is found.
    """

    if value is None:
        return date.min

    match = re.search(r'"date":"([\d\-]+)"', value)
    if not match:
        return date.min

    date_str, = match.groups()
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def get_time(value: str) -> datetime:
    """
    Extracts a datetime from a JSON-like string containing "date" and "time" fields.

    The function searches for the pattern '"date":"YYYY-MM-DD","time":"HH:MM[:SS]"' in the input string.
    If found, it constructs an ISO 8601 datetime string in UTC, parses it, and converts it to
    the "America/Chicago" timezone. If the input is None or the pattern is not found, it returns `datetime.min`.

    Args:
        value (str): A string potentially containing "date" and "time" fields.

    Returns:
        datetime: The parsed datetime object converted to "America/Chicago" timezone,
                  or `datetime.min` if parsing fails.
    """
    if not value:
        return datetime.min

    match = re.search(r'"date":"([\d\-]+)","time":"([\d:]+)"', value)
    if not match:
        return datetime.min

    date_str, time_str = match.groups()

    try:
        dt_utc = datetime.fromisoformat(f"{date_str}T{time_str}+00:00")
        return dt_utc.astimezone(ZoneInfo("America/Chicago"))
    except ValueError:
        return datetime.min