import pandas as pd
import joblib
import  model.encode_data as encode_data
from pathlib import Path

model_file = Path(__file__).parent / 'final_model.pkl'

def evaluate_patient(patient_info):
    df = pd.DataFrame([patient_info])
    encodeDf = encode_data.encode_data(df)

    classifier = joblib.load(model_file)
    return classifier.predict(encodeDf)