import csv
import psycopg2
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
csv_file = "Fire_Incidents.csv"  # Cambiar al nombre de tu archivo CSV

def insert_data(row, conn):
    try:
        # Crear un cursor
        cursor = conn.cursor()

        # Preparar la consulta de inserción
        insert_query = """
            INSERT INTO FactIncidents (
                IncidentNumber, ExposureNumber, ID, Address, IncidentDate,
                CallNumber, AlarmDtTm, ArrivalDtTm, CloseDtTm, City, Zipcode,
                BattalionKey, StationArea, Box, SuppressionUnits, SuppressionPersonnel,
                EMSUnits, EMSPersonnel, OtherUnits, OtherPersonnel, FirstUnitOnScene,
                EstimatedPropertyLoss, EstimatedContentsLoss, FireFatalities, FireInjuries,
                CivilianFatalities, CivilianInjuries, NumberOfAlarms, PrimarySituation,
                MutualAid, ActionTakenPrimary, ActionTakenSecondary, ActionTakenOther,
                DetectorAlertedOccupants, PropertyUse, AreaOfFireOrigin, IgnitionCause,
                IgnitionFactorPrimary, IgnitionFactorSecondary, HeatSource, ItemFirstIgnited,
                HumanFactorsAssociatedWithIgnition, StructureType, StructureStatus,
                FloorOfFireOrigin, FireSpread, NoFlameSpread, NumberOfFloorsWithMinimumDamage,
                NumberOfFloorsWithSignificantDamage, NumberOfFloorsWithHeavyDamage,
                NumberOfFloorsWithExtremeDamage, DetectorsPresent, DetectorType,
                DetectorOperation, DetectorEffectiveness, DetectorFailureReason,
                AutomaticExtinguishingSystemPresent, AutomaticExtinguishingSystemType,
                AutomaticExtinguishingSystemPerformance, AutomaticExtinguishingSystemFailureReason,
                NumberOfSprinklerHeadsOperating, SupervisorDistrict, NeighborhoodDistrict, Point
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Obtener los valores de cada campo del CSV
        values = (
            row["Incident Number"], row["Exposure Number"], row["ID"], row["Address"],
            datetime.strptime(row["Incident Date"], "%Y-%m-%d"), row["Call Number"],
            datetime.strptime(row["Alarm DtTm"], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(row["Arrival DtTm"], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(row["Close DtTm"], "%Y-%m-%d %H:%M:%S"),
            row["City"], row["zipcode"], row["Battalion"], row["Station Area"],
            row["Box"], int(row["Suppression Units"]), int(row["Suppression Personnel"]),
            int(row["EMS Units"]), int(row["EMS Personnel"]), int(row["Other Units"]),
            int(row["Other Personnel"]), row["First Unit On Scene"],
            float(row["Estimated Property Loss"]), float(row["Estimated Contents Loss"]),
            int(row["Fire Fatalities"]), int(row["Fire Injuries"]),
            int(row["Civilian Fatalities"]), int(row["Civilian Injuries"]),
            int(row["Number of Alarms"]), row["Primary Situation"], row["Mutual Aid"],
            row["Action Taken Primary"], row["Action Taken Secondary"],
            row["Action Taken Other"], row["Detector Alerted Occupants"],
            row["Property Use"], row["Area of Fire Origin"], row["Ignition Cause"],
            row["Ignition Factor Primary"], row["Ignition Factor Secondary"],
            row["Heat Source"], row["Item First Ignited"],
            row["Human Factors Associated with Ignition"], row["Structure Type"],
            row["Structure Status"], int(row["Floor of Fire Origin"]),
            row["Fire Spread"], row["No Flame Spead"],
            int(row["Number of floors with minimum damage"]),
            int(row["Number of floors with significant damage"]),
            int(row["Number of floors with heavy damage"]),
            int(row["Number of floors with extreme damage"]), row["Detectors Present"],
            row["Detector Type"], row["Detector Operation"],
            row["Detector Effectiveness"], row["Detector Failure Reason"],
            row["Automatic Extinguishing System Present"],
            row["Automatic Extinguishing Sytem Type"],
            row["Automatic Extinguishing Sytem Perfomance"],
            row["Automatic Extinguishing Sytem Failure Reason"],
            int(row["Number of Sprinkler Heads Operating"]),
            row["Supervisor District"], row["neighborhood_district"], row["point"]
        )

        cursor.execute(insert_query, values)

        # Confirmar la transacción
        conn.commit()

        print("Datos insertados exitosamente.")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        if conn:
            conn.close()

def main():
    try:
        # Establecer conexión a la base de datos
        conn = psycopg2.connect(**db_config)

        # Abrir archivo CSV y realizar inserciones
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                insert_data(row, conn)

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
