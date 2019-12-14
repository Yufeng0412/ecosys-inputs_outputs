import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# draw carbon allocations

stage = 8

yld1 = [None] * stage
yld2 = [None] * stage
yld3 = [None] * stage
yld4 = [None] * stage
yld5 = [None] * stage
yld6 = [None] * stage
yld7 = [None] * stage
yld8 = [None] * stage
yld9 = [None] * stage


x1 = [None] * stage
x2 = [None] * stage
x3 = [None] * stage
x4 = [None] * stage
x5 = [None] * stage
x6 = [None] * stage
x7 = [None] * stage
x8 = [None] * stage
x9 = [None] * stage


f1 = open('C:/Users/yyf/Desktop/Ecosys materials/data_pioneer/sites_MN/Nrates/S1B2/0/010112032scnd1')
data = pd.read_csv(f1, sep='\s+')  # define data type
f1.close()
# c1 = data['GPP']
c2 = data['LEAF_N']
c3 = data['SHTH_N']
c4 = data['STALK_N']
c5 = data['RESERVE_N']
c6 = data['REPRO_N']
c7 = data['GRAIN_N']
c8 = data['ROOT_N']
c9 = data['LITTER_N']

# yld1 = c1
x1 = data ['DOY']
yld2 = c2
x2 = data ['DOY']
yld3 = c2+c3
x3 = data ['DOY']
yld4 = c2+c3+c4
x4 = data ['DOY']
yld5 = c2+c3+c4+c5
x5 = data ['DOY']
yld6 = c2+c3+c4+c5+c6
x6 = data ['DOY']
yld7 = c2+c3+c4+c5+c6+c7
x7 = data ['DOY']
yld8 = c2+c3+c4+c5+c6+c7+c8
x8 = data ['DOY']
yld9 = c2+c3+c4+c5+c6+c7+c8+c9
x9 = data ['DOY']


# draw MRTN figures
fig = plt.figure(figsize=(12, 8))
plt.xlim(100, 288)
plt.ylim(0, 35)
# plt.scatter(x_exp, yld_exp, s=100, c='purple')
# plt.plot(x1, yld1)
plt.plot(x2, yld2)
plt.plot(x3, yld3)
plt.plot(x4, yld4)
plt.plot(x5, yld5)
plt.plot(x6, yld6)
plt.plot(x7, yld7)
plt.plot(x8, yld8)
plt.plot(x9, yld9)

# plt.scatter(a,b,c='red')

plt.gca().fill_between(x1,0,yld2)
plt.gca().fill_between(x1,yld2,yld3)
plt.gca().fill_between(x1,yld3,yld4)
plt.gca().fill_between(x1,yld4,yld5)
plt.gca().fill_between(x1,yld5,yld7)
plt.gca().fill_between(x1,yld6,yld7)
plt.gca().fill_between(x1,yld7,yld8)
plt.gca().fill_between(x1,yld8,yld9)


plt.xlabel('DOY', fontsize = 18)
plt.ylabel('g N/m2', fontsize = 18)
plt.title('N allocation(S1B2_N0)', fontsize = 20)
# plt.legend(labels=['Leaf_C', 'Sheath_C', 'Stalk_C', 'Reserve_C', 'Reproduction_C','Grain_C', 'Root_C', 'Litter_C'], fontsize = 18)
plt.legend(labels=['Leaf_N', 'Sheath_N', 'Stalk_N', 'Reserve_N', 'Grain_N', 'Root_N', 'Litter_N'], fontsize = 18)
plt.tick_params(labelsize=16)
plt.savefig('N allocation(S2B2_N0).png')
# plt.show()