import os
import math
import time
import csv
from datetime import datetime
now = datetime.now()
filename = '%02d-%02d-%04d_%02d-%02d-%02d.csv' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
#filename = "testing" + str(now.second) + ".csv"
write_header = not os.path.exists(filename) or os.stat(filename).st_size == 0


with open(filename, "a") as f_output:
    csv_output = csv.writer(f_output)

    if write_header:
        csv_output.writerow(["hour","second","minute"])

    while True:
        now = datetime.now()
        row = [(now.hour), (now.minute), (now.second)]
        csv_output.writerow(row)
        time.sleep(.1)
        #f_output.flush()
