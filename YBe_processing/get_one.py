import sys
import straxen
import strax
import math
import os
import cutax
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import time 
import datetime
import tqdm
import h5py
from cutax.cuts.s2_width import S2WidthWireModeledWIMP

first = sys.argv[1]


st = cutax.contexts.xenonnt_online(download_heavy = True,
                                   #include_rucio_local=True, 
                                   output_folder='/scratch/midway2/scli/strax_data/')
st.register(S2WidthWireModeledWIMP)
st.register(cutax.cuts.BDTAntiAC)

# runs_s = st.select_runs( run_mode='ybe_linked', 
#                        # include_tags=["_sr1_preliminary"], 
    
#                        available="event_info")

# sel=runs_s['name']>=first
# sel&=runs_s['name']<=last
# runs = runs_s[sel]['name']
# print(np.sum(runs_s[sel]['livetime'])/np.timedelta64(1, 'h'))

targets = ('event_info',
                'cut_cs2_area_fraction_top',
                'cut_daq_veto',
                'cut_main_is_valid_triggering_peak',
                'cut_interaction_exists',
                'cut_run_boundaries',
                'cut_s1_area_fraction_top',
                #'cut_s1_max_pmt',
                #'cut_s1_pattern_bottom',
                #'cut_s1_pattern_top',
                #'cut_s1_single_scatter',
                'cut_s1_width',
                #'cut_s2_pattern',
                'cut_s2_recon_pos_diff',
                'cut_s2_single_scatter',
                'cut_s2_width_wire_modeled_wimps',
                #'cut_s2_naive_bayes',
                #'cut_s1_naive_bayes',
                #'cut_time_shadow',
                #'cut_time_veto',
                #'cut_position_shadow',
                #'cut_ambience',
                #'cut_bdt_ac',
                'cut_s1_tightcoin_3fold',
                'cut_fiducial_volume'
          )

df = st.get_df(first,
               targets,
               max_workers=8
                     )
targets = ('event_info',
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
                'cut_s2_naive_bayes',
                'cut_s1_naive_bayes',
                #'cut_time_shadow',
                'cut_time_veto',
                #'cut_position_shadow',
                #'cut_ambience',
                'cut_bdt_ac',
                'cut_s1_tightcoin_3fold',
                'cut_fiducial_volume'
          )
df = st.get_df(first,
               targets,
               max_workers=8
                     )

df['run_id']=[first]*len(df)
df.to_hdf(f'/dali/lgrandi/sghosh/YBe_data/event_info_{first}.hdf5', key='events', mode='w')
