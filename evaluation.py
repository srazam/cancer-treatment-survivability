from pathlib import Path
import pandas as pd
import json

data_file = Path(__file__).parent / 'data/feature_ranges.json'
data = json.loads(data_file.read_text(encoding='utf-8'))

def diagnose(patient_data, feats):
    ranges = {}
    ranges["M"] = {}
    ranges["B"] = {}

    try:
        m_score = 0
        b_score = 0
        for i in feats:
            for key, value in data["malignant"][i].items():
                start, end = key.split("-")
                if patient_data[i] >= float(start) and patient_data[i] <= float(end):
                    m_score += 1
                    ranges["M"][i] = {"start": start, "end": end, "count":value}

            for key, value in data["benign"][i].items():
                start, end = key.split("-")
                if patient_data[i] >= float(start) and patient_data[i] <= float(end):
                    b_score += 1
                    ranges["B"][i] = {"start": start, "end": end, "count":value}

        if m_score == b_score:
            for i in feats:
                try:
                    m_interval = pd.Interval(ranges["M"][i][start], ranges["M"][i][end])
                    b_interval = pd.Interval(ranges["B"][i][start], ranges["B"][i][end])

                    if m_interval.overlaps(b_interval):
                        if ranges["B"][i]["count"] > ranges["M"][i]["count"]:
                            b_score += 1 
                        else:
                            m_score += 1
                except:
                    continue
                        
        if m_score > b_score:
            return 'M'
        else:
            return 'B'

    except:
        return 'Invalid data value entered'
