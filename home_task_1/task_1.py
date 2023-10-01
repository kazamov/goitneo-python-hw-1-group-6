from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users: list[dict]):
    """Print users who have birthday in current week."""
    if len(users) == 0:
        print("No users found")
        return

    birthdays_list = defaultdict(list)
    current_date = datetime.now().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days=2)
        elif birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days=1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days > 0 and delta_days <= 7:
            birthdays_list[birthday_this_year].append(name)

    if len(birthdays_list) == 0:
        print("No birthdays near 7 days")

    sorted_birthdays_list = sorted(birthdays_list.keys())
    for day in sorted_birthdays_list:
        print(f"{day.strftime('%A')}: {', '.join(birthdays_list[day])}")
