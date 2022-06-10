import datetime
import time

now = time.time()
print(datetime.datetime.fromtimestamp(now))

today = datetime.datetime.now()
print(datetime.datetime.timestamp(today))
