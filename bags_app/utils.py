import pandas as pd
import streamlit as st
import os

# get the absolute path to the directory contain the .csv file
dir_name = os.path.abspath(os.path.dirname(__file__))
# join the bobrza1.csv to directory to get file path
location = os.path.join(dir_name, 'bags.csv')

def load_data(data_filepath=location):
    df = pd.read_csv(data_filepath)
    return df

# DATA_FILEPATH = "bags.csv"

# def load_data(data_filepath=DATA_FILEPATH):
#     df = pd.read_csv(data_filepath)
#     return df

def get_shop(df):
    """Returns the list of shops in the dataset."""
    shop = df["Company"].unique()
    return sorted(shop)

def median(df):
    """gets median on each of the variables"""
    med = df[['Net proceeds  (£)', 'Donated to good causes (£)', 'Not donated (£)']].median()
    return med
