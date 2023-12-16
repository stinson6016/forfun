# testing time for another project

from dateutil.relativedelta import relativedelta
# import datetime
from datetime import date, datetime
# import time

today = date.today()
# print(today + relativedelta(weeks=4))
# print(today + relativedelta(months=1))

datetoday = datetime.now()
current_time = datetoday.strftime("%I:%M:%S %p")
print (current_time)
current_time = datetoday.strftime("%H:%M:00")
print (current_time)


DAY_OF_WEEK = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}


day = datetoday.isoweekday()
print(day)
print(DAY_OF_WEEK[day])