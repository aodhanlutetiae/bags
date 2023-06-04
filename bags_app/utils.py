import pandas as pd
import streamlit as st

DATA_FILEPATH = "data/bags.csv"

def load_data(data_filepath=DATA_FILEPATH):
    df = pd.read_csv(data_filepath)
    return df

def get_shop(df):
    """Returns the list of shops in the dataset."""
    shop = df["Company"].unique()
    return sorted(shop)

def median(df):
    """gets median on each of the variables"""
    med = df[['Net proceeds  (£)', 'Donated to good causes (£)', 'Not donated (£)']].median()
    return med
