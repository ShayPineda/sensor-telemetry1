import random
import datetime
import time .

from datetime import datetime
import os

with open("sensor_log.csv", "a") as f:
    if not os.path.exists("sensor_log.csv") or os.path.getsize("sensor_log.csv") == 0:
        f.write("timestamp,temperature,humidity\n")

    for i in range(1, 11):
        rand_temp = round(random.uniform(20.00, 35.00), 1)
        rand_humi = round(random.uniform(30.00, 90.00), 1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        print (f"current time: {current_time} Temp: {rand_temp} Humidity: {rand_humi}")


        if i < 10:
            time.sleep(1)
        
        f.write(f"{current_time}, {rand_temp}, {rand_humi}\n")





