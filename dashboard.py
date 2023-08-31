#pip install plotly

import psycopg2
import plotly.express as px

# Configuración de la conexión a la base de datos
db_config = {
    "dbname": "your_database",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

def create_bar_chart():
    try:
        # Establecer conexión a la base de datos
        conn = psycopg2.connect(**db_config)

        # Consulta para obtener los datos de incidentes por distrito
        query = """
            SELECT d.DistrictName, COUNT(*) AS IncidentCount
            FROM FactIncidents f
            JOIN DimDistrict d ON f.DistrictKey = d.DistrictKey
            GROUP BY d.DistrictName
            ORDER BY IncidentCount DESC;
        """

        # Obtener los datos de la base de datos
        data = []
        with conn.cursor() as cursor:
            cursor.execute(query)
            for row in cursor.fetchall():
                district_name, incident_count = row
                data.append({"DistrictName": district_name, "IncidentCount": incident_count})

        # Crear gráfico de barras
        fig = px.bar(data, x="DistrictName", y="IncidentCount", title="Incidentes por Distrito")

        # Mostrar el gráfico
        fig.show()

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_bar_chart()
