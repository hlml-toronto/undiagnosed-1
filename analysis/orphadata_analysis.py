import numpy as np
import os
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# ----------------------------------------------
# Globals
# ----------------------------------------------
DATABASE = 'databases/orphadata/'
disease_labels = []
symptom_features = []
orpha = []
with open(os.path.join(os.getcwd(), DATABASE, 'diseases_HPO.dat'), 'rb') as f:
    disease_labels = pickle.load(f)
with open(os.path.join(os.getcwd(), DATABASE, 'symptoms_HPO.dat'), 'rb') as f:
    symptom_features = pickle.load(f)
with open(os.path.join(os.getcwd(), DATABASE, 'matrix_HPO.dat'), 'rb') as f:
    orpha = pickle.load(f)


if __name__ == "__main__":
# Perform PCA
    print("PCA")
    num_diseases = len(disease_labels)
    num_symptoms = len(symptom_features)
    # Mean-center each feature
    print("Mean-centering")
    feature_means = np.mean(orpha, axis=0)
    for disease_idx in range(num_diseases):
        orpha[disease_idx] = np.subtract(orpha[disease_idx], feature_means)
    # Get PCA-transformed data
    print("PCA Transformation")
    pca_vectors = PCA(n_components=50).fit(orpha)
    pca_transformed_data = pca_vectors.transform(orpha)

    # Perform tSNE
    print("TSNE")
    tsne_embedded_symptoms = TSNE(n_components=2, verbose=1).fit_transform(pca_transformed_data)

    # Plot
    print("Plotting")
    plt.figure()
    plt.scatter(tsne_embedded_symptoms[:,0], tsne_embedded_symptoms[:,1], marker='.', color='green', alpha=0.75)
    plt.title("tSNE plot of rare diseases based on symptoms")
    plt.savefig('tSNE_plot_orhpadata.pdf')
