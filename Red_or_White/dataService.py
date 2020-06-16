import pandas as pd

def dataframe():
    redwine = pd.read_csv("data/winequality-red.csv", sep=';')
    redwine.drop("quality",axis =1, inplace = True)
    redwine["Gatunek"] = 'Czerwone wino'
    whitewine = pd.read_csv("data/winequality-white.csv", sep=';')
    whitewine.drop("quality",axis =1, inplace = True)
    whitewine["Gatunek"] = 'Białe wino'
    wina = pd.concat([redwine,whitewine], ignore_index=True)
    return wina

def redwine():
    redwine = pd.read_csv("data/winequality-red.csv", sep=';')
    redwine.drop("quality", axis=1, inplace=True)
    redwine["Gatunek"] = 'Czerwone wino'
    return redwine

def whitewine():
    whitewine = pd.read_csv("data/winequality-white.csv", sep=';')
    whitewine.drop("quality", axis=1, inplace=True)
    whitewine["Gatunek"] = 'Białe wino'
    return whitewine

