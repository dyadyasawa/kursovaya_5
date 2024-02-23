
from classes.db_managaer import DBManager
from utils.utils import create_database, create_tables, add_data_to_tables

db = DBManager()

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

while True:
    print('  1 - вывести список всех компаний и количество открытых вакансий у каждой из них.')
    print('  2(интереснее) - вывести название компании, название вакансии(профессию), зарплату и ссылку на вакансию.')
    print('  3 - вывести среднюю зарплату по всем вакансиям.')
    print('  4 - вывести информацию о вакансиях, у которых зарплата выше средней(взятой по всем вакансиям)')
    print('  5 - вывести вакансии, в названии которых есть некое ключевое слово.')
    print('      (введи ключевое слово!, а если такового в названии вакансии не окажется -> пустая строка...)')
    print('  q - выход из программы.')

    answer = input()

    if answer == 'q':
        quit()
    elif answer == '1':
        db.get_companies_and_vacancies_count('new_database')
        quit()
    elif answer == '2':
        db.get_all_vacancies('new_database')
        quit()
    elif answer == '3':
        db.get_avg_salary('new_database')
        quit()
    elif answer == '4':
        db.get_vacancies_with_higher_salary('new_database')
        quit()
    elif answer == '5':
        keyword = input('Введи поисковое слово:  ')
        db.get_vacancies_with_keyword('new_database', keyword)
        quit()
    else:
        print('Наверное, ты, что-то ввел неправильно, попробуй еще раз, можно:')
