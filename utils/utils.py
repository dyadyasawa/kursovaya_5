
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


def create_tables(name_db):
    """ Функция для создания таблиц в базе данных. """

    conn = psycopg2.connect(dbname=name_db, **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('CREATE TABLE employers'
                '('
                'employer_id  int PRIMARY KEY,'
                'employer_name varchar(255) UNIQUE NOT NULL,'
                'open_vacancies int'
                ')')

    cur.execute('CREATE TABLE vacancies'
                '('
                'employer_id int PRIMARY KEY,'
                'employer_name varchar(255) UNIQUE NOT NULL,'
                'area varchar(255),'
                'salary_from int,'
                'salary_to int,'
                'url varchar(255)'
                ')')
                # 'employer int REFERENCES employers(employer_id) NOT NULL,'


    cur.close()
    conn.close()


create_database('new_database')
create_tables('new_database')