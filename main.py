
from classes.hh_api import HeadHunterApi
from utils.utils import create_database, create_tables, add_data_to_tables
from pprint import pprint

print()
print('Приветствую, тебя, ув.Пользователь!')
print('Сегодня мы с тобой создадим базу данных и заполним ее информацией, полученной с сайта hh.ru.')
print('Мы выберем 10 случайных компаний и по 20 вакансий для каждой из них(итого 200 вакансий!),')
print('а также сможем разнообразно обработать и вывести полученные данные.')
print('Ну, что, готов?... Тогда жми букву ENTER и поехали... ')
input()
print()

create_database('new_database')
create_tables('new_database')
add_data_to_tables('new_database')

print('... ... ну ... и, ... вот база данных и создана! ')
print()
print('Теперь, можно, немного поработать с полученными данными.')
print('Возможны следующие варианты:')
print('  1 - вывести список всех компаний и количество открытых вакансий у каждой из них.')
print('  2(уже интереснее) - вывести название компании, название вакансии(профессию), зарплату и ссылку на вакансию.')
print('  3 - вывести среднюю зарплату по всем вакансиям.')
print('  4 - вывести информацию о вакансиях, у которых зарплата выше средней(взятой по всем вакансиям)')
print('  5 - вывести вакансии, в названии которых есть некое ключевое слово.')
print('      (нужно будет ввести ключевое слово!, а если такового в названии вакансии не окажется -> пустая строка...)')
print('  q - выход из программы.')

# answer = input()



# hh = HeadHunterApi()
#
# pprint(hh.choise_data_for_vacancies())