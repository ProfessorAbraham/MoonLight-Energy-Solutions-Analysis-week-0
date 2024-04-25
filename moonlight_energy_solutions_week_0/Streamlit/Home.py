import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
benin_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\benin-malanville.csv')
sierraleone_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\sierraleone-bumbuna.csv')
togo_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\togo-dapaong_qc.csv')

# Sidebar
st.sidebar.title('Select Dataset')
selected_dataset = st.sidebar.selectbox('Select dataset', ['Benin', 'Sierra Leone', 'Togo'])

# Main content
st.title('Solar Farm Data Dashboard')

# Display basic information about the selected dataset
st.write(f"**{selected_dataset} Data Info:**")
if selected_dataset == 'Benin':
    st.write(benin_data.info())
elif selected_dataset == 'Sierra Leone':
    st.write(sierraleone_data.info())
elif selected_dataset == 'Togo':
    st.write(togo_data.info())

# Summary statistics for the selected dataset
st.write(f"\n**Summary Statistics for {selected_dataset} Data:**")
if selected_dataset == 'Benin':
    st.write(benin_data.describe())
elif selected_dataset == 'Sierra Leone':
    st.write(sierraleone_data.describe())
elif selected_dataset == 'Togo':
    st.write(togo_data.describe())

# Check for missing values in the selected dataset
st.write(f"\n**Missing Values in {selected_dataset} Data:**")
if selected_dataset == 'Benin':
    st.write(benin_data.isnull().sum())
elif selected_dataset == 'Sierra Leone':
    st.write(sierraleone_data.isnull().sum())
elif selected_dataset == 'Togo':
    st.write(togo_data.isnull().sum())

# Plot time series data (e.g., GHI, DNI, DHI) for the selected dataset
st.write(f"\n**Global Horizontal Irradiance (GHI) over Time for {selected_dataset}:**")
plt.figure(figsize=(12, 6))
if selected_dataset == 'Benin':
    plt.plot(benin_data['Timestamp'], benin_data['GHI'], label='GHI')
elif selected_dataset == 'Sierra Leone':
    plt.plot(sierraleone_data['Timestamp'], sierraleone_data['GHI'], label='GHI')
elif selected_dataset == 'Togo':
    plt.plot(togo_data['Timestamp'], togo_data['GHI'], label='GHI')
plt.title('Global Horizontal Irradiance (GHI) over Time')
plt.xlabel('Timestamp')
plt.ylabel('GHI (W/m²)')
plt.legend()
st.pyplot()

# Perform correlation analysis for the selected dataset
st.write(f"\n**Correlation Matrix for {selected_dataset} Data:**")
if selected_dataset == 'Benin':
    correlation_matrix = benin_data.corr()
elif selected_dataset == 'Sierra Leone':
    correlation_matrix = sierraleone_data.corr()
elif selected_dataset == 'Togo':
    correlation_matrix = togo_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title(f"Correlation Matrix for {selected_dataset} Data")
st.pyplot()
