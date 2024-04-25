
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
