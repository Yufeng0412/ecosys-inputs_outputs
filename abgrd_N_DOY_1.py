import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# draw grain yield response to N rate

def init_1d(treats_num):
    return [None for i in range(treats_num)]
def init_2d(treats_num,site_num):
    return [[None for i in range(treats_num)] for j in range(site_num)]
    
# sites1 = ['S1B1_2014','S1B2_2014','S1B3_2014','S1B4_2014','S2B1_2014','S2B2_2014','S2B3_2014','S2B4_2014']
# sites2 = ['S1B1_2015','S1B2_2015','S1B3_2015','S1B4_2015','S2B1_2015','S2B2_2015','S2B3_2015','S2B4_2015']

# groups according to planting_sidedress nitrogen treatments
total_treats = ['0_0','40_0','80_0','120_0','160_0','200_0','240_0','280_0',
                '40_40','40_80','40_120','40_160','40_200','40_240',
                '80_80','80_160']
# group_1 = ['0_0','40_0','80_0','120_0','160_0','200_0','240_0','280_0']
# group_2 = ['40_0','40_40','40_80','40_120','40_160','40_200','40_240']
# group_3 = ['80_0','80_80','80_160']

# x1 = init_1d(len(group_1))
# x2 = init_1d(len(group_2))
# x3 = init_1d(len(group_3))
# yld1 = init_1d(len(group_1))
# yld2 = init_1d(len(group_2))
# yld3 = init_1d(len(group_3))
# x = {}
# sim_yld = {}
#
# T_N = init_2d(len(total_treats),len(sites))
# P_N = init_2d(len(total_treats),len(sites))
# S_N = init_2d(len(total_treats),len(sites))
# obs_yld = init_2d(len(total_treats),len(sites))
# # T_N1 = np.zeros([8, 8])
# T_N1 = init_2d(len(group_1),len(sites))
# T_N2 = init_2d(len(group_2),len(sites))
# T_N3 = init_2d(len(group_3),len(sites))
# obs_yld1 = init_2d(len(group_1),len(sites))
# obs_yld2 = init_2d(len(group_2),len(sites))
# obs_yld3 = init_2d(len(group_3),len(sites))

# m = pd.read_csv('./yields.csv')
# grain = pd.read_csv(m,sep='\s+')
# obs = m['PMN']
# Ntr1 = m['Total_N']
# Ntr2 = m['Plant_N']
# Ntr3 = m['Side_N']
# for i in range(0,8):
#     T_N[i] = Ntr1.loc[(i * 16):(i * 16 + 15)]
#     P_N[i] = Ntr2.loc[(i * 16):(i * 16 + 15)]
#     S_N[i] = Ntr3.loc[(i * 16):(i * 16 + 15)]
#     obs_yld[i] = obs.loc[(i * 16):(i * 16 + 15)] * 0.89


sites1 = ['S1B1_2014','S1B2_2014','S1B3_2014','S1B4_2014','S2B1_2014','S2B2_2014','S2B3_2014','S2B4_2014']
sites2 = ['S1B1_2015','S1B2_2015','S1B3_2015','S1B4_2015','S2B1_2015','S2B2_2015','S2B3_2015','S2B4_2015']
components = ['SHOOT N','LEAF_N','SHTH_N','STALK_N','RESERVE_N','GRAIN_N','ROOT_N','LITTER_N'] 

