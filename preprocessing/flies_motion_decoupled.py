# Fly manifest

experiment_name = "tuning_rphi_decoupled"
path = "/Volumes/flybehaviour/Ball/reverse_project/paper1"

dt = 0.05

flies = {
    'WT CS': [
        ['20171018_fly01_exp01', range(1, 35), range(9, 34)],
        ['20171018_fly02_exp01', range(1, 35), range(9, 34)],
        ['20171018_fly21_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly26_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly28_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly29_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly31_exp01', range(1, 35), range(5, 30)],
        ['20171019_fly33_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly35_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly37_exp01', range(1, 35), range(9, 34)],
        ['20171019_fly39_exp01', range(1, 32), range(5, 30)],
    ]
}

mappings = {
    'lambda': lambda x: x[0],
    'direction': lambda x: "left" if x[1] == 1 else "right",
    'contrast': lambda x: x[2],
    'jump_f': lambda x: x[3],
    'jump_width': lambda x: x[4],
    'switch_f': lambda x: x[5],
}
