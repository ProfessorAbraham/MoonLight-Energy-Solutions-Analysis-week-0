# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from scipy import stats

# # Load the datasets
# benin_df = pd.read_csv("../data/benin-malanville.csv")
# sierra_leone_df = pd.read_csv("../data/sierraleone-bumbuna.csv")
# togo_df = pd.read_csv("../data/togo-dapaong_qc.csv")

# # Define a function to perform data cleaning and EDA for each dataset
# def perform_eda(df, country):
#     print("\n=== {} Dataset ===\n".format(country))
#     print("First few rows of the dataset:")
#     print(df.head())

#     print("\nSummary statistics:")
#     print(df.describe())

#     print("\nMissing values:")
#     print(df.isnull().sum())

#     plt.figure(figsize=(12, 8))
#     plt.subplot(2, 2, 1)
#     sns.histplot(df['GHI'], bins=20, kde=True)
#     plt.xlabel('Global Horizontal Irradiance (W/m²)')
#     plt.ylabel('Frequency')
#     plt.title('Distribution of GHI - {}'.format(country))

#     plt.subplot(2, 2, 2)
#     sns.histplot(df['Tamb'], bins=20, kde=True)
#     plt.xlabel('Ambient Temperature (°C)')
#     plt.ylabel('Frequency')
#     plt.title('Distribution of Ambient Temperature - {}'.format(country))

#     plt.subplot(2, 2, 3)
#     sns.boxplot(x=df['Cleaning'], y=df['GHI'])
#     plt.xlabel('Cleaning Event')
#     plt.ylabel('Global Horizontal Irradiance (W/m²)')
#     plt.title('Effect of Cleaning on GHI - {}'.format(country))

#     plt.subplot(2, 2, 4)
#     sns.boxplot(x=df['Cleaning'], y=df['Tamb'])
#     plt.xlabel('Cleaning Event')
#     plt.ylabel('Ambient Temperature (°C)')
#     plt.title('Effect of Cleaning on Ambient Temperature - {}'.format(country))

#     plt.tight_layout()
#     plt.show()

#     # Handle missing values
#     df.dropna(inplace=True)
#     df = df[df['GHI'] >= 0]

#     # Additional data cleaning steps
#     # ...

#     # Check for outliers using z-score method
#     z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI', 'Tamb']])
#     outliers = (z_scores > 3).any(axis=1)
#     print("\nNumber of outliers detected in {} dataset:".format(country), outliers.sum())

#     # Remove outliers
#     df = df[~outliers]

#     # Check summary statistics after additional cleaning
#     print("\nSummary statistics after additional cleaning - {}:".format(country))
#     print(df.describe())

# # Perform EDA for each dataset
# perform_eda(benin_df, "Benin")
# perform_eda(sierra_leone_df, "Sierra Leone")
# perform_eda(togo_df, "Togo")

# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# # # Load the datasets
# # benin_df = pd.read_csv("../data/benin-malanville.csv")
# # sierra_leone_df = pd.read_csv("../data/sierraleone-bumbuna.csv")
# # togo_df = pd.read_csv("../data/togo-dapaong_qc.csv")

# # # EDA for Benin dataset
# # print("\n=== Benin Dataset ===\n")
# # print("First few rows of the dataset:")
# # print(benin_df.head())

# # print("\nSummary statistics:")
# # print(benin_df.describe())

# # print("\nMissing values:")
# # print(benin_df.isnull().sum())

# # plt.figure(figsize=(12, 8))
# # plt.subplot(2, 2, 1)
# # sns.histplot(benin_df['GHI'], bins=20, kde=True)
# # plt.xlabel('Global Horizontal Irradiance (W/m²)')
# # plt.ylabel('Frequency')
# # plt.title('Distribution of GHI - Benin')

# # plt.subplot(2, 2, 2)
# # sns.histplot(benin_df['Tamb'], bins=20, kde=True)
# # plt.xlabel('Ambient Temperature (°C)')
# # plt.ylabel('Frequency')
# # plt.title('Distribution of Ambient Temperature - Benin')

# # plt.subplot(2, 2, 3)
# # sns.boxplot(x=benin_df['Cleaning'], y=benin_df['GHI'])
# # plt.xlabel('Cleaning Event')
# # plt.ylabel('Global Horizontal Irradiance (W/m²)')
# # plt.title('Effect of Cleaning on GHI - Benin')

# # plt.subplot(2, 2, 4)
# # sns.boxplot(x=benin_df['Cleaning'], y=benin_df['Tamb'])
# # plt.xlabel('Cleaning Event')
# # plt.ylabel('Ambient Temperature (°C)')
# # plt.title('Effect of Cleaning on Ambient Temperature - Benin')

# # plt.tight_layout()
# # plt.show()

# # # Handle missing values
# # benin_df.dropna(inplace=True)
# # benin_df = benin_df[benin_df['GHI'] >= 0]

# # # More data cleaning for Benin dataset...

# # # EDA for Sierra Leone dataset
# # print("\n=== Sierra Leone Dataset ===\n")
# # # Similar analysis for Sierra Leone dataset...

# # # EDA for Togo dataset
# # print("\n=== Togo Dataset ===\n")
# # # Similar analysis for Togo dataset...
# # # Remove duplicate rows
# # benin_df.drop_duplicates(inplace=True)

# # # Convert 'Timestamp' column to datetime format
# # benin_df['Timestamp'] = pd.to_datetime(benin_df['Timestamp'])

# # # Extract date and time components
# # benin_df['Date'] = benin_df['Timestamp'].dt.date
# # benin_df['Time'] = benin_df['Timestamp'].dt.time

