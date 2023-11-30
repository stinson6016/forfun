import schedule 
import time

def something():
    print("something happened")

if __name__ == "__main__":
    print('start up')
    schedule.every(20).seconds.do(something)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("ending")