FOR component in components:
    for fig_num, sites in enumerate([sites1,sites2]):
        if sites == sites1:
            year = '2014'
        else:
            year = '2015'
        fig = plt.figure(fig_num, figsize=(48, 16))
        fig_plc = 1
        for i, site in enumerate(sites):

            for k in range(0, 8):
                if k == 0:
                    N1 = 40 * k
                    f1 = open('./' + site + '/' + str(N1) + '_0/01011{}scnd1'.format(year))
                    data1 = pd.read_csv(f1, sep='\s+')  # define data type
                    f1.close()
                    x1 = init_2d(len(data1['DOY']),len(total_treats))
                    y1 = init_2d(len(data1['DOY']),len(total_treats))
                    y1[k] = data1[component] * 8.9  # g/m2 -> lb/acre, if C to biomass *8.9 / 0.45 = * 19.826
                    x1[k] = data1['DOY']
                elif k < 3:
                    N1 = 40 * k
                    f1 = open('./' + site + '/' + str(N1) + '_0/01011{}scnd1'.format(year))
                    data1 = pd.read_csv(f1, sep='\s+')  # define data type
                    f1.close()
                    y1[k] = data1[component] * 8.9  # g/m2 -> lb/acre, if C to biomass *8.9 / 0.45 = * 19.826
                    x1[k] = data1['DOY']

                    N2 = 40 * k
                    f2 = open('./' + site + '/40_' + str(N2) + '/01011{}scnd1'.format(year))
                    data2 = pd.read_csv(f2, sep='\s+')  # define data type
                    f2.close()
                    y1[k+7] = data2[component] * 8.9
                    x1[k+7] = data2['DOY']

                    N3 = 80 * k
                    f3 = open('./' + site + '/80_' + str(N3)+'/01011{}scnd1'.format(year))
                    data3 = pd.read_csv(f3, sep='\s+')  # define data type
                    f3.close()
                    y1[k+13] = data3[component] * 8.9
                    x1[k+13] = data3['DOY']
                elif k < 7:
                    N1 = 40 * k
                    f1 = open('./' + site + '/' + str(N1) + '_0/01011{}scnd1'.format(year))
                    data1 = pd.read_csv(f1, sep='\s+')  # define data type
                    f1.close()
                    y1[k] = data1[component] * 8.9  # g/m2 -> lb/acre, if C to biomass *8.9 / 0.45 = * 19.826
                    x1[k] = data1['DOY']

                    N2 = 40 * k
                    f2 = open('./' + site + '/40_' + str(N2)+'/01011{}scnd1'.format(year))
                    data2 = pd.read_csv(f2, sep='\s+')  # define data type
                    f2.close()
                    y1[k+7] = data2[component] * 8.9  # g/m2 -> lb/acre, if C to biomass *8.9 / 0.45 = * 19.826
                    x1[k+7] = data2['DOY']
                else:
                    N1 = 40 * k
                    f1 = open('./' + site + '/' + str(N1) + '_0/01011{}scnd1'.format(year))
                    data1 = pd.read_csv(f1, sep='\s+')  # define data type
                    f1.close()
                    y1[k] = data1[component] * 8.9  # g/m2 -> lb/acre, if C to biomass *8.9 / 0.45 = * 19.826
                    x1[k] = data1['DOY']

            plt.subplot(2,4,fig_plc)
            plt.ylim(0,500)
            for m in range(0,16):
                if m < 8:
                    plt.plot(x1[m],y1[m])
                elif m < 14:
                    plt.plot(x1[m],y1[m],'--')
                else:
                    plt.plot(x1[m],y1[m],'-.')

            plt.legend(labels=['0_0 (lb N/acre)','40_0','80_0','120_0','160_0','200_0','240_0','280_0',
                    '40_40','40_80','40_120','40_160','40_200','40_240',
                    '80_80','80_160'], fontsize = 14)
            plt.xlabel('DOY', fontsize = 20)
            plt.ylabel('{} (lb/acre)'.format(component), fontsize = 20)
            plt.title(site, fontsize=22)
            plt.tick_params(labelsize=18)
            # print(y1[13].max())
            fig_plc += 1
        #
        plt.savefig('{}_DOY_{}.png'.format(component,year))
    plt.clf()
# x = pd.DataFrame(x) 
# sim_yld = pd.DataFrame(sim_yld) 
# x.to_csv('N rates_S1S2.csv',index = 0)
# sim_yld.to_csv('simulated_abovegndN_S1S2.csv',index = 0)
# plt.show()

