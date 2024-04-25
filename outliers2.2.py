import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('gastos_costos_sin_nulos.xlsx', index_col= 0)
#print(df.head(5))

valores_nulos = df.isnull().sum()
#print(valores_nulos)


fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IMPORTE"], color='red', rwidth=0.50)
plt.title('Histograma de Importe con outliers')
plt.xlabel('Importe')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["IMPORTE"]) 
plt.title("Outliers de Importe")
plt.show()

#Usar cuartiles
y=df["IMPORTE"]
print(y)

p25=y.quantile(0.25) 
p75=y.quantile(0.75) 
print(p25)
print(p75)
iqr= p75 - p25
print(iqr)

Limite_Superior_iqr= p75 + 1.5*iqr
Limite_Inferior_iqr= p25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

#Datos limpios
data_clean_iqr= df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
print(data_clean_iqr.head(5))          

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IMPORTE"]) 
plt.title("Importe sin outliers ")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["IMPORTE"], color='blue', rwidth=0.50)
plt.title('Histograma de Importe sin outliers')
plt.xlabel('Importe')
plt.ylabel('Frecuencia')
plt.show()

y=df["IMPORTE"]
Limite_Superior= y.mean() + 3*y.std()
Limite_Inferior= y.mean() - 3*y.std()
print("Limite superior permitido", Limite_Superior)
print("Limite inferior permitido", Limite_Inferior)

#Datos limpios DE
data_clean_de= df[(y<Limite_Superior)&(y>Limite_Inferior)]
print(data_clean_de.head(5))          

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_de["IMPORTE"]) 
plt.title("Outliers de Importe - DE")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_de["IMPORTE"], color='blue', rwidth=0.50)
plt.title('Histograma de Importe sin outliers -DE')
plt.xlabel('Importe')
plt.ylabel('Frecuencia')
plt.show()

data_clean_iqr["IMPORTE"].to_csv('Importe_clean.xlsx')