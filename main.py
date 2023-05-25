from file_downloader import FileDownloader
from data_analyzer import DataAnalyzer
from display import Display
from users_db import UsersTable
from contacts_db import ContactsTable
from database_finder import DatabaseFinder


def main():
    url = 'https://lk.globtelecom.ru/upload/test_prog1.csv'
    downloader = FileDownloader(url)  # Создаем объект класса FileDownloader и скачиваем файл
    data = downloader.read_file()  # Переносим данные из файла в переменную

    data_analyzer = DataAnalyzer(data)  # Создаем объект для обработки данных (выборка нужной информации, превращение в словарь, добавление возраста)
    data_analyzed = data_analyzer.get_processed_file()  # Выборка нужной информации, превращение в словарь, добавление возраста
    users_with_incorrect_phones = data_analyzer.get_users_with_incorrect_phones()  # Выбираем юзеров с некорректными номерами
    data_analyzer.separation_people_by_pay_method(users_with_incorrect_phones)  # Делим людей по способам оплаты и в зависимости от этого записываем их в соответствующий файл

    display = Display(data_analyzer)
    display.table_lastname_duplicates()  # Однофамильцы
    display.table_birth_year_count()  # Кто в какой год родился
    display.table_non_unique_phones()  # Повторяющиеся телефоны
    display.table_users_with_incorrect_phone_numbers(users_with_incorrect_phones)  # Некорректные номера

    users_db = UsersTable(data_analyzed)
    users_db.insert_to_table()

    contacts_db = ContactsTable(data_analyzed)
    contacts_db.insert_to_table()

    db_finder = DatabaseFinder(users_db, contacts_db)
    phone = '70001005627'
    db_finder.find_user_by_phone(phone)

    # data_users = db.filtering_data()
    #
    # for row in data_analyzed:
    #     print(row)


if __name__ == '__main__':
    main()

