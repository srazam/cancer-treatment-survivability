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

def get_rows():
    table = database.return_table()
    
    final_rows = []
    for row in table:
        row_list = list(row)
        ith_row = {}
        ith_row['id'] = row_list[0]
        ith_row['diagnosis'] = row_list[1]

        for feat, i in zip(features, range(2, len(features))):
            ith_row[feat] = row_list[i]

        final_rows.append(ith_row)

    return final_rows

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

    info_table.rows = get_rows()
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
table_columns.append({'name': 'id', 'label': 'id', 'field': 'id'})
table_columns.append({'name': 'diagnosis', 'label': 'diagnosis', 'field': 'diagnosis'})

for i in features:
    table_columns.append({
        'name': i,
        'label': i,
        'field': i
    })

info_table = ui.table(rows=get_rows(), columns=table_columns)



ui.run()