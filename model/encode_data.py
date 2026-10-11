import json

from sklearn.preprocessing import LabelEncoder
from pathlib import Path

encoder_file = Path(__file__).parent / 'encodes_for_categorical_data.json'
categorical_data = ['Gender', 'Tumor_Type', 'Biopsy_Result', 'Treatment']
ordinal_data = ["No Response", "Partial Response", "Complete Response"]
features_to_encode = ['Gender', 'Tumor_Type', 'Biopsy_Result', 'Treatment', 'Response_to_Treatment']


def encode_data(df, fit = False):
    encoded_df = df.copy()

    if fit:
        encodes = {}
        for category in categorical_data:
            label_encoder = LabelEncoder()
            label_encoder.fit(encoded_df[category].astype(str))
            encodes[category] = {}
            for index, value in enumerate(label_encoder.classes_):
                encodes[category][str(value)] = index

        encodes['Response_to_Treatment'] = {}
        for index, value in zip(range(0, 3), ordinal_data):
            encodes['Response_to_Treatment'][value] = index
        
        encoder_file.write_text(json.dumps(encodes, indent=4), encoding='utf-8')
    
    encodes = json.loads(encoder_file.read_text(encoding='utf-8'))

    for category in features_to_encode:
        mapping = encodes[category]
        encoded_values = encoded_df[category].astype(str).map(mapping)
        encoded_df[category] = encoded_values.astype('int64')

    return encoded_df