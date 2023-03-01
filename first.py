import sys
import os
import datetime
import time

print(sys.version)
print(os.getcwd())
# print(os.environ)
print(datetime.date.today())

#exercise date, month, year print

# display user friendly time
print(datetime.date.isoformat(datetime.date.today()))

#print the time week name and hour format
print(time.strftime('%H %M %A %P'))