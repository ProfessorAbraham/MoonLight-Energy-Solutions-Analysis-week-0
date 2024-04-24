import pandas as pd
import matplotlib.pyplot as plt

# Read CSV files for each area
benin_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\benin-malanville.csv')
sierraleone_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\sierraleone-bumbuna.csv')
togo_data = pd.read_csv(r'C:\Users\Professor Ab\Downloads\data\data\togo-dapaong_qc.csv')

# Display basic information about each dataset
print("Benin Data Info:")
print(benin_data.info())

print("\nSierra Leone Data Info:")
print(sierraleone_data.info())

print("\nTogo Data Info:")
print(togo_data.info())

# Summary statistics for each dataset
print("\nSummary Statistics for Benin:")
print(benin_data.describe())

print("\nSummary Statistics for Sierra Leone:")
print(sierraleone_data.describe())

print("\nSummary Statistics for Togo:")
print(togo_data.describe())

# Check for missing values in each dataset
print("\nMissing Values in Benin:")
print(benin_data.isnull().sum())

print("\nMissing Values in Sierra Leone:")
print(sierraleone_data.isnull().sum())

print("\nMissing Values in Togo:")
print(togo_data.isnull().sum())

# Plot time series data (e.g., GHI, DNI, DHI) for each area
plt.figure(figsize=(12, 6))

try:
    plt.plot(benin_data.index, benin_data['GHI'], label='Benin GHI')
except KeyError:
    print("Error: 'GHI' column not found in Benin dataset.")
except Exception as e:
    print("Error plotting Benin data:", e)

try:
    plt.plot(sierraleone_data.index, sierraleone_data['GHI'], label='Sierra Leone GHI')
except KeyError:
    print("Error: 'GHI' column not found in Sierra Leone dataset.")
except Exception as e:
    print("Error plotting Sierra Leone data:", e)

try:
    plt.plot(togo_data.index, togo_data['GHI'], label='Togo GHI')
except KeyError:
    print("Error: 'GHI' column not found in Togo dataset.")
except Exception as e:
    print("Error plotting Togo data:", e)

plt.title('Global Horizontal Irradiance (GHI) over Time')
plt.xlabel('Timestamp')
plt.ylabel('GHI (W/m²)')
plt.legend()
plt.show()
