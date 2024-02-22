
import psycopg2
from config import config
from classes.classes import HeadHunterApi


def create_database(name_db):
    """ Функция для создания базы данных. """

    conn = psycopg2.connect(database='postgres', **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {name_db}')
    cur.execute(f'CREATE DATABASE {name_db}')

    cur.close()
    conn.close()

def create_tables(name_db):
    """ Функция для создания таблиц в базе данных. """

    conn = psycopg2.connect(database=name_db, **config())
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE employers
                    (
                    employer_id  int PRIMARY KEY,
                    employer_name varchar(255) UNIQUE NOT NULL,
                    open_vacancies int
                    )
                    """)

    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE vacancies
                    (
                    vacancy_id int PRIMARY KEY,
                    employer_id int REFERENCES employers(employer_id),
                    vacancy_name varchar(255),
                    area varchar(255),
                    salary_from int,
                    salary_to int,
                    url varchar(255)
                    )
                    """)
    cur.close()
    conn.close()

def add_data_to_tables(name_db):
    """ Функция добавляет информацию в таблицы базы данных. """

    hh = HeadHunterApi()
    data = hh.choise_data_for_vacancies()
    employers = data[0]
    vacancies = data[1]

    conn = psycopg2.connect(database=name_db, **config())
    conn.autocommit = True
    cur = conn.cursor()

    for employer in employers:
        cur.execute("""
                    INSERT INTO employers (employer_id, employer_name, open_vacancies) 
                    VALUES (%s, %s, %s)
                    """,
                    (employer['employer_id'],
                    employer['employer_name'],
                    employer['vacancies']))

    for vacancy in vacancies:
        cur.execute("""
                    INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, area, salary_from, salary_to, url)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (vacancy['vacancy_id'],
                    vacancy['employer_id'],
                    vacancy['vacancy_name'],
                    vacancy['area'],
                    vacancy['salary_from'],
                    vacancy['salary_to'],
                    vacancy['url']))

    cur.close()
    conn.close()

create_database('new_database')
create_tables('new_database')
add_data_to_tables('new_database')
