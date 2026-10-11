from nicegui import ui
from model import evaluation

ui.page_title("Cancer Treatment Survivability Classification System")
ui.label("Classification System").style('font-size: 200%')

def submit(age, sex, tumor_size, tumor_type, biopsy_result, treatment, response_to_treatment):
    patient_data = {
        'Age': age.value,
        'Gender': sex.value,
        'Tumor_Size(cm)': tumor_size.value,
        'Tumor_Type': tumor_type.value,
        'Biopsy_Result': biopsy_result.value,
        'Treatment': treatment.value,
        'Response_to_Treatment': response_to_treatment.value
    }

    for key in patient_data.keys():
        if key == 'Age':
            try:
                patient_data['Age'] = int(patient_data['Age'])
            except:
                return "Invalid age value"
        elif patient_data["Gender"] == 'Sex':
            return "Invalid sex value" 
        elif key == 'Tumor_Size(cm)':
            try:
                patient_data['Tumor_Size(cm)'] = float(patient_data['Tumor_Size(cm)'])
            except:
                return "Invalid tumor size value"
        elif key.replace("_", " ").lower() == (patient_data[key]).lower():
            return f"Invalid {key.replace("_", " ").lower()} value"

    survivability_status = evaluation.evaluate_patient(patient_data)[0]
    if survivability_status == "Deceased":
        return "Patient may not respond well to treatment. Re-evaluate treatment type."
    else:
        return "Patient will respond well to treatment!"

with ui.tabs() as tabs:
    ui.tab('s', label = 'Survivability Classification')
    ui.tab('t', label = 'Treatment Recommendation')

with ui.tab_panels(tabs, value='s').classes('w-full'):
    with ui.tab_panel('s'):
        ui.html('<p>Enter the following information for your patient:</p>')

        s_age = ui.input(label = "Age")
        s_sex = ui.select(['Sex', 'Male', 'Female'], value = "Sex")
        s_tumor_size = ui.input(label = "Tumor Size (in cm)")
        s_tumor_type = ui.select(['Tumor Type', 'Benign', 'Malignant'], value = 'Tumor Type')
        s_biopsy_result = ui.select(['Biopsy Result', 'Positive', 'Negative'], value = "Biopsy Result")
        s_treatment = ui.select(['Treatment', 'Surgery', 'Radiation Therapy', 'Chemotherapy'], value = "Treatment")
        s_response_to_treatment = ui.select(['Response to Treatment', 'No Response', 'Complete Response', 'Partial Response'], value = "Response to Treatment")
        
        ui.button('Submit',on_click=lambda: ui.label(submit(s_age, s_sex, s_tumor_size, s_tumor_type, s_biopsy_result, s_treatment, s_response_to_treatment)))


    with ui.tab_panel('t'):
        ui.html('<p>Enter the following information for your patient:</p>')
        
        t_age = ui.input(label = "Age")
        t_sex = ui.select(['Sex', 'Male', 'Female'], value = "Sex")
        t_tumor_size = ui.input(label = "Tumor Size (in cm)")
        t_tumor_type = ui.select(['Tumor Type', 'Benign', 'Malignant'], value = 'Tumor Type')
        t_biopsy_result = ui.select(['Biopsy Result', 'Positive', 'Negative'], value = "Biopsy Result")

ui.run()