import time
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01

py = Pysense()
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)
next_time = time.time()

# array
rows = 50
cols = 4
sensor_data = [[0] * cols for i in range(rows)]

# Printing out comma seperated values
print("time,temperature,humidity,roll,ptich,yaw")

for cycles in range(50):

    print("Reading sensor values...")

    sensor_data[cycles-1][0] = time.time()
    sensor_data[cycles-1][1] = si.temperature()
    sensor_data[cycles-1][2] = si.humidity()
    sensor_data[cycles-1][3] = li.acceleration()

    # print(lt.light())
    # print(li.roll())
    # print(li.pitch())
    # print(li.yaw())

    next_time +=10
    time.sleep(max(0, next_time - time.time()))

# Battery voltage
print(py.read_battery_voltage())

# Final sensor data
print(sensor_data)
for i in range(0, len(sensor_data)):
    s= ""
    s+= str(sensor_data[i][0])
    s+=","
    s+= str(sensor_data[i][1])
    s+=","
    s+= str(sensor_data[i][2])
    s+=","
    s+= str(sensor_data[i][3])
    print(s)
