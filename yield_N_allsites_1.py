import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# draw grain yield response to N rate

def init_1d(treats_num):
    return [None for i in range(treats_num)]
def init_2d(treats_num,site_num):
    return [[None for i in range(treats_num)] for j in range(site_num)]
    
sites = ['S1B1_2014','S1B2_2014','S1B3_2014','S1B4_2014','S2B1_2014','S2B2_2014','S2B3_2014','S2B4_2014']
# sites = ['S1B1_2015','S1B2_2015','S1B3_2015','S1B4_2015','S2B1_2015','S2B2_2015','S2B3_2015','S2B4_2015']

# groups according to planting_sidedress nitrogen treatments
total_treats = ['0_0','40_0','80_0','120_0','160_0','200_0','240_0','280_0',
                '40_40','40_80','40_120','40_160','40_200','40_240',
                '80_80','80_160']
group_1 = ['0_0','40_0','80_0','120_0','160_0','200_0','240_0','280_0']
group_2 = ['40_0','40_40','40_80','40_120','40_160','40_200','40_240']
group_3 = ['80_0','80_80','80_160']


x1 = init_1d(len(group_1))
x2 = init_1d(len(group_2))
x3 = init_1d(len(group_3))
yld1 = init_1d(len(group_1))
yld2 = init_1d(len(group_2))
yld3 = init_1d(len(group_3))
x = {}
sim_yld = {}
#
T_N = init_2d(len(total_treats),len(sites))
P_N = init_2d(len(total_treats),len(sites))
S_N = init_2d(len(total_treats),len(sites))
obs_yld = init_2d(len(total_treats),len(sites))
# T_N1 = np.zeros([8, 8])
T_N1 = init_2d(len(group_1),len(sites))
T_N2 = init_2d(len(group_2),len(sites))
T_N3 = init_2d(len(group_3),len(sites))
obs_yld1 = init_2d(len(group_1),len(sites))
obs_yld2 = init_2d(len(group_2),len(sites))
obs_yld3 = init_2d(len(group_3),len(sites))

m = pd.read_csv('./yield_Nrates.csv')
# grain = pd.read_csv(m,sep='\s+')
obs = m['GYdry']
Ntr1 = m['Total_N']
Ntr2 = m['Plant_N']
Ntr3 = m['Side_N']
for i in range(0,8):
    T_N[i] = Ntr1.loc[(i * 16):(i * 16 + 15)]
    P_N[i] = Ntr2.loc[(i * 16):(i * 16 + 15)]
    S_N[i] = Ntr3.loc[(i * 16):(i * 16 + 15)]
    obs_yld[i] = obs.loc[(i * 16):(i * 16 + 15)] * 0.89


