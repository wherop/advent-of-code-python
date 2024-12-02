from datetime import datetime
import pytz


def get_est_now():
    # AoC challenges are released at midnight based on EST time

    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)

    # Convert to EST (Eastern Standard Time)
    est = pytz.timezone("US/Eastern")
    return utc_now.astimezone(est)


def get_year():
    est_now = get_est_now()

    # Assumes if it's not December currently, 
    # then user wants to work on last year's challenges
    if est_now.month < 12:
        year = est_now.year - 1
    else:
        year = est_now.year
    return year


def get_day():
    est_now = get_est_now()

    # If it's not an advent day currently, 
    # assumes user wants to start with day one.
    # Does not check whether any days from chosen year already exist.
    if est_now.month == 12 and est_now.day in range(1, 26):
        return est_now.day
    else:
        return 1
