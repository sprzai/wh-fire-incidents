
# crear base de datos
docker build -t postgres-database -f Dockerfile .

docker run -d --name postgres-container -p 5432:5432 -v $(pwd)/postgres_data:/var/lib/postgresql/data postgres-database



# Para ejecutar la consulta que crea la tabla de Incidentes, sigue estos pasos:

# Conecta al contenedor con el cliente psql. Puedes ejecutar el siguiente comando desde tu terminal:
docker exec -it postgres-container psql -U user -d postgres-database

docker exec -it 86515083dbb3 psql -U myuser -d mydatabase -f /docker-entrypoint-initdb.d/create_tables.sql

docker exec -it 86515083dbb3 psql -U myuser -d mydatabase



