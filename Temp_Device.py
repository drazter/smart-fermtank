import numpy as np
Temp_Device = {'28-01192df9f63f': 1, '28-01192e036bab': 2, '28-01192e050454': 3,
               '28-01192e14a812': 4, '28-01192e217b99': 5, '28-01192e2a2b66': 6}

temp = np.array([['28-01192e2a2b66', '28-01192e217b99', '28-01192e036bab', '28-01192e050454',
                  '28-01192e14a812', '28-01192df9f63f'], [26.562, 26.687, 26.687, 26.562, 26.75, 26.25]])
temp_new = np.zeros((2, len(Temp_Device)), dtype='object')
print(temp)


def Sort(temp):

    temp_new = np.zeros((2, len(Temp_Device)), dtype='object')

    for i in range(len(Temp_Device)):
        a = 1
    return temp_new


temp_new = Sort(temp)
print(temp_new)
