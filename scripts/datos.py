import pandas as pd

# Cargar el archivo CSV
file_path = 'C:/Users/Daniela/Desktop/Simu3/Sysarmy-2023-2.xlsx.csv'
df = pd.read_csv(file_path)

# Mostrar las primeras filas del dataframe
print(df.head())

# Mostrar los nombres de las columnas
print(df.columns)
