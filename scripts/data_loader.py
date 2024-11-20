import pandas as pd
import os


def load_data_from_csv(filename):
    filepath = os.path.join('..', 'data', 'final_tables', filename)
    data = pd.read_csv(filepath)
    return data

def load_data_from_temp(filename):
    filepath = os.path.join('..', 'data', 'temp', filename)
    data = pd.read_csv(filepath)
    return data