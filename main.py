from src import healthchecks as hc

# TODO:
# - 

def main():
    new_check = hc.create_a_new_check(
        name="New Check",
        tags="example test",
        schedule="* * * * *",
    )
    print(new_check.get("name"))
    print(
        hc.list_existing_checks_pretty(
            headers=["name", "tags", "schedule", "grace", "tz", "uuid"]
        )
    )


if __name__ == "__main__":
    main()