# # # Drop unnecessary columns
# # benin_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# # # Check for any remaining missing values
# # print("\nRemaining missing values after initial cleaning:")
# # print(benin_df.isnull().sum())

# # # Fill missing values using forward fill method
# # benin_df.fillna(method='ffill', inplace=True)

# # # Check for outliers using z-score method
# # from scipy import stats
# # z_scores = stats.zscore(benin_df[['GHI', 'DNI', 'DHI', 'Tamb']])
# # outliers = (z_scores > 3).any(axis=1)
# # print("\nNumber of outliers detected:", outliers.sum())

# # # Remove outliers
# # benin_df = benin_df[~outliers]

# # # Check summary statistics after additional cleaning
# # print("\nSummary statistics after additional cleaning:")
# # print(benin_df.describe())
# # # 
# # # Remove duplicate rows
# # sierra_leone_df.drop_duplicates(inplace=True)

# # # Convert 'Timestamp' column to datetime format
# # sierra_leone_df['Timestamp'] = pd.to_datetime(sierra_leone_df['Timestamp'])

# # # Extract date and time components
# # sierra_leone_df['Date'] = sierra_leone_df['Timestamp'].dt.date
# # sierra_leone_df['Time'] = sierra_leone_df['Timestamp'].dt.time

# # # Drop unnecessary columns
# # sierra_leone_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# # # Check for any remaining missing values
# # print("\nRemaining missing values after initial cleaning:")
# # print(sierra_leone_df.isnull().sum())

# # # Fill missing values using forward fill method
# # sierra_leone_df.fillna(method='ffill', inplace=True)

# # # Check for outliers using z-score method
# # from scipy import stats
# # z_scores = stats.zscore(sierra_leone_df[['GHI', 'DNI', 'DHI', 'Tamb']])
# # outliers = (z_scores > 3).any(axis=1)
# # print("\nNumber of outliers detected:", outliers.sum())

# # # Remove outliers
# # sierra_leone_df = sierra_leone_df[~outliers]

# # # Check summary statistics after additional cleaning
# # print("\nSummary statistics after additional cleaning:")
# # print(sierra_leone_df.describe())
# # # 
# # # Remove duplicate rows
# # togo_df.drop_duplicates(inplace=True)

# # # Convert 'Timestamp' column to datetime format
# # togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])

# # # Extract date and time components
# # togo_df['Date'] = togo_df['Timestamp'].dt.date
# # togo_df['Time'] = togo_df['Timestamp'].dt.time

# # # Drop unnecessary columns
# # togo_df.drop(['Timestamp', 'Comments'], axis=1, inplace=True)

# # # Check for any remaining missing values
# # print("\nRemaining missing values after initial cleaning:")
# # print(togo_df.isnull().sum())

# # # Fill missing values using forward fill method
# # togo_df.fillna(method='ffill', inplace=True)

# # # Check for outliers using z-score method
# # from scipy import stats
# # z_scores = stats.zscore(togo_df[['GHI', 'DNI', 'DHI', 'Tamb']])
# # outliers = (z_scores > 3).any(axis=1)
# # print("\nNumber of outliers detected:", outliers.sum())

# # # Remove outliers
# # togo_df = togo_df[~outliers]

# # # Check summary statistics after additional cleaning
# # print("\nSummary statistics after additional cleaning:")
# # print(togo_df.describe())
# # # Save the cleaned data frames as .
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Define a list of countries and corresponding file paths
countries = ["Benin", "Sierra Leone", "Togo"]
file_paths = ["../data/benin-malanville.csv", "../data/sierraleone-bumbuna.csv", "../data/togo-dapaong_qc.csv"]

# Loop through each dataset
for country, file_path in zip(countries, file_paths):
    print("\n=== {} Dataset ===\n".format(country))

    # Load the dataset
    df = pd.read_csv(file_path)

    # Print first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Visualizations
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    sns.histplot(df['GHI'], bins=20, kde=True)
    plt.xlabel('Global Horizontal Irradiance (W/m²)')
    plt.ylabel('Frequency')
    plt.title('Distribution of GHI - {}'.format(country))

    plt.subplot(2, 2, 2)
    sns.histplot(df['Tamb'], bins=20, kde=True)
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Ambient Temperature - {}'.format(country))

    plt.subplot(2, 2, 3)
    sns.boxplot(x=df['Cleaning'], y=df['GHI'])
    plt.xlabel('Cleaning Event')
    plt.ylabel('Global Horizontal Irradiance (W/m²)')
    plt.title('Effect of Cleaning on GHI - {}'.format(country))

    plt.subplot(2, 2, 4)
    sns.boxplot(x=df['Cleaning'], y=df['Tamb'])
    plt.xlabel('Cleaning Event')
    plt.ylabel('Ambient Temperature (°C)')
    plt.title('Effect of Cleaning on Ambient Temperature - {}'.format(country))

    plt.tight_layout()
    plt.show()

    # Handle missing values
    df.dropna(inplace=True)
    df = df[df['GHI'] >= 0]

    # Additional data cleaning steps
    # ...

    # Check for outliers using z-score method
    z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI', 'Tamb']])
    outliers = (z_scores > 3).any(axis=1)
    print("\nNumber of outliers detected in {} dataset:".format(country), outliers.sum())

    # Remove outliers
    df = df[~outliers]

    # Check summary statistics after additional cleaning
    print("\nSummary statistics after additional cleaning - {}:".format(country))
    print(df.describe())
