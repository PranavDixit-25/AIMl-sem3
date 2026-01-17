import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder

df = pd.read_csv("full.csv")

data = df[['Survived', 'Pclass', 'Sex', 'Age']].copy()
data['Age'].fillna(data['Age'].mean(), inplace=True)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(x='Sex', data=data)
plt.title("Count of Sex Before Encoding")
plt.subplot(1, 2, 2)
sns.countplot(x='Pclass', data=data)
plt.title("Count of Pclass Before Encoding")
plt.show()

encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded = encoder.fit_transform(data[['Sex', 'Pclass']])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Sex', 'Pclass']))
data_encoded = pd.concat([data.drop(['Sex', 'Pclass'], axis=1), encoded_df], axis=1)

encoded_counts = data_encoded.iloc[:, - (encoded_df.shape[1]):].sum().reset_index()
encoded_counts.columns = ['Encoded Feature', 'Count']
plt.figure(figsize=(8, 4))
sns.barplot(data=encoded_counts, x='Encoded Feature', y='Count')
plt.title("Bar graph of One Hot Encoded Features")
plt.show()

scaler_standard = StandardScaler()
scaler_minmax = MinMaxScaler()
scaled_standard = scaler_standard.fit_transform(data_encoded[['Age']])
scaled_minmax = scaler_minmax.fit_transform(data_encoded[['Age']])
data_encoded['Age_StandardScaled'] = scaled_standard
data_encoded['Age_MinMaxScaled'] = scaled_minmax

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.kdeplot(data_encoded['Age'], color='blue', fill=True)
plt.title("Original Age Distribution")
plt.subplot(1, 2, 2)
sns.kdeplot(data_encoded['Age_MinMaxScaled'], color='green', fill=True)
plt.title("MinMax Scaled Age Distribution")
plt.show()

print(data_encoded.describe())
