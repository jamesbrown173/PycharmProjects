import json
import os
import pprint

from datetime import date, timedelta
from oura import OuraClient

soup = OuraClient(personal_access_token="57YMETS637H5XH6FUASL6OPKTAPJXHLU")

# Get today's date
today = date.today()
print("Today's date:", today)

# Calculate yesterday's date
yesterday = str(today - timedelta(days=1))
print("Yesterday's date:", yesterday)

# Assign variables to all available information
user_info = soup.user_info()
sleep_summary = soup.sleep_summary(start=yesterday)
activity_summary = soup.activity_summary(start=yesterday)
bedtime_summary = soup.bedtime_summary(start=yesterday)
readiness_summary = soup.readiness_summary(start=yesterday)


# Print all available information
print(f"Your user information is ......\n\n {user_info}\n")
print(f"Your sleep summary is ......\n\n {sleep_summary}\n")
print(f"Your bedtime summary is ......\n\n {bedtime_summary}\n")
print(f"Your readiness summary is ......\n\n {readiness_summary}\n")





#  TODO Assign values onto previous day for sleep Start, HRV,
#   HR and current day for sleep end? or complete in sheets


