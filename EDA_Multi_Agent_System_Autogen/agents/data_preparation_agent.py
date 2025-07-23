import pandas as pd

class DataPreparationAgent:
    def clean_data(self, filepath):
        df = pd.read_csv(filepath)
        df = df.dropna()
        df = df.drop_duplicates()
        return df
