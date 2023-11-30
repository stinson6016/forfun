# testing time for another project

from dateutil.relativedelta import relativedelta
# import datetime
from datetime import date, datetime

today = date.today()
print(today + relativedelta(weeks=4))
print(today + relativedelta(months=1))

print(datetime.now())