import pandas as pd
import matplotlib.pyplot as plt

# Configura la conexión a PostgreSQL
from db_conexion import establecer_conexion

conn, cursor = establecer_conexion()

def cargar_datos():
    query = "SELECT * FROM candidates"  
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def graficar_contrataciones_por_tecnologia(df):
    plt.figure(figsize=(10, 7))
    df['technology'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Contrataciones por Tecnología')
    plt.ylabel('')
    plt.show()


def graficar_contrataciones_por_año(df):
    df['application_date'] = pd.to_datetime(df['application_date'])
    df['year'] = df['application_date'].dt.year
    plt.figure(figsize=(10, 7))
    df['year'].value_counts().sort_index().plot(kind='barh')
    plt.title('Contrataciones por Año')
    plt.xlabel('Número de Contrataciones')
    plt.ylabel('Año')
    plt.show()
    
    
def graficar_contrataciones_por_antiguedad(df):
    plt.figure(figsize=(10, 7))
    df['seniority'].value_counts().plot(kind='bar')
    plt.title('Contrataciones por Antigüedad')
    plt.xlabel('Antigüedad')
    plt.ylabel('Número de Contrataciones')
    plt.show()


def graficar_contrataciones_por_pais(df):
    plt.figure(figsize=(10, 7))
    df['country'].value_counts().head(10).plot(kind='line')
    plt.title('Contrataciones por País')
    plt.xlabel('País')
    plt.ylabel('Cantidad')
    plt.show()
    

# Ejecución de las visualizaciones
df = cargar_datos()
graficar_contrataciones_por_tecnologia(df)
graficar_contrataciones_por_año(df)
graficar_contrataciones_por_antiguedad(df)
graficar_contrataciones_por_pais(df)
