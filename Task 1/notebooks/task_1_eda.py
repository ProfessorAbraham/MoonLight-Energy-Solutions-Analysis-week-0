import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
benin_df = pd.read_csv("data/benin_data.csv")
sierra_leone_df = pd.read_csv("data/sierra_leone_data.csv")
togo_df = pd.read_csv("data/togo_data.csv")

# EDA for Benin dataset
print("\n=== Benin Dataset ===\n")
print("First few rows of the dataset:")
print(benin_df.head())

print("\nSummary statistics:")
print(benin_df.describe())

print("\nMissing values:")
print(benin_df.isnull().sum())

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.histplot(benin_df['GHI'], bins=20, kde=True)
plt.xlabel('Global Horizontal Irradiance (W/m²)')
plt.ylabel('Frequency')
plt.title('Distribution of GHI - Benin')

plt.subplot(2, 2, 2)
sns.histplot(benin_df['Tamb'], bins=20, kde=True)
plt.xlabel('Ambient Temperature (°C)')
plt.ylabel('Frequency')
plt.title('Distribution of Ambient Temperature - Benin')

plt.subplot(2, 2, 3)
sns.boxplot(x=benin_df['Cleaning'], y=benin_df['GHI'])
plt.xlabel('Cleaning Event')
plt.ylabel('Global Horizontal Irradiance (W/m²)')
plt.title('Effect of Cleaning on GHI - Benin')

plt.subplot(2, 2, 4)
sns.boxplot(x=benin_df['Cleaning'], y=benin_df['Tamb'])
plt.xlabel('Cleaning Event')
plt.ylabel('Ambient Temperature (°C)')
plt.title('Effect of Cleaning on Ambient Temperature - Benin')

plt.tight_layout()
plt.show()

# Handle missing values
benin_df.dropna(inplace=True)
benin_df = benin_df[benin_df['GHI'] >= 0]

# More data cleaning for Benin dataset...

# EDA for Sierra Leone dataset
print("\n=== Sierra Leone Dataset ===\n")
# Similar analysis for Sierra Leone dataset...

# EDA for Togo dataset
print("\n=== Togo Dataset ===\n")
# Similar analysis for Togo dataset...
# Remove duplicate rows
benin_df.drop_duplicates(inplace=True)

# Convert 'Timestamp' column to datetime format
benin_df['Timestamp'] = pd.to_datetime(benin_df['Timestamp'])

# Extract date and time components
benin_df['Date'] = benin_df['Timestamp'].dt.date
benin_df['Time'] = benin_df['Timestamp'].dt.time

# Drop unnecessary columns
benin_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# Check for any remaining missing values
print("\nRemaining missing values after initial cleaning:")
print(benin_df.isnull().sum())

# Fill missing values using forward fill method
benin_df.fillna(method='ffill', inplace=True)

# Check for outliers using z-score method
from scipy import stats
z_scores = stats.zscore(benin_df[['GHI', 'DNI', 'DHI', 'Tamb']])
outliers = (z_scores > 3).any(axis=1)
print("\nNumber of outliers detected:", outliers.sum())

# Remove outliers
benin_df = benin_df[~outliers]

# Check summary statistics after additional cleaning
print("\nSummary statistics after additional cleaning:")
print(benin_df.describe())
# 
# Remove duplicate rows
sierra_leone_df.drop_duplicates(inplace=True)

# Convert 'Timestamp' column to datetime format
sierra_leone_df['Timestamp'] = pd.to_datetime(sierra_leone_df['Timestamp'])

# Extract date and time components
sierra_leone_df['Date'] = sierra_leone_df['Timestamp'].dt.date
sierra_leone_df['Time'] = sierra_leone_df['Timestamp'].dt.time

# Drop unnecessary columns
sierra_leone_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# Check for any remaining missing values
print("\nRemaining missing values after initial cleaning:")
print(sierra_leone_df.isnull().sum())

# Fill missing values using forward fill method
sierra_leone_df.fillna(method='ffill', inplace=True)

# Check for outliers using z-score method
from scipy import stats
z_scores = stats.zscore(sierra_leone_df[['GHI', 'DNI', 'DHI', 'Tamb']])
outliers = (z_scores > 3).any(axis=1)
print("\nNumber of outliers detected:", outliers.sum())

# Remove outliers
sierra_leone_df = sierra_leone_df[~outliers]

# Check summary statistics after additional cleaning
print("\nSummary statistics after additional cleaning:")
print(sierra_leone_df.describe())
# 
# Remove duplicate rows
togo_df.drop_duplicates(inplace=True)

# Convert 'Timestamp' column to datetime format
togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])

# Extract date and time components
togo_df['Date'] = togo_df['Timestamp'].dt.date
togo_df['Time'] = togo_df['Timestamp'].dt.time

# Drop unnecessary columns
togo_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# Check for any remaining missing values
print("\nRemaining missing values after initial cleaning:")
print(togo_df.isnull().sum())

# Fill missing values using forward fill method
togo_df.fillna(method='ffill', inplace=True)

# Check for outliers using z-score method
from scipy import stats
z_scores = stats.zscore(togo_df[['GHI', 'DNI', 'DHI', 'Tamb']])
outliers = (z_scores > 3).any(axis=1)
print("\nNumber of outliers detected:", outliers.sum())

# Remove outliers
togo_df = togo_df[~outliers]

# Check summary statistics after additional cleaning
print("\nSummary statistics after additional cleaning:")
print(togo_df.describe())
# Save the cleaned data frames as .
