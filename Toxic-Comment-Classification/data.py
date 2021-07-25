from zipfile import ZipFile
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def get_data(next=False):
    folder = "data/data1.zip" if next else "data/data.zip"
    csv_file = "data/data1.csv" if next else "data/data.csv"
    with ZipFile(folder, 'r') as file:
        file.extractall("data/")
        df = pd.read_csv(csv_file)
        os.remove(csv_file)
    return df

def split(df, test_size=.2):
    train, test = train_test_split(df, test_size=test_size)
    return train, test