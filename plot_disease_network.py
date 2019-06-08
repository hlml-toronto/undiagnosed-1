import numpy as np
import os
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# ----------------------------------------------
# Globals
# ----------------------------------------------
disease_labels = []
symptom_features = []
hsdn = []
with open(os.path.join(os.getcwd(), 'databases', 'disease_labels.p'), 'rb') as f:
    disease_labels = pickle.load(f)
with open(os.path.join(os.getcwd(), 'databases', 'symptom_features.p'), 'rb') as f:
    symptom_features = pickle.load(f)
with open(os.path.join(os.getcwd(), 'databases', 'hsdn.p'), 'rb') as f:
    hsdn = pickle.load(f)


if __name__ == "__main__":
    """
    X_embedded = TSNE(n_components=2).fit_transform(X)
    
    """