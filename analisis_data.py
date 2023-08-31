import pandas as pd

# Cargar el archivo CSV
csv_file = "Fire_Incidents.csv"  # Cambia esto a la ruta real del archivo CSV
data = pd.read_csv(csv_file)

# Seleccionar los campos relevantes para la tabla de incidentes
columns = [
    "Incident Number", "Incident Date", "Battalion", "Address",
    "City", "zipcode", "Primary Situation", "Action Taken Primary",
    "Estimated Property Loss", "Estimated Contents Loss",
    "Fire Fatalities", "Fire Injuries", "Civilian Fatalities",
    "Civilian Injuries"
]

# Crear un DataFrame con los campos seleccionados
incident_df = data[columns]

# Mostrar el análisis simple de la tabla de incidentes
print("Total de incidentes:", len(incident_df))
print("Fecha más antigua:", incident_df["Incident Date"].min())
print("Fecha más reciente:", incident_df["Incident Date"].max())
print("Promedio de propiedad perdida estimada:", incident_df["Estimated Property Loss"].mean())
print("Promedio de contenido perdido estimado:", incident_df["Estimated Contents Loss"].mean())


'''  Salida
Total de incidentes: 637003
Fecha más antigua: 2003-01-01T00:00:00
Fecha más reciente: 2023-08-25T00:00:00
Promedio de propiedad perdida estimada: 7598.359019172097
Promedio de contenido perdido estimado: 2482.749009741307

'''

# incident_df.to_csv("tabla_incidentes.csv", index=False)
