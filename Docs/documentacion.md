# Procurement Visualization Project Documentation


## 1. Introduction
This project aims to visualize data related to hiring in the technology sector. The main objective is to provide an interactive tool that allows analyzing hiring patterns based on various variables such as the technology used, the seniority of the candidates, the country of origin, among others.


## 2. Project Structure
The project is structured as follows:

- **src/**: Contains the main scripts for data extraction, cleaning, and visualization.
  - `extract.py`: Extracts data from the PostgreSQL database.
  - `visualizations.py`: Contains the functions to generate the visualizations.
  - `db_conexion.py`: Handles the connection to the PostgreSQL database.
  
- **data/**: Folder where the CSV exported from the database is stored (if necessary).
- **db/**: Contains the SQL script (`candidates.sql`) for creating the `candidates` table.
- **docs/**: Contains the project documentation.
- **.venv/**: Python virtual environment that contains the project dependencies.
- **notebooks/**: Contains the previous visualization tests in Jupyter.


## 3. Prerequisites
Before running the project, make sure you have the following installed:

-Python 3.11
- PostgreSQL
- Dependencies listed in `requirements.txt`


## 4. Installation
Follow the installation steps mentioned in the readme


## 5. Use
Data Extraction and Cleaning:
Run extract.py to extract and clean the data from the database.

Generation of Visualizations:
Run visualizations.py to generate the visualizations into graphs.

Visualization in Power BI:
Import the clean data into Power BI to generate additional visualizations.


## 6. Description of Visualizations
Hiring by Technology: Pie chart showing the distribution of hiring by technology.
Hires by Year: Bar graph showing the number of hires per year.
Hires by Seniority: Bar graph that illustrates the distribution of hires according to experience.
Hiring by Country: Multiline graph showing hiring by year in the US, Brazil, Colombia, and Ecuador.


## 7. Conclusion
This project provides a solid analysis along with a visualization of hiring data in the technology sector. It is a valuable tool for decision making with its ability to generate graphs and certain analyses.


## 8. License
MIT License

Copyright (c) 2024 [William Alejandro Botero Florez]