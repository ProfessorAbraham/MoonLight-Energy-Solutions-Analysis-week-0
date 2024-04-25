# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the datasets
# benin_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\benin-malanville.csv')
# sierraleone_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\sierraleone-bumbuna.csv')
# togo_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\togo-dapaong_qc.csv')

# # Sidebar
# st.sidebar.title('Select Dataset')
# selected_dataset = st.sidebar.selectbox('Select dataset', ['Benin', 'Sierra Leone', 'Togo'])

# # Main content
# st.title('Solar Farm Data Dashboard')

# # Display basic information about the selected dataset
# st.write(f"**{selected_dataset} Data Info:**")
# if selected_dataset == 'Benin':
#     st.write(benin_data.info())
# elif selected_dataset == 'Sierra Leone':
#     st.write(sierraleone_data.info())
# elif selected_dataset == 'Togo':
#     st.write(togo_data.info())

# # Summary statistics for the selected dataset
# st.write(f"\n**Summary Statistics for {selected_dataset} Data:**")
# if selected_dataset == 'Benin':
#     st.write(benin_data.describe())
# elif selected_dataset == 'Sierra Leone':
#     st.write(sierraleone_data.describe())
# elif selected_dataset == 'Togo':
#     st.write(togo_data.describe())

# # Check for missing values in the selected dataset
# st.write(f"\n**Missing Values in {selected_dataset} Data:**")
# if selected_dataset == 'Benin':
#     st.write(benin_data.isnull().sum())
# elif selected_dataset == 'Sierra Leone':
#     st.write(sierraleone_data.isnull().sum())
# elif selected_dataset == 'Togo':
#     st.write(togo_data.isnull().sum())

# # Plot time series data (e.g., GHI, DNI, DHI) for the selected dataset
# st.write(f"\n**Global Horizontal Irradiance (GHI) over Time for {selected_dataset}:**")
# plt.figure(figsize=(12, 6))
# if selected_dataset == 'Benin':
#     plt.plot(benin_data['Timestamp'], benin_data['GHI'], label='GHI')
# elif selected_dataset == 'Sierra Leone':
#     plt.plot(sierraleone_data['Timestamp'], sierraleone_data['GHI'], label='GHI')
# elif selected_dataset == 'Togo':
#     plt.plot(togo_data['Timestamp'], togo_data['GHI'], label='GHI')
# plt.title('Global Horizontal Irradiance (GHI) over Time')
# plt.xlabel('Timestamp')
# plt.ylabel('GHI (W/m²)')
# plt.legend()
# st.pyplot()

# # Perform correlation analysis for the selected dataset
# st.write(f"\n**Correlation Matrix for {selected_dataset} Data:**")
# if selected_dataset == 'Benin':
#     correlation_matrix = benin_data.corr()
# elif selected_dataset == 'Sierra Leone':
#     correlation_matrix = sierraleone_data.corr()
# elif selected_dataset == 'Togo':
#     correlation_matrix = togo_data.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title(f"Correlation Matrix for {selected_dataset} Data")
# st.pyplot()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_eda(df, country):
    st.subheader("=== {} Dataset ===".format(country))

    # Display first few rows
    st.write("First few rows of the dataset:")
    st.write(df.head())

    # Summary statistics
    st.write("Summary statistics:")
    st.write(df.describe())

    # Missing values
    st.write("Missing values:")
    st.write(df.isnull().sum())

    # Visualizations
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Visualizations for {}".format(country))

    sns.histplot(df['GHI'], bins=20, kde=True, ax=axs[0, 0])
    axs[0, 0].set_title('Distribution of GHI')
    axs[0, 0].set_xlabel('Global Horizontal Irradiance (W/m²)')
    axs[0, 0].set_ylabel('Frequency')

    sns.histplot(df['Tamb'], bins=20, kde=True, ax=axs[0, 1])
    axs[0, 1].set_title('Distribution of Ambient Temperature')
    axs[0, 1].set_xlabel('Ambient Temperature (°C)')
    axs[0, 1].set_ylabel('Frequency')

    sns.boxplot(x=df['Cleaning'], y=df['GHI'], ax=axs[1, 0])
    axs[1, 0].set_title('Effect of Cleaning on GHI')
    axs[1, 0].set_xlabel('Cleaning Event')
    axs[1, 0].set_ylabel('Global Horizontal Irradiance (W/m²)')

    sns.boxplot(x=df['Cleaning'], y=df['Tamb'], ax=axs[1, 1])
    axs[1, 1].set_title('Effect of Cleaning on Ambient Temperature')
    axs[1, 1].set_xlabel('Cleaning Event')
    axs[1, 1].set_ylabel('Ambient Temperature (°C)')

    st.pyplot(fig)

    # Handle missing values
    df.dropna(inplace=True)
    df = df[df['GHI'] >= 0]

    # Additional data cleaning steps
    # ...

    # Check for outliers using z-score method
    z_scores = stats.zscore(df[['GHI', 'DNI', 'DHI', 'Tamb']])
    outliers = (z_scores > 3).any(axis=1)
    st.write("\nNumber of outliers detected in {} dataset:".format(country), outliers.sum())

    # Remove outliers
    df = df[~outliers]

    # Check summary statistics after additional cleaning
    st.write("\nSummary statistics after additional cleaning - {}:".format(country))
    st.write(df.describe())

def main():
    st.title("Energy Solutions Data Analysis Dashboard")

    # Define a list of countries and corresponding file paths
    countries = ["Benin", "Sierra Leone", "Togo"]
    file_paths = ["../data/benin-malanville.csv", "../data/sierraleone-bumbuna.csv", "../data/togo-dapaong_qc.csv"]

    # Load and perform EDA for each dataset
    for country, file_path in zip(countries, file_paths):
        df = load_data(file_path)
        perform_eda(df, country)

if __name__ == "__main__":
    main()
