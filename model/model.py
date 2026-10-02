from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import joblib
import pandas as pd
import encode_data

df = pd.read_csv('../data/cancer_diagnosis_data.csv')
encodeDf = encode_data.encode_data(df, fit=True)

x = encodeDf[['Age', 'Gender', 'Tumor_Size(cm)', 'Tumor_Type', 'Biopsy_Result', 'Treatment', 'Response_to_Treatment']]
y = encodeDf['Survival_Status']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

# Base tree classifier
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

param_grid = {
    'max_depth': range(1, 10, 1),
    'min_samples_leaf': range(1, 20, 2),
    'min_samples_split': range(2, 20, 2),
    'criterion': ["entropy", "gini"]
}

# Hypertuned tree classifier
tunedClassifier = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(estimator=tunedClassifier, param_grid=param_grid,cv=5, verbose=True)
grid_search.fit(x_train, y_train)

print(f"Best accuracy after grid search: {grid_search.best_score_}")
print(f"Parameters of the best estimator:{grid_search.best_estimator_}")

joblib.dump(grid_search.best_estimator_, 'final_model.pkl')

final_model = joblib.load('final_model.pkl')
plt.figure(figsize=(18, 17))
plot_tree(final_model, feature_names = list(x.columns), class_names = list(y.unique()))
plt.savefig('tree_decisions.png')
plt.show()
