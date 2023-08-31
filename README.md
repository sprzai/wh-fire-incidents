# Warehouse para Datos de Incidentes - Solución 

Este documento describe la solución propuesta para crear un warehouse
que refleje el estado actual de los datos de incidentes provenientes
de https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric, con actualizaciones diarias. 
Además, se proporciona
información sobre cómo el equipo de Business Intelligence puede
ejecutar consultas que agreguen incidentes a lo largo de las
dimensiones de período de tiempo, distrito y batallón. También se
incluye un informe de ejemplo que ilustra cómo utilizar el modelo.

## Solución Propuesta

La solución implica la creación de un warehouse basado en una base de
datos relacional, PostgreSQL, que almacene los datos de
incidentes provenientes de la fuente. La base de datos se actualizará
diariamente mediante un proceso de ETL
automatizado que traerá los nuevos datos de la fuente y los
incorporará al warehouse. Se asume que los datos de incidentes
incluyen información sobre período de tiempo, distrito y batallón.

Las tablas principales en el warehouse incluirán:

1. **Tabla de Incidentes:** Almacena los detalles de cada incidente,
incluyendo fecha y hora, distrito, batallón y otros campos relevantes.

2. **Tabla de Dimensiones:** Contiene información sobre distritos y
batallones, lo que permite la agregación y análisis en esas
dimensiones.

## Proceso de Pensamiento

1. **Diseño del Warehouse:** Definir la estructura de las tablas en la
base de datos, incluyendo las relaciones entre las tablas de
incidentes y dimensiones.

2. **ETL Automatizado:** Configurar un proceso de ETL automatizado
que, a diario, extraiga los nuevos datos de la fuente, realice las
transformaciones necesarias para adaptarlos al esquema del warehouse y
luego los cargue en las tablas correspondientes.

3. **Consultas de Business Intelligence:** El equipo de BI podrá
ejecutar consultas SQL en el warehouse para realizar análisis.
Ejemplos de consultas pueden incluir:
   - Agregar incidentes por período de tiempo (día, semana, mes).
   - Agregar incidentes por distrito y batallón.
   - Obtener tendencias de incidentes a lo largo del tiempo.

## Instrucciones de Uso

1. **Configuración Inicial:**
   - Instale una base de datos relacional, PostgreSQL.
   - Cree las tablas según el diseño propuesto.

2. **Ejecución de Consultas:**
   - El equipo de BI puede ejecutar consultas SQL en la base de datos
para obtener información agregada.



