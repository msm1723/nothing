# pulling the postgres image
FROM postgres:14-alpine

# initiate db using postgress docker entripoint
ADD ./create.sql /docker-entrypoint-initdb.d
