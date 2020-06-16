import pandas as pd

def dataframe():
    df = pd.read_csv("data/winemag-data-130k-v2.csv", sep=',')
    return df

#dataframe()