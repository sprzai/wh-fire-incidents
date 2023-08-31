import csv
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Configuración de la conexión a la base de datos
db_config = {
    "dbname": "mydatabase",
    "user": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "port": "5432"
}

# Archivo CSV
csv_file = "Fire_Incidents.csv"  
def insert_into_dimtime(conn, incident_date):
    with conn.cursor() as cursor:
        insert_query = sql.SQL("INSERT INTO DimTime (IncidentDate) VALUES (%s);")
        cursor.execute(insert_query, [incident_date])
    conn.commit()

def insert_into_dimdistrict(conn, district_name):
    with conn.cursor() as cursor:
        insert_query = sql.SQL("INSERT INTO DimDistrict (DistrictName) VALUES (%s);")
        cursor.execute(insert_query, [district_name])
    conn.commit()

def insert_into_dimbattalion(conn, battalion_name):
    with conn.cursor() as cursor:
        insert_query = sql.SQL("INSERT INTO DimBattalion (BattalionName) VALUES (%s);")
        cursor.execute(insert_query, [battalion_name])
    conn.commit()

def main():
    try:
        # Establecer conexión a la base de datos
        conn = psycopg2.connect(**db_config)

        # Abrir archivo CSV y realizar inserciones
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                incident_date = datetime.strptime(row["Incident Date"], "%Y-%m-%d")
                district_name = row["neighborhood_district"]
                battalion_name = row["Battalion"]

                insert_into_dimtime(conn, incident_date)
                insert_into_dimdistrict(conn, district_name)
                insert_into_dimbattalion(conn, battalion_name)

        print("Inserciones realizadas exitosamente.")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
