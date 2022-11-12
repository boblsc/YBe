import straxen
xx1=xx=np.array([  1.,   3.,   5.,   7.,   9.,  11.,  13.,  15.,  17.,  19.,  21.,
         23.,  25.,  27.,  29.,  31.,  33.,  35.,  37.,  39.,  41.,  43.,
         45.,  47.,  49.,  51.,  53.,  55.,  57.,  59.,  61.,  63.,  65.,
         67.,  69.,  71.,  73.,  75.,  77.,  79.,  81.,  83.,  85.,  87.,
         89.,  91.,  93.,  95.,  97.,  99., 101., 103., 105., 107., 109.,
        111., 113., 115., 117., 119., 121., 123., 125., 127., 129., 131.,
        133., 135., 137., 139., 141., 143., 145., 147., 149., 151., 153.,
        155., 157., 159., 161., 163., 165., 167., 169., 171., 173., 175.,
        177., 179., 181., 183., 185., 187., 189., 191., 193., 195., 197.,
        199.])
yy=np.array([ 541.19124461,  601.9918823 ,  661.94901198,  721.07227172,
         779.37129956,  836.85573356,  893.53521175,  949.41937219,
        1004.51785293, 1058.84029203, 1112.39632752, 1165.19559747,
        1217.24773991, 1268.56239291, 1319.14919451, 1369.01778275,
        1418.1777957 , 1466.6388714 , 1514.41064789, 1561.50276324,
        1607.92485549, 1653.68656269, 1698.79752288, 1743.26737413,
        1787.10575448, 1830.32230198, 1872.92665467, 1914.92845062,
        1956.33732787, 1997.16292446, 2037.41487846, 2077.10282791,
        2116.23641085, 2154.82526535, 2192.87902944, 2230.40734119,
        2267.41983863, 2303.92615982, 2339.93594281, 2375.45882565,
        2410.50444639, 2445.08244308, 2479.20245377, 2512.87411651,
        2546.10706935, 2578.91095033, 2611.29539752, 2643.27004895,
        2674.84454268, 2706.02851677, 2736.83160925, 2767.26345818,
        2797.3337016 , 2827.05197758, 2856.42792415, 2885.47117938,
        2914.1913813 , 2942.59816797, 2970.70117744, 2998.51004776,
        3026.03441697, 3053.28392314, 3080.2682043 , 3106.99689851,
        3133.47964382, 3159.72607827, 3185.74583993, 3211.54856683,
        3237.14389703, 3262.54146858, 3287.75091953, 3312.78188792,
        3337.64401181, 3362.34692925, 3386.90027829, 3411.31369697,
        3435.59682336, 3459.75929549, 3483.81075142, 3507.76082919,
        3531.61916686, 3555.39540248, 3579.0991741 , 3602.74011977,
        3626.32787753, 3649.87208544, 3673.38238154, 3696.8684039 ,
        3720.33979055, 3743.80617955, 3767.27720894, 3790.76251678,
        3814.27174112, 3837.81452001, 3861.40049149, 3885.03929362,
        3908.74056445, 3932.51394202, 3956.36906439, 3980.3155696 ])
