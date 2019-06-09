import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def make_tsne_diagnosis(data, plot_fname, patient_vector):
    # Add patient to data as an unlabelled 'disease'
    data.append(patient_vector)
    # Perform PCA
    print("PCA")
    num_diseases = np.shape(data)[0]
    # Mean-center each feature
    print("Mean-centering")
    feature_means = np.mean(data, axis=0)
    for disease_idx in range(num_diseases):
        data[disease_idx] = np.subtract(data[disease_idx], feature_means)
    # Get PCA-transformed data
    print("PCA Transformation")
    pca_vectors = PCA(n_components=50).fit(data)
    pca_transformed_data = pca_vectors.transform(data)

    # Perform tSNE
    print("TSNE")
    tsne_embedded_symptoms = TSNE(n_components=2, verbose=1).fit_transform(pca_transformed_data)

    # Plot
    print("Plotting")
    plt.figure()
    plt.scatter(tsne_embedded_symptoms[:-1, 0], tsne_embedded_symptoms[:-1, 1], marker='.', color='green', alpha=0.75)
    plt.scatter(tsne_embedded_symptoms[-1, 0], tsne_embedded_symptoms[-1, 1], marker='.', color='black', alpha=1)
    plt.title("tSNE plot of diseases based on symptoms")
    plt.savefig(plot_fname)

if __name__ == "__main__":
    disease_labels = []
    symptom_features = []
    hsdn = []
    with open(os.path.join(os.getcwd(), 'databases', 'disease_labels.p'), 'rb') as f:
        disease_labels = pickle.load(f)
    with open(os.path.join(os.getcwd(), 'databases', 'symptom_features.p'), 'rb') as f:
        symptom_features = pickle.load(f)
    with open(os.path.join(os.getcwd(), 'databases', 'hsdn.p'), 'rb') as f:
        hsdn = pickle.load(f)

    patient_symptom_v1 = np.loadtxt(os.path.join(os.getcwd(), 'patient', 'patient_symptoms_v1.txt'))
    patient_symptom_v2 = np.loadtxt(os.path.join(os.getcwd(), 'patient', 'patient_symptoms_v2.txt'))
    patient_symptom_v3 = np.loadtxt(os.path.join(os.getcwd(), 'patient', 'patient_symptoms_v3.txt'))

    # Patient vector 1
    make_tsne_diagnosis(hsdn, "tsne_symptom_plot_v1.pdf", patient_symptom_v1)