# import pandas as pd
# import os
# import gdown
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from imblearn.over_sampling import SMOTE
#
# file_id = "1XWydcU314PzUnerMD-aznUHrDcwSKuqM"
# output = 'creditcard.csv'
# url = f"https://drive.google.com/uc?id={file_id}"
# gdown.download(url, output, quiet=False)
#
# if not os.path.exists('data'):
#     os.makedirs('data')
#
# # reading the dataset
# df = pd.read_csv('creditcard.csv')
#
# # data_split = len(df) // 2
# # data_part1 = df.iloc[:data_split]
# # data_part2 = df.iloc[data_split:]
# #
# # data_part1.to_csv('data/creditcard.csv_part_1.csv', index=False)
# # data_part2.to_csv('data/creditcard.csv_part_2.csv', index=False)
# #
# #
# # def read_and_concat_csv(file_parts):
# #     return pd.concat([pd.read_csv(part) for part in file_parts], ignore_index=True)
# #
# # # Reading the dataset from multiple parts
# #
# #
# # creditcard_files = ['data/creditcard.csv_part_1.csv', 'data/creditcard.csv_part_2.csv']
# # df = read_and_concat_csv(creditcard_files)
#
#
# print('Missing values per column:')
# print(df.isnull().sum())
#
# print("Zero values per column:")
# print((df == 0).sum())
#
# # Dropping duplicate rows if any
# df = df.drop_duplicates()
#
# # In the dataset, time and Amount have different scales. ML models work
# # best when they have a similar scale. Therefore, we normalize it.
#
# scaler = StandardScaler()
# df[['Amount', 'Time']] = scaler.fit_transform(df[['Amount', 'Time']])
#
#
# # We need to separate input from output. The values stored in class represent if
# # it's a fraud transaction or not. We need to store this as y for testing.
#
# # we want all the features except for class to use to predict fraud
# X = df.drop(columns=['Class'])
# y = df['Class']
#
# # we need to break the data into training and testing sets
# # 80% of the data is used to train the model through X_train and y_train
# # 20% is used to test the model through X_test and y_test
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # My dataset is highly imbalanced :(
# # When I parsed out the number of fraud cases vs not: its 492/ 284315 (normal data)
# # Now there should be equal representation of the data
#
# smote = SMOTE(random_state=42)
# X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
#
# print("\nOriginal class distribution:")
# print(y.value_counts())
#
# print("\nResampled class distribution:")
# print(pd.Series(y_train_resampled).value_counts())
#
# # Cleaned dataset - yay!!!
#
# X_train_resampled.to_csv('X_train_cleaned.csv', index=False)
# y_train_resampled.to_csv('y_train_cleaned.csv', index=False)
# X_test.to_csv('X_test_cleaned.csv', index=False)
# y_test.to_csv('y_test_cleaned.csv', index=False)
#
# print('My dataset is clean and ready to go!')
#
# # if __name__ == '__main__':
#
