# This program uses datetime module to display user's day of birth (with user's input)
import datetime


def day_of_birth(year, month, day):
    """This function displays the day users has been born with users input info"""
    n = datetime.datetime(year, month, day)
    day_born = n.strftime("%A %d %B %Y")
    print("You were born on " + day_born)

day_of_birth(1982, 7, 15)
