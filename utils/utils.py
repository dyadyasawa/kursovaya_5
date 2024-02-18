
import psycopg2
from config import config


def create_database(name_db):
    """ Функция для создания базы данных. """

    conn = psycopg2.connect(dbname='postgres', **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {name_db}')
    cur.execute(f'CREATE DATABASE {name_db}')

    cur.close()
    conn.close()


create_database('my_new_DB')
