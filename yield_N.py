import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# draw grain yield response to N rate

stage = 8
# plt.subplot(3,1,1)
# plt.ylim((0, 240))
# my_y_ticks = np.arange(0, 240, 20)
# plt.xlim((pd.Timestamp(year=2014, month=4, day=28), pd.Timestamp(year=2014, month=9, day=14)))
# plt.yticks(my_y_ticks)

x1 = [None] * stage
x2 = [None] * stage
x3 = [None] * stage
x4 = [None] * stage
x5 = [None] * stage
x6 = [None] * stage
x7 = [None] * stage
x8 = [None] * stage

yld1 = [None] * stage
yld2 = [None] * stage
yld3 = [None] * stage
yld4 = [None] * stage
yld5 = [None] * stage
yld6 = [None] * stage
yld7 = [None] * stage
yld8 = [None] * stage

a = [[0 for i in range(16)] for j in range(8)]
b = [[0 for i in range(16)] for j in range(8)]
m = pd.read_csv('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/plot/ss.csv')
# grain = pd.read_csv(m,sep='\s+')
obs = m['GYdry']
Ntr = m['N']
for i in range(0,8):
    a[i] = Ntr.loc[(i * 16):(i * 16 + 15)]
    b[i] = obs.loc[(i * 16):(i * 16 + 15)] * 0.89


for k in range(0, 8):
    wjj =  40 * k
    # fert = round(40 * k * 8.9, 1)
    f1 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S1B1/' + str(wjj)+'/010112032sccd1')
    data1 = pd.read_csv(f1, sep='\s+')  # define data type
    f1.close()
    c = data1['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld1[k] = c.max()
    x1[k] = wjj

    # fert = round(40 * k * 8.9, 1)
    f2 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S1B2/' + str(wjj)+'/010112032sccd1')
    data2 = pd.read_csv(f2, sep='\s+')  # define data type
    f2.close()
    c2 = data2['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld2[k] = c2.max()
    x2[k] = wjj

    # fert = round(40 * k * 8.9, 1)
    f3 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S1B3/' + str(wjj)+'/010112032sccd1')
    data3 = pd.read_csv(f3, sep='\s+')  # define data type
    f3.close()
    c3 = data3['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld3[k] = c3.max()
    x3[k] = wjj

    f4 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S1B4/' + str(wjj)+'/010112032sccd1')
    data4 = pd.read_csv(f4, sep='\s+')  # define data type
    f4.close()
    c4 = data4['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld4[k] = c4.max()
    x4[k] = wjj

    f5 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S2B1/' + str(wjj)+'/010112032sccd1')
    data5 = pd.read_csv(f5, sep='\s+')  # define data type
    f5.close()
    c5 = data5['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld5[k] = c5.max()
    x5[k] = wjj

    f6 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S2B2/' + str(wjj)+'/010112032sccd1')
    data6 = pd.read_csv(f6, sep='\s+')  # define data type
    f6.close()
    c6 = data6['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld6[k] = c6.max()
    x6[k] = wjj

    f7 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S2B3/' + str(wjj)+'/010112032sccd1')
    data7 = pd.read_csv(f7, sep='\s+')  # define data type
    f7.close()
    c7 = data7['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld7[k] = c7.max()
    x7[k] = wjj

    f8 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S2B4/' + str(wjj)+'/010112032sccd1')
    data8 = pd.read_csv(f8, sep='\s+')  # define data type
    f8.close()
    c8 = data8['GRAIN_C'] * 19.826 # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
    yld8[k] = c8.max()
    x8[k] = wjj


fig = plt.figure(figsize=(48, 16))
plt.subplot(241)
plt.plot(x1, yld1, c = 'blue')
plt.scatter(a[0],b[0],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S1B1', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(242)
plt.plot(x2, yld2, c = 'blue')
plt.scatter(a[1],b[1],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S1B2', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(243)
plt.plot(x3, yld3, c = 'blue')
plt.scatter(a[2],b[2],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S1B3', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(244)
plt.plot(x4, yld4, c = 'blue')
plt.scatter(a[3],b[3],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S1B4', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(245)
plt.plot(x5, yld5, c = 'blue')
plt.scatter(a[4],b[4],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S2B1', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(246)
plt.plot(x6, yld6, c = 'blue')
plt.scatter(a[5],b[5],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S2B2', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(247)
plt.plot(x7, yld7, c = 'blue')
plt.scatter(a[6],b[6],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S2B3', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.subplot(248)
plt.plot(x8, yld8, c = 'blue')
plt.scatter(a[7],b[7],c='red')
plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 20)
plt.ylabel('Grain yield (lb/acre)', fontsize = 20)
plt.title('S2B4', fontsize = 22)
plt.legend(labels=['simulations', 'experiments'], fontsize = 18)
plt.tick_params(labelsize=18)

plt.savefig('yield-N_old.png')
# plt.show()

