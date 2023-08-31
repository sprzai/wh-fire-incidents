import pandas as pd
import plotly.express as px

def create_daily_incidents_dashboard():
    try:
        # Nombre del archivo CSV
        csv_file = "Fire_Incidents.csv"  # Cambiar al nombre de tu archivo CSV

        # Leer datos del archivo CSV
        df = pd.read_csv(csv_file)

        # Convertir la columna 'Incident Date' a tipo datetime
        df['Incident Date'] = pd.to_datetime(df['Incident Date'])

        # Agrupar los datos por fecha y contar los incidentes diarios
        daily_incidents = df.groupby('Incident Date').size().reset_index(name='Incident Count')

        # Crear gráfico de líneas para mostrar incidentes diarios
        fig = px.line(daily_incidents, x='Incident Date', y='Incident Count', title='Incidentes Diarios')
        fig.update_xaxes(title_text='Fecha')
        fig.update_yaxes(title_text='Cantidad de Incidentes')

        # Mostrar el gráfico
        fig.show()

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    create_daily_incidents_dashboard()
