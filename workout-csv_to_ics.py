"""
Converts a Toggl CSV to ICS.
"""


import sys
# Yeah this is a hack
sys.path.append('.')

from convert import Convert
from datetime import datetime

convert = Convert()
convert.CSV_FILE_LOCATION = 'workout.csv'
convert.SAVE_LOCATION = 'workout.ics'
convert.HEADER_COLUMNS_TO_SKIP = 1
convert.NAME = 0
togglDESCRIPTION = 5
togglUSERNAME = 0
convert.START_DATE = 1
togglSTART_TIME = 2
convert.END_DATE = 3
togglEND_TIME = 4
convert.DESCRIPTION = 6
convert.LOCATION = 7

convert.read_csv()
for row in convert.csv_data:
    row[convert.NAME] = row[convert.NAME]
    row[convert.START_DATE] = datetime.strptime(row[convert.START_DATE]+' '+row[togglSTART_TIME], '%m/%d/%y %H:%M %p')
    row[convert.END_DATE] = datetime.strptime(row[convert.END_DATE]+' '+row[togglEND_TIME], '%m/%d/%y %H:%M %p')
    row[convert.DESCRIPTION] = 'tags: '+row[convert.DESCRIPTION]
    row[convert.LOCATION] = ""
convert.make_ical()
convert.save_ical()
