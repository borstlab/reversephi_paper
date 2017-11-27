# v tuning (rphi)
# (c) 2014 APL
#
# Fly manifest

experiment_name = "tuning_rphi_v"
path = "/Volumes/flybehaviour/Ball/reverse_project/paper1"

dt = 0.05

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
    'F1 id528 x GMRSS00324': [
        ['20141014_fly31_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly34_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly35_exp01', range(1, 70), range(25, 65)],
        ['20141014_fly36_exp01', range(1, 70), range(25, 65)],
        ['20141015_fly37_exp01', range(1, 70), range(15, 55)],
        ['20141015_fly38_exp01', range(1, 70), range(15, 55)],
        ['20141015_fly39_exp01', range(1, 70), range(25, 65)],
        ['20141015_fly40_exp01', range(1, 70), range(25, 65)],
        ['20141015_fly41_exp01', range(1, 70), range(25, 65)],
        ['20141015_fly42_exp01', range(1, 70), range(25, 65)],
    ],

    # New runs 2016 (JoV rev.)

    'F1 TNT x X154 (A)': [
        ['20161213_fly44_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly45_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly46_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly47_exp01', range(1, 60), range(29, 59)],
        ['20161213_fly50_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly51_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly52_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly54_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly55_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly57_exp01', range(1, 60), range(25, 55)],
        ['20161222_fly157_exp01', range(1, 60), range(25, 55)],
        ['20161222_fly159_exp01', range(1, 60), range(25, 55)],
    ],

    'F1 TNT x id548 (B)': [
        ['20161213_fly59_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly61_exp01', range(1, 60), range(25, 55)],
        ['20161213_fly62_exp01', range(1, 60), range(25, 55)],
        ['20161214_fly66_exp01', range(1, 60), range(25, 55)],
        ['20161214_fly67_exp01', range(1, 60), range(10, 40)],
        ['20161214_fly68_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly137_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly139_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly140_exp01', range(1, 60), range(20, 50)],
        ['20161220_fly141_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly143_exp01', range(1, 60), range(25, 55)],
        ['20161221_fly152_exp01', range(1, 60), range(25, 55)],
        ['20161221_fly153_exp01', range(1, 60), range(25, 55)],
        ['20161221_fly154_exp01', range(1, 60), range(25, 55)],
    ],

    'F1 TNT x id114 (C)': [
        ['20161214_fly74_exp01', range(1, 60), range(25, 55)],
        ['20161214_fly77_exp01', range(1, 60), range(25, 55)],
        ['20161214_fly79_exp01', range(1, 60), range(25, 55)],
        ['20161214_fly82_exp01', range(1, 60), range(25, 55)],
        ['20161215_fly84_exp01', range(1, 60), range(25, 55)],
        ['20161215_fly85_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly94_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly95_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly96_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly97_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly99_exp01', range(1, 60), range(25, 55)],
        ['20161221_fly145_exp01', range(1, 60), range(25, 55)],
        ['20161221_fly149_exp01', range(1, 60), range(25, 55)],
        ['20161222_fly160_exp01', range(1, 60), range(15, 45)],
        ['20161222_fly163_exp01', range(1, 60), range(15, 45)],
    ],

    'F1 id548 x X154 (D)': [
        ['20161215_fly88_exp01', range(1, 60), range(25, 55)],
        ['20161215_fly92_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly100_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly102_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly104_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly105_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly106_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly107_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly109_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly110_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly112_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly113_exp01', range(1, 60), range(25, 55)],
        ['20161219_fly114_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly115_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly116_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly117_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly118_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly119_exp01', range(1, 60), range(25, 55)],
    ],

    'F1 id114 x X154 (E)': [
        ['20161220_fly120_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly121_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly122_exp01', range(1, 60), range(20, 50)],
        ['20161220_fly123_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly124_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly125_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly127_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly130_exp01', range(1, 60), range(15, 45)],
        ['20161220_fly131_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly132_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly133_exp01', range(1, 60), range(25, 55)],
        ['20161220_fly134_exp01', range(1, 60), range(25, 55)],
    ],

}

mappings = {
    'direction': lambda x: "left" if x[1] == 1 else "right",
    'lambda': lambda x: x[0],
    'velocity': lambda x: x[3],
}