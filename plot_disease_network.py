import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

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
# Perform PCA
    print("PCA")
    num_diseases = len(disease_labels)
    num_symptoms = len(symptom_features)
    # Mean-center each feature
    print("Mean-centering")
    feature_means = np.mean(hsdn, axis=0)
    for disease_idx in range(num_diseases):
        hsdn[disease_idx] = np.subtract(hsdn[disease_idx], feature_means)
    # Get PCA-transformed data
    print("PCA Transformation")
    pca_vectors = PCA(n_components=50).fit(hsdn)
    pca_transformed_data = pca_vectors.transform(hsdn)

# Perform tSNE
    print("TSNE")
    tsne_embedded_symptoms = TSNE(n_components=2, verbose=1).fit_transform(pca_transformed_data)

# Plot
    print("Plotting")
    plt.figure()
    plt.scatter(tsne_embedded_symptoms[:,0], tsne_embedded_symptoms[:,1], marker='.', color='green', alpha=0.75)
    plt.title("tSNE plot of diseases based on symptoms")
    plt.savefig('tSNE_plot_hsdn.pdf')