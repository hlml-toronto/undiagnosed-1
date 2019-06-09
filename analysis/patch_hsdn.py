import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

# ----------------------------------------------
# Globals
# ----------------------------------------------
disease_labels = []
symptom_features = []
hsdn = []

with open(os.path.join(os.getcwd(), 'databases', 'disease_labels.p'), 'rb') as f:
    disease_labels = pickle.load(f)
with open(os.path.join(os.getcwd(), 'databases', 'hsdn.p'), 'rb') as f:
    hsdn = pickle.load(f)


hsdn_modified = []
disease_labels_modified = []
for row_idx in range(len(hsdn)):
    row_sum = np.sum(hsdn[row_idx])
    if row_sum == 0.0 or row_sum == 0:
        print('found disease with no symptoms')
        pass
    else:
        hsdn_modified.append(hsdn[row_idx])
        disease_labels_modified.append(disease_labels[row_idx])

with open(os.path.join(os.getcwd(), 'databases', 'disease_labels.p'), 'wb') as f:
    pickle.dump(disease_labels_modified, f)
with open(os.path.join(os.getcwd(), 'databases', 'hsdn.p'), 'wb') as f:
    pickle.dump(hsdn_modified, f)
