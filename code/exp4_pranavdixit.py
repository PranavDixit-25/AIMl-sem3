import pandas as pd
import matplotlib.pyplot as plt

file_path = "student_exam_scores.csv"
df = pd.read_csv(file_path)

print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nStatistics:")
print(df.describe(include='all'))

plt.style.use("ggplot")

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(14, 4))
    
    plt.subplot(1, 3, 1)
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of {column}")
    
    plt.subplot(1, 3, 2)
    plt.boxplot(df[column], vert=False)
    plt.title(f"Boxplot of {column}")
    
    plt.subplot(1, 3, 3)
    df[column].plot(kind='kde', color='green')
    plt.title(f"Density Plot of {column}")
    
    plt.tight_layout()
    plt.show()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    print(f"{column}: Skewness = {df[column].skew():.2f}, Kurtosis = {df[column].kurtosis():.2f}")
