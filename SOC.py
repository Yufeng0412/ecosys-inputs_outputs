import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# m = pd.read_csv('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/POC/C0/outputs/010112032sccd1')
# # grain = pd.read_csv(m,sep='\s+')
# obs = m['GYdry']
# Ntr = m['N']
fig = plt.figure(figsize=(12, 10))

for year in range(2016, 2034):
    f1 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/revision/changeAll/spinup_N60/S2B4/0/01010' + str(year)+ 'sccd1')
    data1 = pd.read_csv(f1, sep='\s+',dtype={'DATE':str})
    if year == 2016:
        data = data1
    else:
        data = data.append(data1)
# all['index'] = np.arange(0, len(all))
# a = all['index']
x = pd.to_datetime(data['DATE'].astype(str),format="%d%m%Y")
for i in range(1,13):
    a = data['SOC_'+ str(i)]
    if i == 1:
        y1 = a
        y2 = a
        y3 = a
    elif i < 5:
        y1 = y1 + a
        y2 = y2 + a
        y3 = y3 + a
    elif i < 9:
        y2 = y2 + a
        y3 = y3 + a
    else:
        y3 = y3 + a

# y1 = all['SOC_2']
# y2 = all['SOC_3']
# y3 = all['SOC_4']



plt.subplot(311)
plt.plot(x, y1)
# plt.xlabel('DOY', fontsize=20)
plt.ylabel('SOC_5 (g C/m2)', fontsize=16)
plt.title('S2B4', fontsize=18)
# plt.legend(labels=['N0', 'N40', 'N80', 'N120', 'N160', 'N200', 'N240', 'N280'], fontsize = 12)
plt.tick_params(labelsize=16)

plt.subplot(312)
plt.plot(x, y2)
# plt.xlabel('DOY', fontsize=20)
plt.ylabel('SOC_10 (g C/m2)', fontsize=18)
# plt.title('S1B1', fontsize=22)
# plt.legend(labels=['N0', 'N40', 'N80', 'N120', 'N160', 'N200', 'N240', 'N280'], fontsize = 18)
plt.tick_params(labelsize=16)

plt.subplot(313)
plt.plot(x, y3)
plt.xlabel('time', fontsize=18)
plt.ylabel('SOC_15 (g C/m2)', fontsize=18)
# plt.title('S1B1', fontsize=22)
# plt.legend(labels=['N0', 'N40', 'N80', 'N120', 'N160', 'N200', 'N240', 'N280'], fontsize = 18)
plt.tick_params(labelsize=16)

# plt.savefig('new/spinup_N60/SOC_spinup_S2B4.png')
plt.show()