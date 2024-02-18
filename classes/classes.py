
import requests
import random

class HeadHunterApi:
    """ Класс для работы с данными через API сайта hh.ru. """

    def get_employers_info(self) -> list:
        """ Метод для подключения к API и получения информации о работодателях с hh.ru.
            Из 30 работодателей, отсортированных по убыванию количества открытых вакансий
            случайным образом отбираются 10."""

        url = 'http://api.hh.ru/employers'
        params = {'per_page': 30, 'area': 113, 'sort_by': 'by_vacancies_open'}

        list_employers = requests.get(url, params=params).json()['items']

        return random.sample(list_employers, 10)

    def choise_data_for_employers(self) -> list:
        """ Метод для выборки из полученных данных о работодателях. """

        data = self.get_employers_info()
        data_list = []
        for item in data:
            data_list.append({'employer_id': item['id'],
                              'employer_name': item['name'],
                              'vacancies': item['open_vacancies']})
        return data_list

    def get_vacancies_info(self, id: str) -> list:
        """ Метод для получения информации о вакансиях по id работодателя с hh.ru.
            Будут взяты только первые 20 вакансий."""

        url = 'http://api.hh.ru/vacancies'
        params = {'page': 0, 'per_page': 20, 'employer_id': id}

        list_vacancies = requests.get(url, params=params).json()['items']
        return list_vacancies

    def choise_data_for_vacancies(self) -> list:
        """ Метод для выборки данных из вакансии. """

        data = self.choise_data_for_employers()
        data_list = []
        for item in data:
            vacancies = self.get_vacancies_info(item['employer_id'])

            for item in vacancies:
                if not item['salary']:
                    salary_from = 0
                    salary_to = 0
                else:
                    salary_from = item['salary']['from'] if item['salary']['from'] else 0
                    salary_to = item['salary']['to'] if item['salary']['to'] else 0

                data_list.append({'employer_id': item['employer']['id'],
                                  'employer_name': item['employer']['name'],
                                  'area': item['area']['name'],
                                  'url': item['alternate_url'],
                                  'salary_from': salary_from,
                                  'salary_to': salary_to})
        return data_list