yy1=np.array([1786.96280145, 1886.68103233, 1985.04219375, 2082.05877585,
        2177.74326876, 2272.1081626 , 2365.16594751, 2456.92911361,
        2547.41015104, 2636.62154992, 2724.57580038, 2811.28539256,
        2896.76281657, 2981.02056256, 3064.07112064, 3145.92698096,
        3226.60063364, 3306.1045688 , 3384.45127658, 3461.6532471 ,
        3537.72297051, 3612.67293691, 3686.51563646, 3759.26355926,
        3830.92919546, 3901.52503519, 3971.06356856, 4039.55728572,
        4107.01867679, 4173.46023189, 4238.89444117, 4303.33379475,
        4366.79078275, 4429.27789531, 4490.80762256, 4551.39245462,
        4611.04488163, 4669.77739372, 4727.60248101, 4784.53263363,
        4840.58034172, 4895.75809539, 4950.07838479, 5003.55370004,
        5056.19653127, 5108.01936861, 5159.03470219, 5209.25502214,
        5258.69281858, 5307.36058166, 5355.27080148, 5402.4359682 ,
        5448.86857193, 5494.5811028 , 5539.58605094, 5583.89590649,
        5627.52315958, 5670.48030032, 5712.77981885, 5754.43420531,
        5795.45594981, 5835.8575425 , 5875.65147349, 5914.85023292,
        5953.46631092, 5991.51219761, 6029.00038313, 6065.9433576 ,
        6102.35361116, 6138.24363393, 6173.62591605, 6208.51294764,
        6242.91721883, 6276.85121975, 6310.32744053, 6343.3583713 ,
        6375.95650219, 6408.13432333, 6439.90432484, 6471.27899687,
        6502.27082953, 6532.89231296, 6563.15593728, 6593.07419262,
        6622.65956912, 6651.92455691, 6680.8816461 , 6709.54332684,
        6737.92208925, 6766.03042346, 6793.8808196 , 6821.4857678 ,
        6848.85775818, 6876.00928089, 6902.95282604, 6929.70088377,
        6956.26594421, 6982.66049748, 7008.89703371, 7034.98804304])


def cut_acceptance(df):
    # check how many cuts are applied
    this=[]
    for c in df.columns.values:
        if "cut" in c:
            # print(c)
            this.append(c)

            # check survival in a cumulative way
    fraction_cumu = 1

    cut_name_s = []
    fraction_s = []
    fraction_cumu_s = []
    n_pre_s = []
    n_after_s = []

    for cut_name in this: #cutax.cut_lists.basic.BasicCuts.cuts:
        n_pre = len(df)
        # apply the cut
        #cut_name = this #cut.provides
        # if isinstance(cut_name, tuple):
        #     cut_name = cut_name[0]

        df = df[df[cut_name]]
        n_after = len(df)

        # individual fraction
        fraction = n_after / n_pre
        # cumulative
        fraction_cumu *= fraction

        # append everything
        cut_name_s.append(cut_name)
        fraction_s.append(fraction)
        fraction_cumu_s.append(fraction_cumu)
        n_pre_s.append(n_pre)
        n_after_s.append(n_after)

    df_fraction = pd.DataFrame(dict(
    cut = cut_name_s,
    n_pre = n_pre_s,
    n_after = n_after_s,
    fraction = fraction_s,
    cumulative_fraction = fraction_cumu_s,))

    return straxen.dataframe_to_wiki(df_fraction)

def cut_cs1cs2(df,cs1=[0,10],cs2=[100,1000]):
    sel=df.cs1>cs1[0]
    sel&=df.cs1<cs1[1]
    sel&=df.cs2>cs2[0]
    sel&=df.cs2<cs2[1]
    return df[sel]

def show_cut(df_0,cutname,cs1=[0,10],cs2=[100,1000],save=False,alpha=0.5):
    df=cut_cs1cs2(df_0,cs1,cs2)
    cut=df[df[cutname]!=True]
    sur=df[df[cutname]]
    fig = plt.figure(figsize=(8, 6), dpi=120)
    ax = fig.add_subplot(111)
    ax.scatter(cut['cs1'], cut['cs2'], color='r', marker='.',label='Reject', s=5,alpha=alpha)
    ax.scatter(sur['cs1'], sur['cs2'], color='k', marker='.',label='Survive', s=5,alpha=alpha)
    plt.plot(xx1, yy1, color='purple',linestyle='--')
    plt.plot(xx,yy, color='purple',linestyle='--',label='Rn220 90%')

    ax.set(xlim=cs1, ylim=cs2, xlabel='cS1', ylabel='cS2')
    plt.title(cutname)
    if(save):
        plt.savefig(f"cut_eva/{cutname}.png")
    ax.legend()

    plt.show()
    
