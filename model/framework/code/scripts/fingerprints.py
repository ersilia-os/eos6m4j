import sys
import os
import csv
import numpy as np

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, "../bidd-molmap/"))

from utils import fingerprints_molmap

input_file = sys.argv[1]
output_file = sys.argv[2]

mp = fingerprints_molmap()

with open(input_file, "r") as f:
    smiles_list = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles_list += [r[0]]

X = mp.batch_transform(smiles_list)
X = np.sum(X, axis=3)
print("Output shape", X.shape)
X = X.reshape(X.shape[0], X.shape[1]*X.shape[2])
print("Output shape", X.shape)

with open(output_file, "wb") as f:
    np.save(f, X)