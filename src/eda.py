import pandas as pd
from db_conexion import establecer_conexion

# Establece la conexión a la base de datos
conn, cursor = establecer_conexion()

# Consulta SQL para seleccionar los datos
query = "SELECT * FROM candidates"

# Leer los datos en un DataFrame de pandas
df = pd.read_sql_query(query, conn)

# Definir las categorías de agrupación para las tecnologías
def agrupar_tecnologias(tech):
    development = ['Development - CMS Backend', 'Development - CMS Frontend', 
                    'Development - Backend', 'Development - Frontend', 'Development - FullStack',
                    'Game Development']
    system_network = ['System Administration', 'Security', 'DevOps', 'Database Administration', 'Security Compliance']
    business = ['Client Success', 'Sales', 'Business Analytics / Project Management', 
                'Business Intelligence', 'Salesforce']
    qa_testing = ['QA Manual', 'QA Automation']
    design_media = ['Design', 'Social Media Community Management', 'Adobe Experience Manager']
    
    if tech in development:
        return 'Development'
    elif tech in system_network:
        return 'System & Network'
    elif tech in business:
        return 'Business'
    elif tech in qa_testing:
        return 'QA & Testing'
    elif tech in design_media:
        return 'Design & Media'
    else:
        return 'Otros'

# Aplicar la agrupación a la columna 'Technology'
df['Technology_Group'] = df['technology'].apply(agrupar_tecnologias)

# Eliminar correos electrónicos duplicados dejando solo la primera ocurrencia
df_unique_emails = df.drop_duplicates(subset='email', keep='first')

# Guardar los datos limpios y agrupados en un nuevo archivo CSV
df_unique_emails.to_csv('C:\\Users\\USUARIO\\Documents\\Workshop_ETL1\\data\\candidates_cleaned.csv', index=False)