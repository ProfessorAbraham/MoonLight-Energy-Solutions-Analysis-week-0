import streamlit as st
import pandas as pd

def load_data():
    # Load data from CSV files
    benin_df = pd.read_csv("../data/benin-malanville.csv")
    sierra_leone_df = pd.read_csv("../data/sierra-leone-bumbuna.csv")
    togo_df = pd.read_csv("")
    return benin_df, sierra_leone_df, togo_df

def main():
    st.title("Solar Farm Data Visualization")

    # Load data
    benin_df, sierra_leone_df, togo_df = load_data()

    # Display dataframes
    st.subheader("Benin Data")
    st.write(benin_df)

    st.subheader("Sierra Leone Data")
    st.write(sierra_leone_df)

    st.subheader("Togo Data")
    st.write(togo_df)

if __name__ == "__main__":
    main()
