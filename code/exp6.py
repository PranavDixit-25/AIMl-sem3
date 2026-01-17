import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('full.csv')

print("Original dataset shape:", df.shape)

df_missing = df.copy()
np.random.seed(42)
missing_idx = np.random.choice(df_missing.index, size=50, replace=False)
df_missing.loc[missing_idx, 'Age'] = np.nan

print("\nMissing values in each column:")
print(df_missing.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df_missing.isnull(), cbar=False, cmap="viridis")
plt.title("Missing values (before imputation)")
plt.show()

df_mean = df_missing.copy()
df_mean['Age'] = df_mean['Age'].fillna(df_mean['Age'].mean())

print("\nMissing values after filling 'Age' with mean:")
print(df_mean.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df_mean.isnull(), cbar=False, cmap="viridis")
plt.title("Missing values (after mean imputation)")
plt.show()

df_median = df_missing.copy()
df_median['Age'] = df_median['Age'].fillna(df_median['Age'].median())

print("\nMissing values after filling 'Age' with median:")
print(df_median.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df_median.isnull(), cbar=False, cmap="viridis")
plt.title("Missing values (after median imputation)")
plt.show()

df_arbitrary = df_missing.copy()
df_arbitrary['Cabin'] = df_arbitrary['Cabin'].fillna('Missing')

print("\nMissing values after arbitrary imputation on 'Cabin':")
print(df_arbitrary.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df_arbitrary.isnull(), cbar=False, cmap="viridis")
plt.title("Missing values (after arbitrary imputation)")
plt.show()

ds = sns.load_dataset("titanic")

print("First 5 rows of seaborn Titanic dataset:")
print(ds.head())

print("\nMissing values in seaborn dataset (before handling):")
print(ds.isnull().sum())

ds['age_mean'] = ds['age'].fillna(ds['age'].mean())

ds['age_median'] = ds['age'].fillna(ds['age'].median())

ds['embarked'] = ds['embarked'].fillna(ds['embarked'].mode()[0])

ds = ds.drop(columns=['deck'])

print("\nMissing values after handling seaborn dataset:")
print(ds.isnull().sum())

plt.figure(figsize=(8,5))
plt.hist(ds['age_mean'], bins=30, edgecolor='black', alpha=0.7, label='Mean Imputation')
plt.hist(ds['age_median'], bins=30, edgecolor='black', alpha=0.5, label='Median Imputation')
plt.title("Histogram of Passenger Age (Mean vs Median Imputation)")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
sns.kdeplot(data=ds, x="age_mean", hue="sex", fill=True, common_norm=False, warn_singular=False)
plt.title("Age Distribution by Gender (KDE Plot, Mean Imputation)")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()
