import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_exam_scores.csv")   

# Show basic info
print("\nDataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Identify numerical and categorical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns
print("\nNumerical Columns:", list(num_cols))
print("Categorical Columns:", list(cat_cols))

# ---------- Pair Plot (numerical vs numerical multivariate) ----------
if len(num_cols) > 1:
    sns.pairplot(df[num_cols])
    plt.suptitle("Pair Plot of Numerical Columns", y=1.02)
    plt.show()

# ---------- Line Plot (numerical vs numerical) ----------
if len(num_cols) >= 2:
    sns.lineplot(x=num_cols[0], y=num_cols[1], data=df)
    plt.title(f"Line Plot of {num_cols[0]} vs. {num_cols[1]}")
    plt.show()

# ---------- Cluster Map (correlation between numerical features) ----------
if len(num_cols) > 1:
    corr = df[num_cols].corr().replace([float("inf"), -float("inf")], 0).fillna(0)
    sns.clustermap(corr, annot=True, cmap="coolwarm")
    plt.suptitle("Clustermap of Numerical Correlations", y=1.05)
    plt.show()

# ---------- Heat Map ----------
if len(num_cols) > 1:
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="YlGnBu")
    plt.title("Heatmap of Numerical Correlations")
    plt.show()

# ---------- Distplot (distribution of one numerical variable) ----------
if len(num_cols) > 0:
    sns.histplot(df[num_cols[0]], kde=True)
    plt.title(f"Distribution of {num_cols[0]}")
    plt.show()

# ---------- Box Plot (numerical vs categorical) ----------
if len(num_cols) > 0 and len(cat_cols) > 0:
    sns.boxplot(x=cat_cols[0], y=num_cols[0], data=df)
    plt.title(f"Boxplot of {num_cols[0]} by {cat_cols[0]}")
    plt.show()

# ---------- Bar Plot (categorical vs numerical) ----------
if len(cat_cols) > 0 and len(num_cols) > 0:
    sns.barplot(x=cat_cols[0], y=num_cols[0], data=df, errorbar=None)
    plt.title(f"Barplot of {num_cols[0]} by {cat_cols[0]}")
    plt.show()

# ---------- Categorical vs Categorical (Count Plot) ----------
if len(cat_cols) > 1:
    sns.countplot(x=cat_cols[0], hue=cat_cols[1], data=df)
    plt.title(f"Countplot of {cat_cols[0]} vs. {cat_cols[1]}")
    plt.show()
