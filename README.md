# Workshop ETL Project

## Descripción

Este proyecto consiste en un proceso ETL donde migramos datos, en este caso un dataset de candidatos desde un archivo CSV a una base de datos como lo es PostgreSQL,como ya el csv estaba limpio se tuvo encuenta la limpieza, se enfoco en las visualizaciones utilizando Python.

## Instalacion

Clona este repositorio:

```bash
git clone https://github.com/willyoung21/Project_candidates.git
cd Workshop_ETL1

# crea y activa el entorno virtual
python -m venv .venv
.venv\Scripts\activate


#instala las dependencia
pip install -r requirements.txt

```

## Configuración de la base de datos

1. Crear una base de datos PostgreSQL.
2. Ejecutar el script `candidates.sql` que se encuentra en la carpeta `DB` para crear la tabla `candidates`.
3. Importar el dataset que esta en la carpeta data `candidates.csv`
4. Configurar el archivo `db_conexion.py` con las credenciales de tu base de datos.

Ya configurada ejecuta el script para hacer la conexion

```bash
python src/db_conexion.py
```

## USO

Ejecuta el script de extracción de datos:

```bash
python src/extract.py
#Esto generará un archivo candidates.csv en la carpeta data.

#Para generar las visualizaciones
python src/visualizaciones.py

```

## Visualizaciones
Las visualizaciones generadas incluyen:

Contrataciones por Tecnología (Gráfico Circular)
Contrataciones por Año (Gráfico de Barras Horizontales)
Contrataciones por Antigüedad (Gráfico de Barras)
Contrataciones por País durante los años (Gráfico Multilínea)



