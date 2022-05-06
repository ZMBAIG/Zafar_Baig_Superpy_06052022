# This set out a comparison of different schedules in stipulated dates in inventory database. The query is simply made by entering negative number of days, which print inventory report of the past days.(e.g. python3 main.py expire -nd -30) The default is zero number of days indicates inventory report publish for today.

import argparse
from expiry_schedule import to_get_expire_report_processed, to_acquire_expired_report_today
from datetime import date, timedelta, datetime

parser = argparse.ArgumentParser()
parser.add_argument("-num", required=False,description="Advance date with specified number of days", help="Enter number of days you wish to advance. Number of days (days in the past: negative value). Default: 0 (zero).") # e.g. python3 main.py expire -nd -20
parser.add_argument("-date", required=False, help="Date if start_date is NOT today (input yyyy-mm-dd). Default: today.") # e.g. python3 main.py expire -nd 0
args = vars(parser.parse_args())

if args["num"] == None:
    number_of_days = 0
else:
    number_of_days = int(args["num"])
    
if args["date"] == None:
    get_process_date = date.today()
else:
    get_process_date = date.fromisoformat(args["date"])

# print (f"\n Advance date with specified number of days")
to_get_expire_report_processed(get_process_date, number_of_days )
