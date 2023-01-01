# Given a date, return the total days between the current date and the date

from datetime import date


def days_between(date_given):
    days_split = date_given.split("-")
    [year, month, day] = [int(x) for x in days_split]
    current_date = date.today()
    result = current_date - date(year, month, day)
    print(f"Between {date_given} and the current date {current_date} there's: {result.days} day/s")


days_between("2022-12-31")
# Returns "Between 2022-12-31 and the current date 2023-01-01 there's: 1 day/s"