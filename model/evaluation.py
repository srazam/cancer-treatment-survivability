import pandas as pd
import joblib
import  model.encode_data as encode_data
from pathlib import Path
import copy

model_file = Path(__file__).parent / 'final_model.pkl'

def evaluate_patient(patient_info):
    df = pd.DataFrame([patient_info])
    encodeDf = encode_data.encode_data(df)

    classifier = joblib.load(model_file)
    return classifier.predict(encodeDf)

def compare_treatment_options(patient_info):
    treatments = ['Chemotherapy', 'Radiation Therapy', 'Surgery']
    responses = ['No Response', 'Partial Response', 'Complete Response']
    scenarios = []

    for treatment in treatments:
        for response in responses:
            nth_scenario = copy.deepcopy(patient_info)
            nth_scenario['Treatment'] = treatment
            nth_scenario['Response_to_Treatment'] = response
            scenarios.append(nth_scenario)

    print(scenarios)
    encoded_scenarios = encode_data.encode_data(pd.DataFrame(scenarios))
    classifier = joblib.load(model_file)
    survival_scores = classifier.predict_proba(encoded_scenarios)

    return survival_scores