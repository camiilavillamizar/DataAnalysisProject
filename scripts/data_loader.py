import pandas as pd
import os

def load_data(folder, filename):
    filepath = os.path.join('..', 'data', folder, filename)
    data = pd.read_csv(filepath)
    return data

def load_data_from_csv(filename):
    return load_data('final_tables', filename)

def load_data_from_temp(filename):
    return load_data('temp', filename)

def load_data_from_filtered(filename):
    return load_data('filtered_tables', filename)