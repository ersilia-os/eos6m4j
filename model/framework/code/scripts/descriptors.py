import sys
import os
import csv
import numpy as np

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, "../bidd-molmap/"))

from utils import descriptors_molmap

input_file = sys.argv[1]
output_file = sys.argv[2]

mp = descriptors_molmap()

with open(input_file, "r") as f:
    smiles_list = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles_list += [r[0]]

X = mp.batch_transform(smiles_list)

with open(output_file, "w") as f:
    np.save(f, X)