# dc tuning (rphi)
# (c) 2014 APL
#
# Fly manifest

experiment_name = "tuning_rphi_ultra"
path = "/Volumes/flybehaviour/Ball/reverse_project/paper1"

dt = 0.05

flies = {
    'F1 X154 x TNT': [
        ['20170120_fly01_exp01', range(1, 40), range(10, 35)],
        ['20170120_fly02_exp01', range(1, 40), range(5, 30)],
        ['20170120_fly03_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly29_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly30_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly31_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly32_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly33_exp01', range(1, 40), range(2, 27)],
        ['20170125_fly34_exp01', range(1, 40), range(2, 27)],
        ['20170125_fly35_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly36_exp01', range(1, 40), range(10, 35)],
    ],

    'F1 TNT x id548': [
        ['20170120_fly05_exp01', range(1, 40), range(10, 35)],
        ['20170120_fly06_exp01', range(1, 40), range(10, 35)],
        ['20170120_fly07_exp01', range(1, 40), range(14, 39)],
        ['20170123_fly27_exp01', range(1, 40), range(10, 35)],
        ['20170123_fly28_exp01', range(1, 40), range(5, 30)],
        ['20170126_fly45_exp01', range(1, 40), range(10, 35)],
        ['20170126_fly46_exp01', range(1, 40), range(10, 35)],
        ['20170126_fly47_exp01', range(1, 40), range(10, 35)],
        ['20170126_fly50_exp01', range(1, 40), range(5, 30)],
        ['20170126_fly54_exp01', range(1, 40), range(10, 35)],
        ['20170126_fly55_exp01', range(1, 40), range(10, 35)],
        ['20170126_fly56_exp01', range(1, 40), range(10, 35)],
    ],

    'F1 TNT x id114': [
        ['20170120_fly09_exp01', range(1, 40), range(14, 39)],
        ['20170120_fly10_exp01', range(1, 40), range(10, 35)],
        ['20170120_fly12_exp01', range(1, 40), range(10, 35)],
        ['20170123_fly14_exp01', range(1, 40), range(10, 35)],
        ['20170123_fly16_exp01', range(1, 40), range(14, 39)],
        ['20170123_fly21_exp01', range(1, 40), range(10, 35)],
        ['20170123_fly23_exp01', range(1, 40), range(10, 35)],
        ['20170123_fly24_exp01', range(1, 40), range(7, 32)],
        ['20170125_fly37_exp01', range(1, 40), range(14, 39)],
        ['20170125_fly38_exp01', range(1, 40), range(10, 35)],
        ['20170125_fly39_exp01', range(1, 40), range(14, 39)],
        ['20170126_fly43_exp01', range(1, 40), range(14, 39)],
        ['20170126_fly44_exp01', range(1, 40), range(14, 39)],
    ]
}

mappings = {
    'lambda': lambda x: x[0],
    'direction': lambda x: "left" if x[1] == 1 else "right",
    'contrast': lambda x: x[2],
    'jump_gap': lambda x: x[3],
    'jump_width': lambda x: x[4],
    'dc': lambda x: x[5],
    'reverse': lambda x: x[6],
}
