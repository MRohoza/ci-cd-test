import time
from datetime import datetime, timezone

while True:
    print(
        f"Python app is running: "
        f"{datetime.now(timezone.utc).isoformat()}",
        flush=True,
    )
    time.sleep(15)
