from pathlib import Path
import pandas as pd
import json
import database

data_file = Path(__file__).parent / 'data/feature_ranges.json'
data = json.loads(data_file.read_text(encoding='utf-8'))

def diagnose(patient_data, feats, id):
    ranges = {}
    ranges["M"] = {}
    ranges["B"] = {}

    try:
        m_score = 0
        b_score = 0
        for i in feats:
            for key, value in data["malignant"][i].items():
                start, end = key.split("-")
                if patient_data[i] >= float(start) and patient_data[i] <= float(end) and value != 0.0:
                    m_score += 1
                    ranges["M"][i] = {"start": float(start), "end": float(end), "count":value}

            for key, value in data["benign"][i].items():
                start, end = key.split("-")
                if patient_data[i] >= float(start) and patient_data[i] <= float(end) and value != 0.0:
                    b_score += 1
                    ranges["B"][i] = {"start": float(start), "end": float(end), "count":value}

        if m_score == b_score:
            for i in feats:
                try:
                    m_interval = pd.Interval(ranges["M"][i]["start"], ranges["M"][i]["end"])
                    b_interval = pd.Interval(ranges["B"][i]["start"], ranges["B"][i]["end"])

                    if m_interval.overlaps(b_interval):
                        if ranges["B"][i]["count"] > ranges["M"][i]["count"]:
                            b_score += 1 
                        elif ranges["B"][i]["count"] < ranges["M"][i]["count"]:
                            m_score += 1
                except:
                    continue

        if m_score > b_score:
            database.add_patient_info(patient_data, id, 'M')
            return 'M'
        elif b_score > m_score:
            database.add_patient_info(patient_data, id, 'B')
            return 'B'
        else:
            database.add_patient_info(patient_data, id, 'Cannot be determined')
            return 'Cannot be determined'

    except:
        return 'Invalid data value entered'
