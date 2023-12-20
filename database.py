from dotenv import load_dotenv
from os import environ, getcwd, path
import sys

from psycopg2 import connect


extend_data_directory = getcwd()

if getattr(sys, 'frozen', False):
    extend_data_directory = sys._MEIPASS

load_dotenv(dotenv_path=path.join(extend_data_directory, '.env'))
connection = connect(environ.get('DATABASE_URL'), sslmode='require')
c = connection.cursor()


def close():
    c.close()
    connection.close()


def update(*args):
    c.execute(*args)
    connection.commit()
    return c


def query(*args):
    c.execute(*args)
    return c


def create_tables():
    # TODO: Create more tables. :D

    statements = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY UNIQUE NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
        """,
    )
    upsert_statements = (

    )

    print("Creating tables...")
    for statement in statements:
        update(statement)
    for statement in upsert_statements:
        update(statement)
    print("Tables created. :D")

