# v tuning (rphi)
# (c) 2014 APL
#
# Fly manifest

experiment_name = "tuning_rphi_v"
path = "/Volumes/flybehaviour/Ball/reverse_project/paper1"

# CAREFUL -- this is 100Hz (for detailed transient)
dt = 0.01

flies = {
    'F1 id528 x X154': [
        ['20141012_fly07_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly08_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly10_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly12_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly13_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly14_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly15_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly16_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly17_exp01', range(1, 70), range(25, 65)],
        ['20141012_fly18_exp01', range(1, 70), range(25, 65)],
    ],
    'F1 X154 x GMRSS00324': [
        ['20141014_fly19_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly20_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly21_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly22_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly23_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly24_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly25_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly26_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly27_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly29_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly30_exp01', range(1, 70), range(25, 65)],
    ],
}

mappings = {
    'direction': lambda x: "left" if x[1] == 1 else "right",
    'lambda': lambda x: x[0],
    'velocity': lambda x: x[3],
}