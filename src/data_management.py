import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Caching ensures data is not reloaded unnecessarily in Streamlit
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_houses_data():
    """
    Loads the housing dataset from a CSV file.
    """
    df = pd.read_csv('../outputs/datasets/collection/house_prices_records.csv')
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_data():
    """
    Loads the 4 inherited houses data from a CSV file.
    """
    df_inherited = pd.read_csv("../outputs/datasets/collection/inherited_houses.csv")
    return df_inherited

def load_pkl_file(file_path):
    """
    Loads a serialized object from a pickle (.pkl) file.
    """
    return joblib.load(filename=file_path)
