import pandas as pd

def load_data():
    # Load data from CSV files
    benin_df = pd.read_csv("../data/benin-malanville.csv")
    sierra_leone_df = pd.read_csv("../data/sierra-leone-bumbuna.csv")
    togo_df = pd.read_csv("../data/togo-dapaong_qc.csv")
    
    # Concatenate dataframes
    data = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
    return data
