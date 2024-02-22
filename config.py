
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """ Функция для получения параметров подключения к базе данных из database.ini"""

    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in {1} file'.format(section, filename))
    return db
