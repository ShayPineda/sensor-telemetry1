import random
import datetime
import time 
from datetime import datetime
import os
import matplotlib.pyplot as plt

def generate_readings():
    rand_temp = round(random.uniform(20.00, 35.00), 1)
    rand_humi = round(random.uniform(30.00, 90.00), 1)
    return rand_temp, rand_humi

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def log_readings():
    with open("sensor_log.csv", "a") as f:
        if not os.path.exists("sensor_log.csv") or os.path.getsize("sensor_log.csv") == 0:
            f.write("timestamp,temperature,humidity\n")

        temperatures = []
        humidities = []

        for i in range(1, 11):
            rand_temp, rand_humi = generate_readings()
            current_time = get_time()
            print (f"current time: {current_time} Temp: {rand_temp} Humidity: {rand_humi}")
            temperatures.append(rand_temp)
            humidities.append(rand_humi)



            if i < 10:
                time.sleep(1)
            
            f.write(f"{current_time}, {rand_temp}, {rand_humi}\n")
        plot_readings(temperatures, humidities)


def plot_readings(temperatures, humidities):
    readings = list(range(1,11))

    plt.plot(readings, temperatures, label = "Temperature (°C)")
    plt.plot(readings, humidities, label = "Humidity")
    plt.title ("Temp and Humitity")
    plt.xlabel("Reading")
    plt.ylabel("Temperature (°C) / Humidity (%)")
    plt.legend()
    plt.savefig("sensor_chart.png")


log_readings()



