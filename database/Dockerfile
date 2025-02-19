FROM postgres:13

ENV POSTGRES_DB iris
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password

COPY initialize_db.py /docker-entrypoint-initdb.d/
