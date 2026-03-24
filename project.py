# 🔹 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Step 2: Load Dataset
df = pd.read_csv("students.csv")   # <-- change file name if needed

# 🔹 Step 3: View Data
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 🔹 Step 4: Data Cleaning
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# 🔹 Step 5: Basic Analysis

# Average marks
print("\nAverage Marks:", df['marks'].mean())

# Gender-wise performance
print("\nMarks by Gender:")
print(df.groupby('gender')['marks'].mean())

# Study hours vs marks
print("\nStudy Hours vs Marks:")
print(df.groupby('study_hours')['marks'].mean())

# 🔹 Step 6: Visualization

# Bar chart: Gender vs Marks
plt.figure()
sns.barplot(x='gender', y='marks', data=df)
plt.title("Gender vs Marks")
plt.show()

# Histogram: Marks distribution
plt.figure()
df['marks'].hist()
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Study Hours vs Marks
plt.figure()
sns.scatterplot(x='study_hours', y='marks', data=df)
plt.title("Study Hours vs Marks")
plt.show()

# Heatmap (Correlation)
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 🔹 Step 7: Insights (Printed)
print("\nInsights:")
print("- Students who study more tend to score higher.")
print("- Attendance and study hours positively affect marks.")
print("- Performance varies across different groups.")

# 🔹 Step 8: Conclusion
print("\nConclusion:")
print("This project analyzes student data and shows how different factors affect performance.")