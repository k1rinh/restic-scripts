def verify_oncalendar(oncalendar: str):
    from datetime import datetime

    from oncalendar import BaseIterator, OnCalendarError

    from .config import TIMEZONE

    try:
        it = BaseIterator(oncalendar, datetime.now())
        print(f"预期 Ping 时间（{TIMEZONE}）：")
        for i in range(0, 5):
            print(f"#{i + 1}: {next(it)}")
        return True
    except OnCalendarError:
        print("无效 OnCalendar 表达式")
        return False


def get_hostname():
    import socket

    hostname = socket.gethostname()
    return hostname
