from nicegui import ui
import evaluation
from itertools import count
import database

patient_ids = count(1)

features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
            "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se",
            "smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst",
            "texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst",
            "symmetry_worst","fractal_dimension_worst"]

def get_table():
    table = database.return_table()
    
    final_rows = []
    non_empty_feat = []
    final_cols = []
    
    for row in table:
        row_list = list(row)
        ith_row = {}

        ith_row['id'] = row_list[0]
        ith_row['diagnosis'] = row_list[1]

        for i, feat in enumerate(features, start = 2):
            ith_row[feat] = row_list[i]
            if row_list[i] != 0: 
                non_empty_feat.append(feat) 

        final_rows.append(ith_row)

    final_cols.append({'name': 'id', 'label': 'id', 'field': 'id'})
    final_cols.append({'name': 'diagnosis', 'label': 'diagnosis', 'field': 'diagnosis'})

    for feat in features:
        if feat in non_empty_feat:
            final_cols.append({'name': feat, 'label': feat, 'field': feat})

    return final_rows, final_cols

def submit(data, id):
    patient_values = {}
    for key, input_field in data.items():
        patient_values[key] = (0 if input_field.value == '' else float(input_field.value))
    
    feat_only = []
    for key, value in patient_values.items():
        if value != 0:
            feat_only.append(key)
    feats_used.set_text("Values accounting for: " + ", ".join(feat_only))

    result.set_text(evaluation.diagnose(patient_values, feat_only, id))

    update_rows, update_cols = get_table()
    info_table.rows = update_rows
    info_table.columns = update_cols
    info_table.update()

ui.page_title("Cancer Tumor Classification System")
ui.label("Classification System").style('font-size: 200%')

ui.html('<p>Enter the following information for your patient:</p>')
ui.html('<p>Fields left blank will not be accounted for in prediction</p>')
with ui.grid(columns = 5):
    patient_data = { }
    for i in features:
        patient_data[i] = ui.input(label = i)
result = ui.label()
feats_used = ui.label()

ui.button('Submit',on_click=lambda: submit(patient_data, next(patient_ids)))

table_columns = []

rows, cols = get_table()
info_table = ui.table(rows = rows, columns=cols)

ui.run()