radius = 66.4
height = 148.6
z_cut = [-125, -10]
cut_params = [-1.4, 25]

rate_box_cs1 = [2.5, 10]
rate_box_cs2 = [100, 1000]
rate_box_cs1_sm = [2.5, 10]
rate_box_cs2_sm = [200, 600]

max_radius=61.35
min_z=-13.6132           
max_z=-134.238

params = {
    'font.family': 'serif',
    'font.size' : 24, 'axes.titlesize' : 42, 'axes.labelsize' : 32, 'axes.linewidth' : 2,
    # ticks
    'xtick.labelsize' : 24, 'ytick.labelsize' : 24, 'xtick.major.size' : 18, 'xtick.minor.size' : 8,
    'ytick.major.size' : 18, 'ytick.minor.size' : 8, 'xtick.major.width' : 2, 'xtick.minor.width' : 2,
    'ytick.major.width' : 2, 'ytick.minor.width' : 2, 'xtick.direction' : 'in', 'ytick.direction' : 'in',
    # markers
    'lines.markersize' : 8, 'lines.markeredgewidth' : 2, 'errorbar.capsize' : 5, 'lines.linewidth' : 2,
    #'lines.linestyle' : None, 'lines.marker' : None,
    'savefig.bbox' : 'tight', 'legend.fontsize' : 24,
    'axes.labelsize': 30, 'axes.titlesize':24, 'xtick.labelsize':24, 'ytick.labelsize':24,
    'backend': 'Agg', 'mathtext.fontset': 'dejavuserif',
    'figure.facecolor':'w',
    #pad
    'axes.labelpad':20,
    # ticks
    'xtick.major.pad': 7,   'xtick.minor.pad': 7,   
    'ytick.major.pad': 4, 'ytick.minor.pad': 4,
}
plt.rcParams.update(params)

targets = (
    'event_info',
    'cut_cs2_area_fraction_top',
    'cut_main_is_valid_triggering_peak',
    'cut_interaction_exists',
    'cut_run_boundaries',
    'cut_s1_max_pmt',
    'cut_s1_width',
    'cut_s2_recon_pos_diff',
    'cut_s2_single_scatter',
    'cut_s1_tightcoin_3fold',
    'cut_fiducial_volume',
    'cut_bdt_ac',
    'cut_s2_width_wire_modeled_wimps',
    'cut_s2_pattern',
    'cut_s1_single_scatter',
    'cut_s1_pattern_top',
    'cut_s1_area_fraction_top',
    'cut_s1_pattern_bottom',
    'cut_s1_naive_bayes',
    'cut_s2_naive_bayes',
    'cut_daq_veto',
    'cut_time_veto',
    'cut_s1_tightcoin_3fold',
    
)

target_less = ('event_info',
                'cut_cs2_area_fraction_top',
                'cut_daq_veto',
                'cut_main_is_valid_triggering_peak',
                'cut_interaction_exists',
                'cut_run_boundaries',
                'cut_s1_area_fraction_top',
                'cut_s1_max_pmt',
                'cut_s1_pattern_bottom',
                'cut_s1_pattern_top',
                'cut_s1_single_scatter',
                'cut_s1_width',
                'cut_s2_pattern',
                'cut_s2_recon_pos_diff',
                'cut_s2_single_scatter',
                'cut_s2_width_wire_modeled_wimps',
                # 'cut_s2_naive_bayes',
                # 'cut_s1_naive_bayes',
                #'cut_time_shadow',
                # 'cut_time_veto',
                #'cut_position_shadow',
                #'cut_ambience',
                'cut_bdt_ac',
                'cut_s1_tightcoin_3fold',
                'cut_fiducial_volume'
          )

targets_hs = (
    'event_info',
    'cut_cs2_area_fraction_top',
    # 'cut_main_is_valid_triggering_peak',
    'cut_interaction_exists',
    # 'cut_run_boundaries',
    'cut_s1_max_pmt',
    'cut_s1_width',
    'cut_s2_recon_pos_diff',
    'cut_s2_single_scatter',
    'cut_s1_tightcoin_3fold',
    'cut_fiducial_volume',
    # 'cut_bdt_ac',
    'cut_s2_width_wire_modeled_wimps',
    'cut_s2_pattern',
    'cut_s1_single_scatter',
    'cut_s1_pattern_top',
    'cut_s1_area_fraction_top',
    'cut_s1_pattern_bottom',
    'cut_s1_naive_bayes',
    'cut_s2_naive_bayes',
    # 'cut_daq_veto',
    # 'cut_time_veto',
    'cut_s1_tightcoin_3fold',
    
)


