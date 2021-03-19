import os
import glob
import time
import numpy as np
import Temp_Upload
import Temp_Write

os.system('modprobe w1-gpio')  # import gpio
os.system('modprobe w1-therm')  # import sensor

base_dir = '/sys/bus/w1/devices/'  # set base directory
# set the device folder [list] as folder with 28 in them
device_folder = glob.glob(base_dir + '28*')
device_file = []  # declare list
for i in range(len(device_folder)):  # add w1_slave to all of the directory
    device_file.append(device_folder[i] + '/w1_slave')

device_folder.sort()  # sort folder by number
device_file.sort()  # Sort device file by number


def read_temp_raw(num):  # This function reads raw temperature file
    f = open(device_file[num], 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(num):  # Extract only the temperature value from raw file
    lines = read_temp_raw(num)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(num)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


temp = np.zeros(len(device_folder))  # Create Empty temp array
device_num = []  # Create list to store device number

for i in range(len(device_folder)):  # Store device number
    device_num.append(device_folder[i][-15:])

while True:  # This loop read value from all available sensor
    for i in range(len(device_folder)):
        temp[i] = read_temp(i)
        print('Device Number:%s Temp:%0.2f Celcius' % (device_num[i], temp[i]))
    print('')
    Temp_Upload.upload(temp)  # Upload Temperature
    # save temperature value to csv file
    Temp_Write.write_temp(device_num, temp)
    time.sleep(600)
