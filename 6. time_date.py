"""
Write a Python program to display the current date and time in UTC
"""

from datetime import datetime, UTC

current_time_date = datetime.now(UTC)
print(current_time_date.strftime("Current date in UTC: %Y/%m/%d \nCurrent time in UTC: %H:%M:%S"))

"""
"datetime" is the  module in the Python's standard library that works with date and time.
UTC: Specifies the UTC timezone and sets the code to work with the UTC time and date.
"""