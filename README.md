# ETL Project Workshop

## Description

This project consists of an ETL process where we migrate data, in this case a candidate dataset from a CSV file to a database such as PostgreSQL, since the csv was already clean, the cleaning was taken into account, focusing on the visualizations using Python.

##Facility

Clone this repository:

```bash
git clone https://github.com/willyoung21/Project_candidates.git
cd Workshop_ETL1

# create and activate the virtual environment
python -m venv .venv
.venv\Scripts\activate


#install dependencies
installing pip -r requirements.txt

```

## Database configuration

1. Create a PostgreSQL database.
2. Run the `candidates.sql` script found in the `DB` folder to create the `candidates` table.
3. Import the data set that is in the data `candidates.csv` folder
4. Configure the `db_conexion.py` file with your database credentials.

Once configured, run the script to make the connection

```bash
python src/db_connection.py
```

## USO

Run the data extraction script:

```bash
python src/extract.py
#This will generate a candidates.csv file in the data folder.

#To generate the visualizations
python src/visualizations.py

```

## Views
Visualizations generated include:

Hiring by Technology (Graphic Circular)
Hires by Year (Horizontal Bar Chart)
Hiring by Seniority (Bar Chart)
Hiring by Country over the years (Multiline Chart)