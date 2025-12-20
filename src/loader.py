import pandas as pd

def load_flight_data(path):
    df = pd.read_csv(path)
    return df
