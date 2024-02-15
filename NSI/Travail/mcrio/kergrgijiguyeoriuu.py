from psutil import sensors_temperatures
from time import sleep
from random import randint



while True:
    print(int(sensors_temperatures()['coretemp'][1][1]+273),"K")
    sleep(2)
