import psycopg2

def establecer_conexion():
    dbname='Workshop_ETL1'
    user='postgres'
    password='root'
    host='localhost'
    port='5432'

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print("Conexion exitosa a la base de datos")
    cursor = conn.cursor()

    return conn,cursor