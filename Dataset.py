import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame from iris data
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Example for cleaning if missing values were present:
# df.fillna(df.mean(), inplace=True)  # Fill numerical missing values with mean
# or
# df.dropna(inplace=True)  # Drop rows with missing values


# Basic statistics
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Group by species and compute mean sepal length
grouped_means = df.groupby('species')['sepal length (cm)'].mean()
print("\nMean sepal length per species:")
print(grouped_means)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # seaborn style

# 1. Line chart - sepal length trend over sample index
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['sepal length (cm)'], marker='o', linestyle='-', color='b')
plt.title("Sepal Length Trend Over Sample Index")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of petal width
plt.figure(figsize=(6, 4))
sns.histplot(df['petal width (cm)'], bins=20, kde=True, color='purple')
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

try:
    df_custom = pd.read_csv('your_dataset.csv')
    print(df_custom.head())
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: File is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
