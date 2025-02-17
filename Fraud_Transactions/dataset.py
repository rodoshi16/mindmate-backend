import pandas as pd
import os
import gdown
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

file_id = "1XWydcU314PzUnerMD-aznUHrDcwSKuqM"
output = 'creditcard.csv'
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, output, quiet=False)

# reading the dataset
df = pd.read_csv('creditcard.csv')
os.remove(output)


print('Missing values per column:')
print(df.isnull().sum())

print("Zero values per column:")
print((df == 0).sum())

# Dropping duplicate rows if any
df = df.drop_duplicates()

# In the dataset, time and Amount have different scales. ML models work
# best when they have a similar scale. Therefore, we normalize it.

scaler = StandardScaler()
df[['Amount', 'Time']] = scaler.fit_transform(df[['Amount', 'Time']])


# We need to separate input from output. The values stored in class represent if
# it's a fraud transaction or not. We need to store this as y for testing.

# we want all the features except for class to use to predict fraud
X = df.drop(columns=['Class'])
y = df['Class']

# we need to break the data into training and testing sets
# 80% of the data is used to train the model through X_train and y_train
# 20% is used to test the model through X_test and y_test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# My dataset is highly imbalanced :(
# When I parsed out the number of fraud cases vs not: its 492/ 284315 (normal data)
# Now there should be equal representation of the data

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("\nOriginal class distribution:")
print(y.value_counts())

print("\nResampled class distribution:")
print(pd.Series(y_train_resampled).value_counts())

# Cleaned dataset - yay!!!

print('My dataset is clean and ready to go!')

model = LogisticRegression(max_iter=1000)
model.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
conf_matrix = confusion_matrix(y_val, y_pred)
print(f"Validation Accuracy: {accuracy}")
print(f"Confusion Matrix: \n{conf_matrix}")



