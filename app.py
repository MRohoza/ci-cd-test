import time
from datetime import datetime, timezone
from utils.utils import format_message


def main():
    while True:
        print(format_message(datetime.now(timezone.utc)), flush=True)
        time.sleep(11)


if __name__ == "__main__":
    main()
