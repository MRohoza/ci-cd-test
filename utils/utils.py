from datetime import datetime


def format_message(now: datetime):
    return f"Python app is running: {now.isoformat()}"
