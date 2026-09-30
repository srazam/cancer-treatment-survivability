from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('data/cancer_diagnosis_data.csv')
encodeDf = df.copy()

label_encoder = LabelEncoder()
categoricalData = ['Gender', 'Tumor_Type', 'Biopsy_Result', 'Treatment', 'Response_to_Treatment']

for category in categoricalData:
    new_labels = label_encoder.fit_transform(df[category])
    encodeDf[category] = new_labels

    print(f"Original vallues for {category}: {df[category].unique()}")
    print(f"Encoded vallues for {category}: {encodeDf[category].unique()}\n")

x = encodeDf[['Age', 'Gender', 'Tumor_Size(cm)', 'Tumor_Type', 'Biopsy_Result', 'Treatment', 'Response_to_Treatment']]
y = encodeDf['Survival_Status']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