sites = ['S1B1_2014','S1B2_2014','S1B3_2014','S1B4_2014','S2B1_2014','S2B2_2014','S2B3_2014','S2B4_2014']
# sites = ['S1B1_2015','S1B2_2015','S1B3_2015','S1B4_2015','S2B1_2015','S2B2_2015','S2B3_2015','S2B4_2015']
fig = plt.figure(1, figsize=(40, 16))
fig_plc = 1
for i, site in enumerate(sites):

    for k in range(0, 8):
        if k < 3:
            N1 = 40 * k
            f1 = open('./' + site + '/' + str(N1) + '_0/010112014sccd1')
            data1 = pd.read_csv(f1, sep='\s+')  # define data type
            f1.close()
            c1 = data1['GRAIN_C'] * 19.826  # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
            yld1[k] = c1.max()
            x1[k] = N1

            N2 = 40 * k
            f2 = open('./' + site + '/40_' + str(N2) + '/010112014sccd1')
            data2 = pd.read_csv(f2, sep='\s+')  # define data type
            f2.close()
            c2 = data2['GRAIN_C'] * 19.826
            yld2[k] = c2.max()
            x2[k] = N2 + 40

            N3 = 80 * k
            f3 = open('./' + site + '/80_' + str(N3)+'/010112014sccd1')
            data3 = pd.read_csv(f3, sep='\s+')  # define data type
            f3.close()
            c3 = data3['GRAIN_C'] * 19.826
            yld3[k] = c3.max()
            x3[k] = N3 + 80
        elif k < 7:
            N1 = 40 * k
            f1 = open('./' + site + '/' + str(N1) + '_0/010112014sccd1')
            data1 = pd.read_csv(f1, sep='\s+')  # define data type
            f1.close()
            c1 = data1['GRAIN_C'] * 19.826  # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
            yld1[k] = c1.max()
            x1[k] = N1

            N2 = 40 * k
            f2 = open('./' + site + '/40_' + str(N2)+'/010112014sccd1')
            data2 = pd.read_csv(f2, sep='\s+')  # define data type
            f2.close()
            c2 = data2['GRAIN_C'] * 19.826
            yld2[k] = c2.max()
            x2[k] = N2 + 40
        else:
            N1 = 40 * k
            f1 = open('./' + site + '/' + str(N1) + '_0/010112014sccd1')
            data1 = pd.read_csv(f1, sep='\s+')  # define data type
            f1.close()
            c1 = data1['GRAIN_C'] * 19.826  # g/m2 -> lb/acre, *8.9 / 0.45 = * 19.826
            yld1[k] = c1.max()
            x1[k] = N1

    index1 = np.argwhere(S_N[i] == 0)
    T_N1[i] = np.array(T_N[i])[index1]
    obs_yld1[i] = np.array(obs_yld[i])[index1]
    index2 = np.argwhere(P_N[i] == 40)
    T_N2[i] = np.array(T_N[i])[index2]
    obs_yld2[i] = np.array(obs_yld[i])[index2]
    index3 = np.argwhere(P_N[i] == 80)
    T_N3[i] = np.array(T_N[i])[index3]
    obs_yld3[i] = np.array(obs_yld[i])[index3]

    x[site] = x1[:]
    x[site].append(x2[:])
    x[site].append(x3[:])
    sim_yld[site] = yld1[:]
    sim_yld[site].append(yld2[:])
    sim_yld[site].append(yld3[:])
 
    plt.subplot(2,4,fig_plc)

    plt.plot(x1, yld1,linewidth = 2)
    plt.plot(x2, yld2, linewidth = 2)
    plt.plot(x3, yld3, linewidth = 2)
    plt.scatter(T_N1[i], obs_yld1[i], s=200, marker = '.')
    plt.scatter(T_N2[i], obs_yld2[i], s=150, marker = '*')
    plt.scatter(T_N3[i], obs_yld3[i], s=150, marker = '+')
    if fig_plc ==1:
        plt.ylabel('Grain yield (lb/acre)', fontsize = 24)
        plt.legend(labels=['simulated (Side N=0)', 'simulated (Plant N=40)', 'simulated (Plant N=80)',
                           'observed (Side N=0)', 'observed (Plant N=40)', 'observed (Plant N=80)'], fontsize=18)
    if fig_plc > 4:
        plt.ylim(2000, 12000)
        plt.xlabel('Nitrogen rate (lb/acre)', fontsize = 24)
    if fig_plc == 5:
        plt.ylabel('Grain yield (lb/acre)', fontsize = 24)
    if fig_plc < 5:
        plt.ylim(2000, 10000)
        # plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_ticklabels([])
    else:
        plt.ylim(2000, 12000)
    if fig_plc != 1 and fig_plc != 5:
        # plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_ticklabels([])
    plt.title('{}'.format(site), fontsize=24)
    plt.tick_params(labelsize=20)
    fig_plc += 1
#
plt.savefig('yield_N_allsites_1.png')
x = pd.DataFrame(x) 
sim_yld = pd.DataFrame(sim_yld) 
x.to_csv('N rates_S1S2.csv',index = 0)
sim_yld.to_csv('simulated yield_S1S2.csv',index = 0)
# plt.show()

