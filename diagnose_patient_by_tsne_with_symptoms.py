import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd


def make_tsne_diagnosis(data, plot_fname, patient_vector, labels):
    # Add patient to data as an unlabelled 'disease'
    labels.append('Patient')
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

    # Get distance from patient point to each disease
    distances = []
    for d in range(np.shape(tsne_embedded_symptoms)[0]-1):
        distances.append([labels[d], ((tsne_embedded_symptoms[d, 0]-tsne_embedded_symptoms[-1, 0])**2 + (tsne_embedded_symptoms[d, 1]-tsne_embedded_symptoms[-1, 1])**2)**0.5])
    # Rank diseases from nearest to farthest
    disease_rank = pd.DataFrame.from_records(distances, columns=['Disease', 'Distance'])
    print(disease_rank.sort_values('Distance', ascending=False))

    # Plot
    print("Plotting")
    plt.figure()
    plt.scatter(tsne_embedded_symptoms[:-1, 0], tsne_embedded_symptoms[:-1, 1], marker='.', color='green', alpha=0.75)
    plt.scatter(tsne_embedded_symptoms[-1, 0], tsne_embedded_symptoms[-1, 1], marker='.', color='black', alpha=1)
    plt.title("tSNE plot of diseases based on symptoms")
    plt.savefig(plot_fname)
    plt.show()
    # Save tSNE embedding
    with open(os.path.join(os.getcwd(), 'patient', 'patient_symptoms_v1_diagnosis.p'), 'wb') as f:
        pickle.dump(tsne_embedded_symptoms, f)


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
    #make_tsne_diagnosis(hsdn, "tsne_symptom_plot_v1.pdf", patient_symptom_v1, disease_labels)
    #make_tsne_diagnosis(hsdn, "tsne_symptom_plot_v2.pdf", patient_symptom_v2, disease_labels)
    make_tsne_diagnosis(hsdn, "tsne_symptom_plot_v3.pdf", patient_symptom_v3, disease_labels)