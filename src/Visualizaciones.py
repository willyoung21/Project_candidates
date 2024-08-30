import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar los datos limpios desde el script de limpieza
from eda import df_unique_emails  # Asegúrate de que df_unique_emails sea el DataFrame limpio

def cargar_datos_limpios():
    # Aquí cargamos el DataFrame ya limpio y agrupado
    df = df_unique_emails.copy()
    
    # Agrupar tecnologías en categorías generales
    technology_groups = {
        'Development': ['Data Engineer', 'Development - CMS Backend', 'Game Development', 'Development - CMS Frontend', 
                        'Development - Backend', 'Development - Frontend', 'Development - FullStack'],
        'System and Network': ['System Administration', 'Security', 'Security Compliance', 'Database Administration'],
        'Business': ['Client Success', 'Sales', 'Business Analytics / Project Management', 'Business Intelligence'],
        'Quality Assurance': ['QA Manual', 'QA Automation'],
        'Creative': ['Design', 'Social Media Community Management', 'Adobe Experience Manager'],
        'Others': ['Mulesoft', 'DevOps', 'Salesforce', 'Technical Writing']
    }

    # Crear una nueva columna de grupo de tecnología basada en las categorías
    def categorize_technology(technology):
        for group, techs in technology_groups.items():
            if technology in techs:
                return group
        return 'Others'

    df['technology_group'] = df['technology'].apply(categorize_technology)
    return df

# 1. Gráfico Circular de Contrataciones por Tecnología Agrupada
def graficar_contrataciones_por_tecnologia(df):
    plt.figure(figsize=(10, 7))
    df['technology_group'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Contrataciones por Tecnología Agrupada')
    plt.ylabel('')  # Para evitar que el título del eje Y interfiera
    plt.show()

# 2. Gráfico de Barras de Contrataciones por Año
def graficar_contrataciones_por_anio(df):
    df['application_date'] = pd.to_datetime(df['application_date'])
    df['year'] = df['application_date'].dt.year
    plt.figure(figsize=(10, 7))
    df['year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title('Contrataciones por Año')
    plt.xlabel('Año')
    plt.ylabel('Número de Contrataciones')
    plt.show()

# 3. Gráfico de Barras de Contrataciones por Antigüedad
def graficar_contrataciones_por_antiguedad(df):
    plt.figure(figsize=(10, 7))
    df['seniority'].value_counts().plot(kind='bar', color='orange')
    plt.title('Contrataciones por Antigüedad')
    plt.xlabel('Antigüedad')
    plt.ylabel('Número de Contrataciones')
    plt.show()

# 4. Gráfico de Líneas de Contrataciones por País Durante Años
def graficar_contrataciones_por_pais(df, countries):
    # Asegurarse de que 'application_date' sea datetime
    df['application_date'] = pd.to_datetime(df['application_date'])
    # Extraer el año de la fecha
    df['year'] = df['application_date'].dt.year
    
    # Filtrar por países específicos
    df_filtered = df[df['country'].isin(countries)]
    
    # Crear gráfico multilínea
    plt.figure(figsize=(14, 8))
    for country in countries:
        country_df = df_filtered[df_filtered['country'] == country]
        # Contar contrataciones por año para cada país
        annual_counts = country_df.groupby('year').size()
        # Graficar
        plt.plot(annual_counts.index, annual_counts.values, marker='o', label=country)
    
    plt.title('Contrataciones por País Durante Años')
    plt.xlabel('Año')
    plt.ylabel('Número de Contrataciones')
    plt.legend(title='País')
    plt.grid(True)
    plt.show()
countries = ['United States', 'Brazil', 'Colombia', 'Ecuador']


# Cargar los datos limpios y ejecutar las visualizaciones
df = cargar_datos_limpios()

graficar_contrataciones_por_tecnologia(df)
graficar_contrataciones_por_anio(df)
graficar_contrataciones_por_antiguedad(df)
graficar_contrataciones_por_pais(df, countries)
