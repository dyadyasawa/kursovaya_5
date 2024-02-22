
import psycopg2
from config import config
class DBManager:
    """ Класс для подключения к БД Postgresql и работе с ее данными. """

    def get_companies_and_vacancies_count(self, name_db):
        """ Метод получает список всех компаний и количество вакансий у каждой компании. """

        conn = psycopg2.connect(database=name_db, **config())
        cur = conn.cursor()
        cur.execute("""
                    SELECT employer_name, open_vacancies FROM employers
                    """)

        for row in cur.fetchall():
            print(f'Компания: {row[0]}, открытых вакансий: {row[1]}')

        cur.close()
        conn.close()

    def get_all_vacancies(self, name_db):
        """ Метод получает список всех вакансий с указанием названия компании,
            названия вакансии и зарплаты и ссылки на вакансию. """

        conn = psycopg2.connect(database=name_db, **config())
        cur = conn.cursor()
        cur.execute("""
                    SELECT employers.employer_name, vacancy_name, salary_from, salary_to, url 
                    FROM vacancies JOIN employers USING(employer_id)
                    """)

        for row in cur.fetchall():
            print(f'Компания: {row[0]}, вакансия: {row[1]}, зарплата от: {row[2]} до: {row[3]}, url: {row[4]} ')

        cur.close()
        conn.close()

    def get_avg_salary(self, name_db):
        """ Метод получает среднюю зарплату по вакансиям(используем колонку salary_from). """

        conn = psycopg2.connect(database=name_db, **config())
        cur = conn.cursor()
        cur.execute("""
                    SELECT AVG(salary_from) FROM vacancies
                    """)

        for row in cur.fetchall():
            print(f'Средняя зарплата по вакансиям: {round(row[0], 2)}')

        cur.close()
        conn.close()

    def get_vacancies_with_higher_salary(self, name_db):
        """ Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
            (используем колонку salary_from). """

        conn = psycopg2.connect(database=name_db, **config())
        cur = conn.cursor()
        cur.execute("""
                    SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
                    """)

        for row in cur.fetchall():
            print(f'Id вакансии: {row[0]}, id работодателя: {row[1]}, профессия: {row[2]}, место работы: {row[3]}, '
                  f'зарплата от: {row[4]}, до: {row[5]}, url: {row[6]}')

        cur.close()
        conn.close()

    def get_vacancies_with_keyword(self, name_db, keyword):
        """ Метод получает список всех вакансий,
            в названии которых содержатся переданные в метод слова, например python. """

        conn = psycopg2.connect(database=name_db, **config())
        cur = conn.cursor()
        cur.execute(
                    f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{keyword.title()}%'"
                    )

        for row in cur.fetchall():
            print(f'Id вакансии: {row[0]}, id работодателя: {row[1]}, профессия: {row[2]}, место работы: {row[3]}, '
                  f'зарплата от: {row[4]}, до: {row[5]}, url: {row[6]}')

        cur.close()
        conn.close()


db = DBManager()
db.get_vacancies_with_keyword('new_database', 'летчик')