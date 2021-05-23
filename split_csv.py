import pandas as pd

def split():
    df = pd.read_csv('C:/Users/Sara/PycharmProjects/Adoption_survey/templates/Adoption_data.csv')

    common = df.iloc[:, 3:18]
    child = df.iloc[:, 18:24]
    adolescent = df.iloc[:, 24:32]

    common.to_csv('common.csv', index=False,mode="a")
    child.to_csv('child.csv', index=False,mode="a")
    adolescent.to_csv('adolescent.csv', index=False,mode="a")