def rate_hz_in_box(data,cs1,cs2,dtype='data'):
    if(dtype=='data'):
        h=hour
    elif(dtype=='sim'):
        h=s_hour/sim_ratio
    data_cut=cut_cs1cs2(data,cs1=cs1,cs2=cs2)
    rate = len(data_cut)/(h*3600)
    rate_err = np.sqrt(len(data_cut))/(h*3600)
    return rate, rate_err 
    
            


def plot_cs1cs2_simple(df_data, df_sim=None, xlim=[0,20], ylim=[0,1500], xlabel='cS1 [PE]', ylabel='cS2 [PE]', data_label='YBe data (44h)',sim_label='YBe sim (91h)',plot_sim=None):

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter

    nullfmt = NullFormatter()         # no labels
    

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    plt.figure(1, figsize=(12, 12))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # now determine nice limits by hand:
    data_cuts=cut_cs1cs2(df_data,xlim,ylim)
    x=data_cuts['cs1']
    y=data_cuts['cs2']


    axScatter.set_xlim(xlim)
    axScatter.set_ylim(ylim)
    
    if (df_sim!=None):
        cut_sim=cut_cs1cs2(df_sim,xlim,ylim)
        x_sim=cut_sim['cs1']
        y_sim=cut_sim['cs2']
        

    xbins = np.linspace(xlim[0],xlim[1],50)
    ybins = np.linspace(ylim[0],ylim[1],50)
    axHistx.hist(x, bins=xbins,histtype='step',linewidth=2,color='k',label=data_label)
    axHisty.hist(y, bins=ybins, orientation='horizontal',histtype='step',linewidth=2,color='k',label=data_label)
    if (df_sim!=None):
        axHistx.hist(x_sim, bins=xbins,histtype='step',linewidth=2,color='b',label=sim_label)
        axHisty.hist(y_sim, bins=ybins, orientation='horizontal',histtype='step',linewidth=2,color='b',label=sim_label)
    axHistx.set_ylabel('counts', fontsize = 24)
    axHisty.set_xlabel('counts', fontsize = 24)
    axHistx.legend(fontsize=16)
    # axHisty.legend(fontsize=16)

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())
    axHistx.set_yscale('log')
    axHisty.set_xscale('log')



    axScatter.scatter(x,y,color='k', marker='o',label=data_label, s=10,alpha=0.8)                  
    axScatter.set_xlabel(xlabel, fontsize = 24)
    axScatter.set_ylabel(ylabel, fontsize = 24)
    


    axScatter.plot(xx1, yy1, color='purple',linestyle='--')
    axScatter.plot(xx,yy, color='purple',linestyle='--',label='$^{220}$Rn median 90%')
    
    if(plot_sim=='scatter'):
        axScatter.scatter(x_sim,y_sim,color='b',marker='o',label=sim_label,s=10,alpha=0.6)
    elif(plot_sim=='contour'):
        import seaborn as sns
        sns.kdeplot(x=x_sim, y=y_sim,thresh=0.1,levels=1,color='b')
    
    axScatter.plot(
        [rate_box_cs1[0], rate_box_cs1[0], rate_box_cs1[1], rate_box_cs1[1], rate_box_cs1[0]],
        [rate_box_cs2[0], rate_box_cs2[1], rate_box_cs2[1], rate_box_cs2[0], rate_box_cs2[0]],
        color='r',  linestyle='--',linewidth=3
    )

    axScatter.plot(
        [rate_box_cs1_sm[0], rate_box_cs1_sm[0], rate_box_cs1_sm[1], rate_box_cs1_sm[1], rate_box_cs1_sm[0]],
        [rate_box_cs2_sm[0], rate_box_cs2_sm[1], rate_box_cs2_sm[1], rate_box_cs2_sm[0], rate_box_cs2_sm[0]],
        color='g',  linestyle='-.',linewidth=3
    )
    axScatter.legend(fontsize=16)

    plt.show()       
    

