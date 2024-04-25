import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('gastos_costos_sin_nulos.xlsx', index_col= 0)
#print(df.head(5))

valores_nulos = df.isnull().sum()
#print(valores_nulos)


fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["TOTAL SAT"], color='red', rwidth=0.50)
plt.title('Histograma de Total SAT con outliers')
plt.xlabel('Total SAT')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL SAT"]) 
plt.title("Outliers de Total SAT")
plt.show()

#Usar cuartiles
y=df["TOTAL SAT"]
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
plt.boxplot(data_clean_iqr["TOTAL SAT"]) 
plt.title("Total SAT sin outliers ")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["TOTAL SAT"], color='blue', rwidth=0.50)
plt.title('Histograma de Total SAT sin outliers')
plt.xlabel('Total SAT')
plt.ylabel('Frecuencia')
plt.show()

y=df["TOTAL SAT"]
Limite_Superior= y.mean() + 3*y.std()
Limite_Inferior= y.mean() - 3*y.std()
print("Limite superior permitido", Limite_Superior)
print("Limite inferior permitido", Limite_Inferior)

#Datos limpios DE
data_clean_de= df[(y<Limite_Superior)&(y>Limite_Inferior)]
print(data_clean_de.head(5))          

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_de["TOTAL SAT"]) 
plt.title("Outliers de Total SAT - DE")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_de["TOTAL SAT"], color='blue', rwidth=0.50)
plt.title('Histograma de Total SAT sin outliers -DE')
plt.xlabel('Total SAT')
plt.ylabel('Frecuencia')
plt.show()

data_clean_iqr["TOTAL SAT"].to_csv('Total_SAT_clean.xlsx')