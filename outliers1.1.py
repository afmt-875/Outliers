import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_totales_sinnulos.csv', index_col= 0)
#print(df.head(5))

valores_nulos = df.isnull().sum()
#print(valores_nulos)


fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corrientes")
plt.show()

#Usar cuartiles
y=df["ventas_precios_corrientes"]
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
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Ventas_precios_corriente sin outliers")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes sin outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

y=df["ventas_precios_corrientes"]
Limite_Superior= y.mean() + 3*y.std()
Limite_Inferior= y.mean() - 3*y.std()
print("Limite superior permitido", Limite_Superior)
print("Limite inferior permitido", Limite_Inferior)

#Datos limpios DE
data_clean_de= df[(y<Limite_Superior)&(y>Limite_Inferior)]
print(data_clean_de.head(5))          

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_de["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente - DE")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_de["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con outliers -DE')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
plt.show()

data_clean_iqr["ventas_precios_corrientes"].to_csv('precios_corrientes_clean.csv')

