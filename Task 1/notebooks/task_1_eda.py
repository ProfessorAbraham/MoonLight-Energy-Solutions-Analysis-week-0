import pandas as pd

# Load the datasets
benin_df = pd.read_csv("data/benin_data.csv")
sierra_leone_df = pd.read_csv("data/sierra_leone_data.csv")
togo_df = pd.read_csv("data/togo_data.csv")
# Display the first few rows of the DataFrame
print(benin_df.head())

# Summary statistics
print(benin_df.describe())

# Check for missing values
print(benin_df.isnull().sum())

# Visualize distributions
import matplotlib.pyplot as plt
import seaborn as sns

# Histograms
plt.figure(figsize=(10, 6))
sns.histplot(benin_df['GHI'], bins=20, kde=True)
plt.xlabel('Global Horizontal Irradiance (W/m²)')
plt.ylabel('Frequency')
plt.title('Distribution of GHI in Benin')
plt.show()

# More exploratory analysis...
# Handle missing values
benin_df.dropna(inplace=True)

# Handle outliers
# For example, remove rows where GHI is negative
benin_df = benin_df[benin_df['GHI'] >= 0]

# More data cleaning...
