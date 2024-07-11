import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Cargar el archivo CSV
file_path = 'C:/Users/Daniela/Desktop/Simu3/Sysarmy-2023-2.xlsx.csv'
df = pd.read_csv(file_path)

# Convertir la columna de salario bruto a numérica
df['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local'] = pd.to_numeric(df['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local'], errors='coerce')

# Eliminar filas con valores nulos en la columna de salario
df = df.dropna(subset=['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local'])

# Obtener estadísticas descriptivas básicas
salario_bruto = df['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local']
print(salario_bruto.describe())

# Boxplot del salario bruto mensual
plt.figure(figsize=(10, 6))
sns.boxplot(x=salario_bruto)
plt.title('Boxplot del Salario Bruto Mensual')
plt.xlabel('Salario Bruto Mensual (en moneda local)')
plt.savefig('boxplot_salario.png')  # Guardar gráfico
plt.close()

# Histograma del salario bruto mensual
plt.figure(figsize=(10, 6))
sns.histplot(salario_bruto, kde=True)
plt.title('Histograma del Salario Bruto Mensual')
plt.xlabel('Salario Bruto Mensual (en moneda local)')
plt.ylabel('Frecuencia')
plt.savefig('histograma_salario.png')  # Guardar gráfico
plt.close()

# Análisis comparativo por género
df_genero = df[['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', 'me_identifico_genero']].dropna()
genero_groups = df_genero.groupby('me_identifico_genero')

# Salario medio por género
salario_medio_genero = genero_groups.mean()
print(salario_medio_genero)

# Boxplot del salario bruto mensual por género
plt.figure(figsize=(10, 6))
sns.boxplot(x='me_identifico_genero', y='ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', data=df_genero)
plt.title('Boxplot del Salario Bruto Mensual por Género')
plt.xlabel('Género')
plt.ylabel('Salario Bruto Mensual (en moneda local)')
plt.savefig('boxplot_salario_genero.png')  # Guardar gráfico
plt.close()

# Test t de Student para comparar salarios entre géneros
hombres = df_genero[df_genero['me_identifico_genero'] == 'Hombre']['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local']
mujeres = df_genero[df_genero['me_identifico_genero'] == 'Mujer']['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local']

t_stat, p_value = stats.ttest_ind(hombres, mujeres, equal_var=False)
print(f"t-statistic: {t_stat}, p-value: {p_value}")

# Conclusión del análisis comparativo
if p_value < 0.05:
    print("Existe una diferencia significativa en el salario mensual bruto entre hombres y mujeres.")
else:
    print("No existe una diferencia significativa en el salario mensual bruto entre hombres y mujeres.")

# Análisis comparativo por seniority
df_seniority = df[['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', 'seniority']].dropna()
seniority_groups = df_seniority.groupby('seniority')

# Salario medio por seniority
salario_medio_seniority = seniority_groups.mean()
print(salario_medio_seniority)

# Boxplot del salario bruto mensual por seniority
plt.figure(figsize=(10, 6))
sns.boxplot(x='seniority', y='ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', data=df_seniority)
plt.title('Boxplot del Salario Bruto Mensual por Seniority')
plt.xlabel('Seniority')
plt.ylabel('Salario Bruto Mensual (en moneda local)')
plt.savefig('boxplot_salario_seniority.png')  # Guardar gráfico
plt.close()

# Análisis comparativo por región
df_region = df[['ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', 'estoy_trabajando_en']].dropna()
region_groups = df_region.groupby('estoy_trabajando_en')

# Salario medio por región
salario_medio_region = region_groups.mean()
print(salario_medio_region)

# Boxplot del salario bruto mensual por región
plt.figure(figsize=(10, 6))
sns.boxplot(x='estoy_trabajando_en', y='ultimo_salario_mensual_o_retiro_bruto_en_tu_moneda_local', data=df_region)
plt.title('Boxplot del Salario Bruto Mensual por Región')
plt.xlabel('Región')
plt.ylabel('Salario Bruto Mensual (en moneda local)')
plt.savefig('boxplot_salario_region.png')  # Guardar gráfico
plt.close()

# Análisis de correlación (seleccionando solo columnas numéricas)
numerical_df = df.select_dtypes(include=[np.number])
correlation_matrix = numerical_df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap de la Correlación entre Variables')
plt.savefig('heatmap_correlacion.png')  # Guardar gráfico
plt.close()
