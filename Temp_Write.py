# Import time library
from time import strftime

# Write date/time device number and temperatureto csv file


def write_temp(device_num, temp):
    with open('/home/pi/Desktop/Tank Temperature/Temp_Log.csv', 'a') as log:
        for i in range(temp.size):
            log.write('{0},{1},{2},\n'.format(
                strftime("%Y-%m-%d %H:%M:%S"), device_num[i], temp[i]))
