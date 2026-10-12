# Cancer Tumor Classification System

## Project Description
A python application that predicts whether a tumor is benign and malignant survivability based on a patient's medical information.

## Repository Structure
```
cancer-treatment-survivability
│   .gitignore                      
│   interface.py                            # Interface for users to enter patient information and recieve survivability prediction
│   README.md
│   requirements.txt                        # Dependencies required for project
|   evaluation.py                           # Predict survivability status given data point
|   database.py                             # Implement SQL-Alchemy database to store patient information
│   
├───data
│       Cancer_Data.csv                     # Data downloaded from Kaggle data
│       dataExtract.ipynb                   # Extract data from Kaggle using Kaggle API and perform data exploration
│       feature_ranges.json                 # Bins and counts from histogram graphs for each feature per target class
│       preproc_and_analysis.ipynb          # Remove empty column and create graphs/histograms 
```

## Technologies Used and Requirements
All dependencies can be found in `requirements.txt`. Used Kaggle API to download data from https://www.kaggle.com/datasets/erdemtaha/cancer-data, and nicegui for developing interface.

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
Where I used AI Assistance from GitHub CoPilot: 
To understand and properly encode data
- model.py (for updating interaction with encode_data module)
- evaluation.py (for updating interaction with encode_data module and converting respective numerical values)
- encode_data.py (for properly encoding data and saving encodes so that they can be used for data to be predicted)

To understand why information was not being properly extracted from tabs on the interface:
- interface.py (for updating variable names for the survivability classification tab)

To understand how to do partial prediction to get treatments that would best give positive survivability:
- evaluation.py (Including parts of the compare_treatment_options function to get probability predictions for each target class)
- interface.py (Including parts of compare_treatment_options function but mainly removed to just reuse code from other tab)

To understand SQL Alchemy
- database.py (To know how to interact with the SQL server, mainly overwrote things)
