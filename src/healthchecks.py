# TODO:
# - [x] 与 HealthChecks API 进行交互。
# - [x] 创建 Check 并获取 Ping URL。
# - [x] 列出当前 Host 下的所有 Checks 的时间点。

# Reference:
# - https://healthchecks.io/docs/api/
import requests
from tabulate import tabulate

from .config import (
    HC_PROJECT_READ_WRITE_KEY,
    HC_URL,
    TIMEZONE,
)

# TODO:
# - [ ] 使用 try-expect 提高可靠性和捕获错误
# - [ ] 使用类型注解
# - [ ] 为函数添加 docstring


def list_existing_checks(tag=""):
    HC_API_URL = f"{HC_URL}/api/v3/checks/"
    if tag:
        HC_API_URL += f"?tag={tag}"

    response = requests.get(
        url=HC_API_URL,
        headers={"X-Api-Key": HC_PROJECT_READ_WRITE_KEY},
    )
    return response.json()


def get_a_single_check(uuid):
    HC_API_URL = f"{HC_URL}/api/v3/checks/{uuid}"
    response = requests.get(
        url=HC_API_URL,
        headers={"X-Api-Key": HC_PROJECT_READ_WRITE_KEY},
    )
    return response.json()


def create_a_new_check(
    name,
    schedule,
    tags="",
    desc="",
    grace=300,
    tz=TIMEZONE,
):
    response = requests.post(
        url=f"{HC_URL}/api/v3/checks/",
        headers={"X-Api-Key": HC_PROJECT_READ_WRITE_KEY},
        json={
            "name": name,
            "tags": tags,
            "desc": desc,
            "schedule": schedule,
            "tz": tz,
            "grace": grace,
        },
    )
    return response.json()


def get_a_single_check_pretty(
    uuid, headers=["name", "tags", "schedule", "grace", "tz", "uuid"]
):
    check = get_a_single_check(uuid=uuid)
    return tabulate(
        [[check.get(key) for key in headers]], headers=headers, tablefmt="grid"
    )


def list_existing_checks_pretty(
    tag="",
    headers=["name", "tags", "schedule", "grace", "tz", "uuid"],
):
    checks = list_existing_checks(tag=tag).get("checks", [])
    table = [[check.get(key) for key in headers] for check in checks]
    return tabulate(table, headers=headers, tablefmt="grid")
