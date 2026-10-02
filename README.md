# Cancer Treatment Survivability Prediction Model Interface

## Project Description
A python application that predicts survivability of cancer patient's based on medical information, selected treatment option, and response to treatment.

## Repository Structure
```
cancer-treatment-survivability
│   .gitignore                      
│   interface.py                            # Interface for users to enter patient information and recieve survivability prediction
│   README.md
│   requirements.txt                        # Dependencies required for project
│   
├───data
│       cancer_diagnosis_data.csv           # Data downloaded from Kaggle data
│       dataExtract.ipynb                   # Extract data from Kaggle using Kaggle API and perform data exploration
│       
└───model
        encodes_for_categorical_data.json   # Encodings for categorical data fields
        encode_data.py                      # Generate encodings for categorical data and apply encodings for datat to be predicted
        evaluation.py                       # Predict survivability status given data point
        final_model.pkl                     # Saved Decision Tree Classifier pickle file
        model.py                            # Split data and hypertune/train Decision Tree Classifier
        tree_decisions.png                  # Decision tree path
```

## Technologies Used and Requirements
All dependencies can be found in `requirements.txt`. Used Kaggle API to download data from https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset, Scikit-Learn for Decision Tree Classifier model, and nicegui for developing interface.

## Installation and Usage Instructions
First clone this repository on your local machine:
```
git clone https://github.com/srazam/cancer-treatment-survivability.git
```

Then, create a virtual environment in the root directory of the project:
```
python -m venv name-of-venv
```

Activate your virtual environment:
```
source .venv/bin/activate           # Unix/macOS
name-of-venv/Scripts/Activate.ps1   # Windows
```

Download dependencies to virtual environment:
```
pip install -r requirements.txt
```

Run the UI to input patient information for model prediction:
```
python interface.py
```

## Miscellaneous Information
Hypertuned model accuracy was brought to 51%, with an entropy creterion, a max depth of 3, and a minimum leaf sample of 5. 

Where I used AI Assistance from GitHub CoPilot: to understand and properly encode data
- model.py (for updating interaction with encode_data module)
- evaluation.py (for updating interaction with encode_data module and converting respective numerical values)
- encode_data.py (for properly encoding data and saving encodes so that they can be used for data to be predicted)
