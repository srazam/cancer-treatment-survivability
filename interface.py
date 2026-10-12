from nicegui import ui
import evaluation

features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
            "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se",
            "smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst",
            "texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst",
            "symmetry_worst","fractal_dimension_worst"]

ui.page_title("Cancer Tumor Classification System")
ui.label("Classification System").style('font-size: 200%')

ui.html('<p>Enter the following information for your patient:</p>')
ui.html('<p>Fields left blank will not be accounted for in prediction</p>')
with ui.grid(columns = 5):
    patient_data = { }
    for i in features:
        patient_data[i] = ui.input(label = i)

ui.button('Submit',on_click=lambda: result.set_text(submit(patient_data)))
result = ui.label()
feats_used = ui.label()

def submit(data):
    patient_values = {}
    for key, input_field in data.items():
        patient_values[key] = (0 if input_field.value == '' else float(input_field.value))
    
    feat_only = []
    for key, value in patient_values.items():
        if value != 0:
            feat_only.append(key)
    feats_used.set_text("Values accounting for: " + ", ".join(feat_only))

    return evaluation.diagnose(patient_values, feat_only)

ui.run()