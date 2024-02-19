
import psycopg2
from config import config
from classes.classes import HeadHunterApi


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
                'url varchar(255),'
                'employer int'
                ');'
                'ALTER TABLE vacancies ADD CONSTRAINT fk_vacancies_employers FOREIGN KEY(employer_id) REFERENCES employers(employer_id);')


    cur.close()
    conn.close()

def add_data_to_tables(name_db):
    """ Функция добавляет информацию в таблицы базы данных. """

    hh = HeadHunterApi()
    employers = hh.choise_data_for_vacancies()[0]
    vacancies = hh.choise_data_for_vacancies()[1]

    conn = psycopg2.connect(dbname=name_db, **config())
    conn.autocommit = True
    cur = conn.cursor()

    for employer in employers:
        cur.execute('INSERT INTO employers VALUES(%s, %s, %s),'
                   f'{employer['employer_id']},'
                   f'{employer['employer_name']},'
                   f'{employer['vacancies']}')

    for vacancy in vacancies:
        cur.execute('INSERT INTO vacancies VALUES(%s, %s, %s, %s, %s, %s),'
                    f'{vacancy['employer_id']},'
                    f'{vacancy['employer_name']},'
                    f'{vacancy['area']},'
                    f'{vacancy['salary_from']},'
                    f'{vacancy['salary_to']},'
                    f'{vacancy['url']},'
                    f'{vacancy['employer']}')

    cur.close()
    conn.close()


create_database('new_database')
create_tables('new_database')
add_data_to_tables('new_database')