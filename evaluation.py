from pathlib import Path
import pandas as pd
import json

data_file = Path(__file__).parent / 'data/feature_ranges.json'
data = json.loads(data_file.read_text(encoding='utf-8'))
features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
            "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se",
            "smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst",
            "texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst",
            "symmetry_worst","fractal_dimension_worst"]


fake_data = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
patient_data = {}
for i, j in zip(features, fake_data):
    patient_data[i] = j

def diagnose(patient_data):
    m_score = 0
    b_score = 0
    for i in features:
        for key, value in data["malignant"][i].items():
            start, end = key.split("-")
            if patient_data[i] >= float(start) and patient_data[i] <= float(end):
                m_score += 1

        for key, value in data["benign"][i].items():
            start, end = key.split("-")
            if patient_data[i] >= float(start) and patient_data[i] <= float(end):
                b_score += 1

    if m_score == b_score:
        for i in features:
            for m_key, m_value in data["malignant"][i].items():
                for b_key, b_value in data["benign"][i].items():
                    m_start, m_end = m_key.split("-")
                    b_start, b_end = b_key.split("-")

                    m_interval = pd.Interval(m_start, m_end)
                    b_interval = pd.Interval(b_start, b_end)

                    if m_interval.overlaps(b_interval):
                        if b_value > m_value:
                            b_score += 1 
                        else:
                            m_score += 1
                    

    if m_score > b_score:
        return 'M'
    else:
        return 'B'

print(diagnose(patient_data))