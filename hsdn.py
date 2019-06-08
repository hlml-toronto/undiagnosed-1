import os
import numpy as np


def get_diseases_list():
    diseases = []
    with open(os.path.join(os.getcwd(), 'databases', 'ncomms5212-s1.txt'), 'r') as f:
        line = f.readline()
        for line in f:
            if not line:
                break
            else:
                diseases.append(line)
    return diseases

def get_symptoms_list():
    symptoms = []
    with open(os.path.join(os.getcwd(), 'databases', 'ncomms5212-s2.txt'), 'r') as f:
        f.readline() # throw away first line
        for line in f:
            if not line:
                break
            else:
                symptoms.append(line)
    return symptoms
# ----------------------------------------------
# Globals
# ----------------------------------------------
disease_labels = get_diseases_list()
symptom_features = get_symptoms_list()

# ----------------------------------------------
# Network methods
# ----------------------------------------------


def get_symptoms_for_disease(query_disease):
    symptoms = []
    with open(os.path.join(os.getcwd(), 'databases', 'ncomms5212-s3.txt'), 'r') as f:
        f.readline() # throw away first line
        for line in f:
            if not line:
                break
            else:
                line = line.split("\t")
                if line[1] == query_disease:
                    symptoms.append(line[0])
    return symptoms


def get_symptom_score_for_disease(query_disease, query_symptom):
    with open(os.path.join(os.getcwd(), 'databases', 'ncomms5212-s3.txt'), 'r') as f:
        f.readline()  # throw away first line
        for line in f:
            if not line: # end of file
                return 0 # handles an error in finding disease:symptom
            else:
                line = line.split("\t")
                if (line[1] == query_disease)&(line[0] == query_symptom):
                    return line[3]


def build_symptom_vector(query_disease):
    disease_symptoms = get_symptoms_for_disease(query_disease)
    symptom_vector = []
    for symptom in symptom_features:
        if symptom in disease_symptoms:
            symptom_vector.append(get_symptom_score_for_disease(query_disease, symptom))
        else:
            symptom_vector.append(0)
    return symptom_vector


def build_disease_symptom_matrix():
    disease_symptom_matrix = []
    for disease in disease_labels:
        disease_symptom_matrix.append(build_symptom_vector(disease))
    return disease_symptom_matrix


if __name__ == "__main__":
    disease_symptom_matrix = build_disease_symptom_matrix()
    print(np.shape(disease_symptom_matrix))