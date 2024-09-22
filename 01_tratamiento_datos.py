import pandas as pd
import numpy as np

df = pd.read_csv("dataset_1.csv", index_col=0)

print(df)
print(df.describe())
print(df.info())

set_gen = set (df["Género"].to_list())
set_edu = set (df["Nivel_Educación"].to_list())
set_ciu = set (df["Ciudad"].to_list())
# print(set_gen)
# print(set_edu)
# print(set_ciu)

#1. Tratamiento de Valores negativos
df ["Edad"] = df["Edad"].apply(lambda x: np.nan if x < 0 else x)
df ["Ingresos"] = df["Ingresos"].apply(lambda x: np.nan if x < 0 else x)
df ["Hijos"] = df["Hijos"].apply(lambda x: np.nan if x < 0 else x)

#2.Imputar Valores faltantes
for column in ["Edad","Ingresos","Hijos"]:
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)

#3