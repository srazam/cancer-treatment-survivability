from nicegui import ui
import model.evaluation as evaluation

ui.html('<h4>Enter the following information for your patient:</h4>')

age = ui.input(label = "Age")
sex = ui.select(['Sex', 'Male', 'Female'], value = "Sex")
tumor_size = ui.input(label = "Tumor Size (in cm)")
tumor_type = ui.select(['Tumor Type', 'Benign', 'Malignant'], value = 'Tumor Type')
biopsy_result = ui.select(['Biopsy Result', 'Positive', 'Negative'], value = "Biopsy Result")
treatment = ui.select(['Treatment', 'Surgery', 'Radiation Therapy', 'Chemotherapy'], value = "Treatment")
response_to_treatment = ui.select(['Response to Treatment', 'No Response', 'Complete Response', 'Partial Response'], value = "Response to Treatment")

ui.button('Submit',on_click=lambda: submit())
label = ui.label()

def submit():
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
        label.text = ""

        if key == 'age':
            try:
                patient_data['Age'] = int(patient_data['age'])
            except:
                label.text = "Invalid age value"
                return
        elif key == 'tumor_size':
            try:
                patient_data['Tumor_Size'] = float(patient_data['tumor_size'])
            except:
                label.text = "Invalid tumor size value"
                return
        elif key.replace("_", " ") == (patient_data[key]).lower() or len(patient_data[key]) == 0:
            label.text = f"Invalid {key.replace("_", " ")} value"
            return

        label.text = "Evaluating..."
        print(evaluation.evaluate_patient(patient_data))



ui.run()