def plot_cs1cs2(df_data, df_sim=None, xlim=[0,20], ylim=[0,1500], xlabel='cS1 [PE]', ylabel='cS2 [PE]', data_label='YBe data (44h)',sim_label='YBe sim (91h)',plot_sim=None):

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter

    nullfmt = NullFormatter()         # no labels
    
    rate_l, rate_err_l=rate_hz_in_box(df_data,rate_box_cs1,rate_box_cs2,dtype='data')
    rate_s, rate_err_s=rate_hz_in_box(df_data,rate_box_cs1_sm,rate_box_cs2_sm,dtype='data')

    
    sim_rate_l, sim_rate_l_err=rate_hz_in_box(df_sim,rate_box_cs1,rate_box_cs2,dtype='sim')
    sim_rate_s, sim_rate_s_err=rate_hz_in_box(df_sim,rate_box_cs1_sm,rate_box_cs2_sm,dtype='sim')

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    plt.figure(1, figsize=(12, 12))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # now determine nice limits by hand:
    data_cuts=cut_cs1cs2(df_data,xlim,ylim)
    x=data_cuts['cs1']
    y=data_cuts['cs2']


    axScatter.set_xlim(xlim)
    axScatter.set_ylim(ylim)
    
    cut_sim=cut_cs1cs2(df_sim,xlim,ylim)
    x_sim=cut_sim['cs1']
    y_sim=cut_sim['cs2']
        

    xbins = np.linspace(xlim[0],xlim[1],50)
    ybins = np.linspace(ylim[0],ylim[1],50)
    axHistx.hist(x, bins=xbins,histtype='step',linewidth=2,color='k',label=data_label)
    axHisty.hist(y, bins=ybins, orientation='horizontal',histtype='step',linewidth=2,color='k',label=data_label)
    axHistx.hist(x_sim, bins=xbins,histtype='step',linewidth=2,color='b',label=sim_label)
    axHisty.hist(y_sim, bins=ybins, orientation='horizontal',histtype='step',linewidth=2,color='b',label=sim_label)
    axHistx.set_ylabel('counts', fontsize = 24)
    axHisty.set_xlabel('counts', fontsize = 24)
    axHistx.legend(fontsize=16)
    # axHisty.legend(fontsize=16)

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())
    axHistx.set_yscale('log')
    axHisty.set_xscale('log')



    axScatter.scatter(x,y,color='k', marker='o',label=data_label, s=10,alpha=0.8)                  
    axScatter.set_xlabel(xlabel, fontsize = 24)
    axScatter.set_ylabel(ylabel, fontsize = 24)
    


    axScatter.plot(xx1, yy1, color='purple',linestyle='--')
    axScatter.plot(xx,yy, color='purple',linestyle='--',label='$^{220}$Rn median 90%')
    
    if(plot_sim=='scatter'):
        axScatter.scatter(x_sim,y_sim,color='b',marker='o',label=sim_label,s=10,alpha=0.6)
    elif(plot_sim=='contour'):
        import seaborn as sns
        sns.kdeplot(x=x_sim, y=y_sim,thresh=0.1,levels=1,color='b')
    
    axScatter.plot(
        [rate_box_cs1[0], rate_box_cs1[0], rate_box_cs1[1], rate_box_cs1[1], rate_box_cs1[0]],
        [rate_box_cs2[0], rate_box_cs2[1], rate_box_cs2[1], rate_box_cs2[0], rate_box_cs2[0]],
        color='r', label=f'data={rate_l*1000:.2f}$\pm${rate_err_l*1000:.2f}mHz, sim={sim_rate_l*1000:.2f}$\pm${sim_rate_l_err*1000:.2f}mHz', linestyle='--',linewidth=3
    )

    axScatter.plot(
        [rate_box_cs1_sm[0], rate_box_cs1_sm[0], rate_box_cs1_sm[1], rate_box_cs1_sm[1], rate_box_cs1_sm[0]],
        [rate_box_cs2_sm[0], rate_box_cs2_sm[1], rate_box_cs2_sm[1], rate_box_cs2_sm[0], rate_box_cs2_sm[0]],
        color='g', label=f'data={rate_s*1000:.2f}$\pm${rate_err_s*1000:.2f}mHz, sim={sim_rate_s*1000:.2f}$\pm${sim_rate_s_err*1000:.2f}mHz', linestyle='-.',linewidth=3
    )
    axScatter.legend(fontsize=16)

    plt.show()       

    
    
