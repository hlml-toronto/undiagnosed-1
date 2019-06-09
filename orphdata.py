import xml.etree.ElementTree as ET
import numpy as np
import pickle

def create_database(DATABASE, FILE):
    # orphadata quantification of certain phenotypes to disease
    FREQUENCY = {'Occasional (29-5%)' : 0.2, 'Frequent (79-30%)' : 0.55, 'Very frequent (99-80%)' : 0.9, 'Obligate (100%)' : 1.0, 'Very rare (<4-1%)' : 0.025, 'Excluded (0%)' : 0.0}

    # loading database
    root = ET.parse( DATABASE + FILE ).getroot()

    # creating dictionary of the database {disease1 : {symptom1 : frequency, symptom2: frequency, ...}, disease12: {symptom1 : frequency, symptom2: frequency, ...}, ...}
    disease_pheno = {}
    for disorder in root.findall('DisorderList/Disorder'):
        disease_pheno[disorder.find('Name').text] = {}# good
        for symptom in disorder.findall('HPODisorderAssociationList/HPODisorderAssociation'):

            disease_pheno[disorder.find('Name').text][symptom.find('HPO/HPOTerm').text] = FREQUENCY[symptom.find('HPOFrequency/Name').text]

    # save database
    with open(DATABASE + 'dictionary_HPO.dat', 'wb') as f:
        pickle.dump( disease_pheno, f )

    # save list of diseases and
    diseases = []; symptoms = []
    for dis in disease_pheno:
        diseases.append( dis )
        for sym in disease_pheno[dis]:
            if sym not in symptoms:
                symptoms.append( sym )

    with open(DATABASE + 'diseases_HPO.dat', 'wb') as f:
        pickle.dump( diseases, f )

    with open(DATABASE + 'symptoms_HPO.dat', 'wb') as f:
        pickle.dump( symptoms, f )

    # create matrix of disease and symptoms (disease, symptom)
    database = []
    for dis in diseases:
        database.append( [ disease_pheno[dis][sym] if sym in disease_pheno[dis] else 0.0 for sym in symptoms ] )

    with open(DATABASE + 'matrix_HPO.dat', 'wb') as f:
        pickle.dump( database, f )

    return 0

def create_patient_symptom_vector(DATABASE, FILE):
    # converting patient symptoms to symptoms in our list
    with open( DATABASE + 'symptom_patient_excel.txt', 'r' ) as f:
        patient_symptoms_excel = f.read().splitlines()
    # previously created whole list of symptoms
    with open( DATABASE + "symptoms_HPO.dat", "rb") as f:
        symptoms = pickle.load(f)

    patient_symptoms = [ 1.0 if sym in patient_symptoms_excel else 0.0 for sym in symptoms ]

    with open(DATABASE + 'rare_syndrome_vector_HPO.dat', 'wb') as f:
        pickle.dump( patient_symptoms, f )

    print( np.sum(patient_symptoms) )

if __name__ == '__main__':
    #directory
    DATABASE = 'databases/orphadata/'
    FILE = 'en_product4_HPO.xml'

    create_database(DATABASE, FILE)
    create_patient_symptom_vector(DATABASE, FILE)
