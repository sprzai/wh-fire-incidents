FROM postgres:latest

# Variables de entorno para la configuración de la base de datos
ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword

# Copia archivos SQL al contenedor
COPY create_tables.sql /docker-entrypoint-initdb.d/