#wire cuts
perp_wire_x_pos = 13.06  # cm
perp_wire_angle = np.deg2rad(30)


def rotate_axis(x_obs, y_obs):
    x_rot = np.cos(perp_wire_angle) * x_obs - np.sin(perp_wire_angle) * y_obs
    y_rot = np.sin(perp_wire_angle) * x_obs + np.cos(perp_wire_angle) * y_obs
    return x_rot, y_rot


def get_near_wires(x_obs, y_obs, distance_cm):
    '''Returns a mask selecting the events near the perpendicular wires.'''
    x_rot, y_rot = rotate_axis(x_obs, y_obs)
    mask_near_wires = np.abs(np.abs(x_rot) - perp_wire_x_pos) < distance_cm
    return mask_near_wires

def wire_cut(events,dist_cm=4.45):
    sel=get_near_wires(events['s2_x'], events['s2_y'], dist_cm)
    return events[sel==False]



def add_wire_cut(events,dist_cm=4.45):
    sel=get_near_wires(events['s2_x'], events['s2_y'], dist_cm)
    events['wire_cut']=sel==False
    return events

def plot_xy(data_cs1cs2_cuts,cs1_range, cs2_range):
    fig = plt.figure(figsize=(9, 7), dpi=120)
    ax = fig.add_subplot(111)
    ax.axis('equal')
    bkg_n=10000

    # ax.scatter(data['x'][:bkg_n], data['y'][:bkg_n], c='grey',s=1,alpha=0.1)
    s = ax.scatter(data_cs1cs2_cuts['x'], data_cs1cs2_cuts['y'], c=data_cs1cs2_cuts['cs1'],s=data_cs1cs2_cuts['cs2']/10,alpha=0.7)
    cb = plt.colorbar(s, label='cs1')
    theta = np.linspace(-np.pi, np.pi, 100)
    x = np.cos(theta)*radius
    y = np.sin(theta)*radius
    ax.plot(x,y, color='black',label='TPC')

    x = np.cos(theta)*max_radius
    y = np.sin(theta)*max_radius
    ax.plot(x,y, color='black',linestyle='--',label='WIMP FV')

    ax.set(xlim=[-70,70], ylim=[-70,70], xlabel='x (cm)', ylabel='y (cm)')
    # plt.legend()

    plt.title(f'cS1={cs1_range}PE,cS2={cs2_range}PE',fontsize=16)
    plt.show()

    
def plot_rz(data_cs1cs2_cuts,cs1_range, cs2_range):
    xlim=[0,5000]
    ylim=[-160,0]
    fig = plt.figure(figsize=(8, 7), dpi=120)
    ax = fig.add_subplot(111)
    # ax.scatter(data['x'][:bkg_n]**2,data['z'][:bkg_n], c='grey',s=1,alpha=0.1)
    s = ax.scatter(data_cs1cs2_cuts['r'].values**2, data_cs1cs2_cuts['z'], c=data_cs1cs2_cuts['cs1'],s=data_cs1cs2_cuts['cs2']/10,alpha=0.7)
    cb = plt.colorbar(s, label='cS1')
    ax.hlines([-height], xmin=xlim[0], xmax=xlim[1], color='black')
    ax.vlines([max_radius**2], ymin=ylim[0], ymax=ylim[1], color='black',linestyle='--')
    ax.vlines([radius**2], ymin=ylim[0], ymax=ylim[1], color='black')
    ax.hlines([max_z,min_z], xmin=xlim[0], xmax=xlim[1], color='k', label='FV',linestyle='--')
    ax.set(xlim=xlim, ylim=ylim, xlabel='r$^2$ (cm$^2$)', ylabel='z (cm)')
    plt.title(f'cS1={cs1_range}PE, cS2={cs2_range}PE')
    plt.show()
    