import os
import pandas as pd
import pickle
from numpy import nan
import csv
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
    col_names = ['symptom', 'MeSH', 'detailed symptom', 'Nature','Age','Date','Organization','Filename','Page','Comments']
    patient_symptoms = pd.read_csv(os.path.join(os.getcwd(), 'databases', 'medicaldata_MERGE_RAWSymptoms.csv'),
                                   header=None, index_col=False, names=col_names)
    patient_symptoms_MeSH = patient_symptoms['MeSH'].dropna().drop_duplicates().values
    symptom_count = len(patient_symptoms_MeSH)
    matching_symptom_count = 0
    matching_symptom_list = []
    print("There are {} symptoms recorded".format(symptom_count))
    for s in patient_symptoms_MeSH:
        if s is not nan:
            if s in symptom_features:
                # print("{} is not in the database".format(s))
                matching_symptom_count += 1
                matching_symptom_list.append(s)
    print("There are {} symptoms matching".format(matching_symptom_count))
    print("The symptoms are:")
    print(matching_symptom_list)

    # Build base patient symptom vector
    patient_symptoms_v1 = []
    for s in symptom_features:
        if s in matching_symptom_list:
            patient_symptoms_v1.append(1)
        else:
            patient_symptoms_v1.append(0)
    with open(os.path.join(os.getcwd(), 'patient', 'patient_symptoms_v1.csv'), 'w') as f:
        wr = csv.writer(f)
        wr.writerow(patient_symptoms_v1)

