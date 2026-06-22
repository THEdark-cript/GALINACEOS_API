from flask import g
import psycopg2

from helpers.application import app
from helpers.enviroment import environment

DATABASE_NAME = environment.get("DB_NAME")
DATABASE_USER = environment.get("DB_USER")
DATABASE_PASSWORD = environment.get("DB_PASSWORD")
DATABASE_PORT = environment.get("DB_PORT")
DATABASE_HOST = environment.get("DB_HOST")


def get_conn():
    conn = getattr(g, "_database", None)
    if conn is None:
        print("Tentando conectar em:",
              DATABASE_NAME,
              DATABASE_USER,
              DATABASE_HOST,
              DATABASE_PORT)
        conn = g._database = psycopg2.connect(
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT
        )
    return conn


@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, "_database", None)
    if conn is not None:
        conn.close()
