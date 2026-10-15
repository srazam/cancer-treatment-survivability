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
|   tests.py                                # Tests to check evaluation metrics are consistent
│   
├───data
│       Cancer_Data.csv                     # Data downloaded from Kaggle data
│       dataExtract.ipynb                   # Extract data from Kaggle using Kaggle API and perform data exploration
│       feature_ranges.json                 # Bins and counts from histogram graphs for each feature per target class
│       preproc_and_analysis.ipynb          # Remove empty column and create graphs/histograms 
```

## Technologies Used and Requirements
The application's runtime dependencies are listed in `requirements.txt`. Install them into your virtual environment with `pip install -r requirements.txt`.

The Kaggle API is used to download data from https://www.kaggle.com/datasets/erdemtaha/cancer-data.

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
source name-of-venv/bin/activate        # Unix/macOS
name-of-venv/Scripts/Activate.ps1       # Windows
```

Download dependencies to virtual environment:
```
pip install -r requirements.txt
```

Run the UI to input patient information for model prediction:
```
python interface.py
```

## Tests
Tests are written using UnitTest library to check that evaluations are consistent and that data is properly being added to the database. They can be found in the `test.py` file.

## AI Agent Log
Where I used AI Assistance from GitHub CoPilot: 

To understand why information was not being properly extracted from tabs on the interface:
- interface.py (for updating variable names for the survivability classification tab)

To understand SQL Alchemy
- database.py (To know how to interact with the SQL server, mainly overwrote things)

To assist in debugging of table preview on interface
- interface.py (Using enumerate instead of zip to iterate through the features and understanding that updating columns for a table in nicegui is not overwriting currently existing columns)

To update requirements.txt file with necessary dependencies only and to partially update README file with information about the file. 