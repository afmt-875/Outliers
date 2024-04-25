import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#solo limpio las columnas para las que haré el tratamiento de outliers

df = pd.read_excel('gastos_costos_20_23.xlsx')
print(df[['IVA', 'IMPORTE', 'TOTAL SAT']].isnull().sum())

df['IMPORTE'].fillna(df['TOTAL SAT'] / 1.16, inplace=True)
df['IVA'].fillna(df['IMPORTE'] * 0.16, inplace=True)
df['TOTAL SAT'].fillna(df['IMPORTE'] + df['IVA'], inplace=True)

print(df[['IVA', 'IMPORTE', 'TOTAL SAT']].isnull().sum())

print(df[['IVA', 'IMPORTE', 'TOTAL SAT']].isnull().sum())

df.to_excel('gastos_costos_sin_nulos.xlsx')

