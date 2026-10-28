from datetime import datetime, timezone
from utils.utils import format_message

def test_format_message():
    now = datetime(2026, 1, 15, 12, 30, tzinfo=timezone.utc)

    result = format_message(now)

    assert result == "Python app is running: 2026-01-15T12:30:00+00:00"
