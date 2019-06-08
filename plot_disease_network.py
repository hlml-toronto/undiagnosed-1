import numpy as np
from sklearn.manifold import TSNE


if __name__ == "__main__":
    disease_symptom_matrix = build_disease_symptom_matrix()
    print(np.shape(disease_symptom_matrix))
    with open(os.path.join(os.getcwd(), 'databases', 'hsdn.p'), 'wb') as f:
        pickle.dump(disease_symptom_matrix, f)
