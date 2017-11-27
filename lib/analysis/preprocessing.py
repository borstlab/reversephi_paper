import numpy as np
import os
from struct import unpack
import scipy.interpolate as interpolate
import xml.etree.ElementTree as etree

import progressbar

columns_names = ['i_stimulus', 'time', 'forward_translation', 'sideward_translation', 'rot', 'x', 'y', 'path', 'temperature', 'info1', 'info2', 'info3']
columns_units = ['', 's', 'cm', 'cm', 'deg', 'cm', 'cm', 'cm', 'celcius', '', '', '']

def loaddata(file):
    #print file
    fp = open(file, "rb")
    info_str = fp.read(unpack('<L', fp.read(4))[0])
    
    # [formatversion, creation_time, columns_names, columns_units] = pickle.loads(info_str)
    
    # read the data
    buffer = fp.read()
    fp.close()
    #print buffer
    data = np.frombuffer(buffer, dtype=np.dtype('<d'))
    data = data.reshape(-1, len(columns_names))

    return data

def dopreprocessing_experiments(path, experiment_name, experiments, dt=0.05, process_columns=[2,4], trialstep = 1, with_temperature=False):
    
    for experiment in experiments:        
        data_processed =  dopreprocessing_experiment(path, experiment_name, experiment, dt, process_columns, trialstep, with_temperature)
        np.save(os.path.join(path, experiment_name, experiment[0], 'processeddata', 'data.npy'), data_processed)

def dopreprocessing_experiment(path, experiment_name, experiment, dt, process_columns, trialstep, with_temperature):

    # Fetch info about stimulus length:
    tree = etree.parse(os.path.join(path, experiment_name, experiment[0], 'info.xml'))
    setup_name = tree.find('setup').text
    genotype = tree.find('genotype').text
    stimlength = float(tree.find('tstimulus').text)
    
    interpol_time = np.arange(0, stimlength, dt)
    
    stimuli = np.load(os.path.join(path, experiment_name, experiment[0], 'stimuli.npy'))   
    i_stimuli = range(len(stimuli))
   
    data_processed = []

    progress = progressbar.ProgressBar(widgets=['Preprocessing {0} (genotype: {1}, measured on: {2})'.format(experiment[0], genotype, setup_name),
                                                progressbar.Percentage(), progressbar.Bar(), progressbar.ETA()])
            
    for trial in progress(experiment[1]):

        file_path = os.path.join(path, experiment_name, experiment[0], 'rawdata', 'trial%03d.bin'%trial)

        rawdata = loaddata(file_path)
        
        data_processed_trial = []

        for i_stimulus in i_stimuli:
            ind_stimulus = np.where(rawdata[:,0] == i_stimulus)[0]
            data_stimulus = rawdata[ind_stimulus]
            
            data_processed_trial_stim = []
            
            for i_column in process_columns:                
                # interpolate the data
                f = interpolate.interp1d(data_stimulus[:,1], data_stimulus[:,i_column], bounds_error = False)
                data_processed_trial_stim_column = f(interpol_time)
                
                data_processed_trial_stim.append(data_processed_trial_stim_column)
                
            data_processed_trial.append(data_processed_trial_stim)    

        data_processed.append(data_processed_trial)        
        
    data_processed = np.array(data_processed)
    return data_processed