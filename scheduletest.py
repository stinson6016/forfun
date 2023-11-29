import schedule 
import time

def something():
    print("something happened")

schedule.every(1).minutes.do(something)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    pass