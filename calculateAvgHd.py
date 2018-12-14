import sys
from os import listdir
from os.path import join
folder = sys.argv[1]
label_dict = {"23": "Right Accumbens Area", "30": "Left Accumbens Area", "31": "Right_Amygdala", "32": "Left Amygdala", "36": "Right Caudate", "37": "Left Caudate", "47": "Right Hippocampus",
              "48": "Left Hippocampus", "55": "Right Pallidum", "56": "Left Pallidum", "57": "Right Putamen", "58": "Left Putamen", "59": "Right Thalamus", "60": "Left Thalamus"}
avg = {}
for file in listdir(folder):
    with open(join(folder, file)) as f:
        lines = f.readlines()
        for line in lines:
            label = line.split()[0]
            val = float(line.split()[2])
            if label in avg:
                avg[label] += val
            else:
                avg[label] = val

for key, val in avg.items():
    if key in label_dict:
        avg[key] = val / len(listdir(folder))
        print("\t" + label_dict[key] + "  --->   " +  str(avg[key]))
