def new_check():
    from .config import TIMEZONE
    from .utils import get_hostname

    return {
        "name": input("name> "),
        "schedule": new_oncalendar(),
        "tags": input("tags(default: $hostname)> ") or get_hostname(),
        "desc": input("desc> "),
        "grace": int(input("grace(default: 300)> ") or 300),
        "tz": input(f"tz(default: {TIMEZONE})> ") or TIMEZONE,
    }


def new_oncalendar():
    from .utils import verify_oncalendar

    while True:
        oncalendar = input("oncalendar> ")
        if verify_oncalendar(oncalendar):
            return oncalendar
