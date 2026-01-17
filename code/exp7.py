import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("full.csv")

cat_cols = df.select_dtypes(include=['object']).columns
print("\nMissing values in categorical columns:")
print(df[cat_cols].isnull().sum())

missing_cat = df[cat_cols].isnull().sum()
missing_cat_nonzero = missing_cat[missing_cat > 0]

if not missing_cat_nonzero.empty:
    plt.figure(figsize=(8,4))
    sns.barplot(x=missing_cat_nonzero.index, y=missing_cat_nonzero.values, palette="mako")
    plt.title("Missing Values in Categorical Columns")
    plt.ylabel("Count")
    plt.show()

plt.figure(figsize=(10, 4))
sns.heatmap(df[cat_cols].isnull(), cbar=False, cmap="YlGnBu", yticklabels=False)
plt.title("Missing Values Heatmap (Before Imputation)")
plt.show()

df_mode = df.copy()
for col in cat_cols:
    df_mode[col] = df_mode[col].fillna(df_mode[col].mode()[0])

plt.figure(figsize=(10, 4))
sns.heatmap(df_mode[cat_cols].isnull(), cbar=False, cmap="YlGnBu", yticklabels=False)
plt.title("Missing Values Heatmap (After Mode Imputation)")
plt.show()

plt.figure(figsize=(7,4))
sns.countplot(data=df, x="Embarked")
plt.title("Embarked Distribution (Before Imputation)")
plt.show()

plt.figure(figsize=(7,4))
sns.countplot(data=df_mode, x="Embarked")
plt.title("Embarked Distribution (After Mode Imputation)")
plt.show()

if "Age" in df.columns and "Sex" in df.columns:
    plt.figure(figsize=(8,5))
    for category in df["Sex"].dropna().unique():
        sns.kdeplot(data=df[df["Sex"] == category], x="Age", fill=True, label=category, alpha=0.5)
    plt.title("KDE Plot of Age by Sex")
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.legend(title="Sex")
    plt.show()

if "Age" in df.columns and "Embarked" in df.columns:
    plt.figure(figsize=(8,5))
    for category in df["Embarked"].dropna().unique():
        sns.kdeplot(data=df[df["Embarked"] == category], x="Age", fill=True, label=category, alpha=0.5)
    plt.title("KDE Plot of Age by Embarked")
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.legend(title="Embarked")
    plt.show()
