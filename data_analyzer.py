from datetime import datetime, date
from file_analyzer import FileAnalyzer
from file_saver import FileSaver
import re


DELIMITER_LINE = '\n'


class DataAnalyzer:
    def __init__(self, analyzed_data):
        self.analyzed_data = analyzed_data
        self.processed_data = []

    @staticmethod
    def get_normalized_phone(verifiable_phone: str) -> str:
        """
            Нормализует номер телефона путем удаления всех нецифровых символов.
        :param verifiable_phone: (str) Номер телефона для нормализации.
        :return: (str) Нормализованный номер телефона без нецифровых символов.
        """

        not_a_number = r'\D+'
        normalized_number = re.sub(not_a_number, '', verifiable_phone)

        return normalized_number

    @staticmethod
    def get_elem_for_dict_by_key(dict_for_copy: dict, keys_for_copy: list):
        """
            Возвращает новый словарь, содержащий элементы из исходного словаря, соответствующие указанным ключам.
        :param dict_for_copy: (dict) Исходный словарь, из которого будут копироваться элементы.
        :param keys_for_copy: (list) Список ключей, для которых нужно скопировать элементы из исходного словаря.
        :return: (dict) Новый словарь, содержащий элементы из исходного словаря, соответствующие указанным ключам.
        """

        new_dictionary = {key: value for key, value in dict_for_copy.items() if key in keys_for_copy}

        return new_dictionary

    @staticmethod
    def get_age_by_year(birth_date: str) -> int:
        """
        Рассчитывает возраст на основе даты рождения.
        :param birth_date: (str) Дата рождения в формате 'дд.мм.гггг'
        :return: age: (str) Возраст в годах, рассчитанный на основе даты рождения.
        """

        today = date.today()
        birth_date_obj = datetime.strptime(birth_date, '%d.%m.%Y').date()
        age = today.year - birth_date_obj.year - ((today.month, today.day) < (birth_date_obj.month, birth_date_obj.day))

        return age

    @staticmethod
    def get_last_names_from_full_names(data_for_processing: list) -> list:
        """
            Функция возвращает список фамилий на основе списка ФИО
        :param data_for_processing: (list) список словарей с данными, каждый словарь содержит ключ 'ФИО', со значением - полным именем.
        :return: (list) список фамилий из переданного списка.
        """

        last_names = []
        full_name_key = 'ФИО'

        for line in range(len(data_for_processing)):
            full_name = data_for_processing[line][full_name_key]
            last_name = full_name.split()[0]
            last_names.append(last_name)

        return last_names

    @staticmethod
    def get_elem_from_list_of_dict_by_key(data_for_processing: list, key_for_copy: str) -> list:
        """
            Извлекает значения из списка словарей по указанному ключу и возвращает список этих значений.
        :param data_for_processing: (list) Список словарей, из которых нужно извлечь значения.
        :param key_for_copy: (str) Ключ, по которому нужно извлечь значения.
        :return: (list) Список значений, извлеченных из списка словарей по указанному ключу.
        """

        ready_list = [item[key_for_copy] for item in data_for_processing]

        return ready_list

    @staticmethod
    def get_year_from_date(data_for_get: list) -> list:
        """
            Извлекает годы из списка дат и возвращает список этих годов.
        :param data_for_get: (list) Список дат, из которых нужно извлечь годы.
        :return: (list) Список годов, извлеченных из списка дат по указанному ключу.
        """

        years_of_birth = [datetime.strptime(data, '%d.%m.%Y').year for data in data_for_get]

        return years_of_birth

    def get_processed_file(self) -> list:
        """
            Возвращает список словарей, в который попадают выбранные элементы, им присваиваются ключи, а также добавляется информация о возрасте.
        :return: (list) список словарей с выбранными элементами, возрастом и подписаными в формате int номерами строк
        """

        indexes_copied_elem = [0, 3, 4, 7, 8]
        keys_of_created_dict = ['Телефон', 'ИО', 'ФИО', 'Метод оплаты', 'День рождения']

        lines = self.analyzed_data.strip().split(DELIMITER_LINE)
        delimiter = FileAnalyzer.delimiter_identify(lines)

        fio_key = 'ИО'
        date_birth_key = 'День рождения'
        age_key = 'Возраст'
        line_number_key = 'Номер строки'
        gender_key = 'Пол'
        user_id_key = 'user_id'
        user_id = 1

        for line in range(len(lines)):
            new_line = []
            elem_data = lines[line].split(delimiter)
            for index_elem_data, elem_data in enumerate(elem_data):
                if index_elem_data in indexes_copied_elem:
                    new_line.append(elem_data)
                dictionary = dict(zip(keys_of_created_dict, new_line))
            dictionary[age_key] = DataAnalyzer.get_age_by_year(dictionary[date_birth_key])
            dictionary[line_number_key] = line
            dictionary[gender_key] = DataAnalyzer.get_gender(dictionary[fio_key])
            dictionary[user_id_key] = user_id
            self.processed_data.append(dictionary)
            user_id += 1

        return self.processed_data

    def get_users_with_incorrect_phones(self) -> list:
        """
        Возвращает список пользователей с неправильными телефонами.
        :return: (list) Список словарей пользователей с неправильными телефонами. Каждый словарь содержит скопированные ключи и нормализованный телефон.
        """

        keys_for_copy = ['Номер строки', 'ИО']

        pattern_not_a_number = r'\D+'
        number_digits = 11
        phone_key = 'Телефон'
        users_with_incorrect_phones = []

        for line in range(len(self.processed_data)):
            phone = self.processed_data[line][phone_key]
            phone_length = len(self.processed_data[line][phone_key])

            if re.search(pattern_not_a_number, phone) or phone_length != number_digits:
                user_with_incorrect_phone = {}
                for elem in keys_for_copy:
                    user_with_incorrect_phone[elem] = self.processed_data[line][elem]
                user_with_incorrect_phone[phone_key] = DataAnalyzer.get_normalized_phone(phone)
                users_with_incorrect_phones.append(user_with_incorrect_phone)

        return users_with_incorrect_phones

    def separation_people_by_pay_method(self, users_with_incorrect_phones: list):
        """
            Разделяет людей по способу оплаты и сохраняет результаты в различные файлы. В ходе работы:
            1. Отбрасывает людей с некорректно записаными номерами
            2. Выбирает какие элементы словаря копировать в итоговые файлы на основе key_for_copy_to_file

        :param users_with_incorrect_phones: (list) Список пользователей с некорректными номерами телефонов.
        :return: None
        """
        key_for_copy_to_file = ['ФИО', 'Телефон', 'День рождения', 'Возраст']

        pay_method_key = 'Метод оплаты'
        number_line_key = 'Номер строки'
        pos = []
        cash = []
        other_pay_method = []

        # создаем список номеров строк юзеров с корявыми номерами
        line_numbers_with_incorrect_phones = DataAnalyzer.get_elem_from_list_of_dict_by_key(users_with_incorrect_phones,
                                                                                            number_line_key)

        # фильтруем исходные данные по способу оплаты с отбрасыванием тех юзеров, у кого корявые номера и ненужных столбиков
        for line in range(len(self.processed_data)):
            if line not in line_numbers_with_incorrect_phones:
                if self.processed_data[line][pay_method_key] == 'pos':
                    pos.append(DataAnalyzer.get_elem_for_dict_by_key(self.processed_data[line], key_for_copy_to_file))
                elif self.processed_data[line][pay_method_key] == 'cash':
                    cash.append(DataAnalyzer.get_elem_for_dict_by_key(self.processed_data[line], key_for_copy_to_file))
                else:
                    other_pay_method.append(DataAnalyzer.get_elem_for_dict_by_key(self.processed_data[line], key_for_copy_to_file))

        # сохраняем файлы
        FileSaver.save_file(pos, 'pos_h.csv')
        FileSaver.save_file(cash, 'cash_h.csv')
        FileSaver.save_file(other_pay_method, 'other_h.csv')

    def get_count_of_duplicate_surnames(self) -> int:
        """
            Извлекает фамилии из исходных данных и определяет количество повторяющихся фамилий.
        Фамилии считаются повторяющимися, если они встречаются более одного раза.
        Возвращается общее количество повторяющихся фамилий.
        :return: (int) Количество повторяющихся фамилий.
        """

        last_names = DataAnalyzer.get_last_names_from_full_names(self.processed_data)
        unique_names = list(set(last_names))
        general_count = 0

        for name in unique_names:
            count = last_names.count(name)
            if count > 1:
                general_count += count

        return general_count

    def get_duplicate_phones(self) -> tuple:
        """
            Получает дублирующиеся телефоны из обработанных данных и возвращает их,
            а также количество повторяющихся телефонов.
        :return: (tuple) Кортеж с двумя элементами:
            - non_uniq (list), содержащий дублирующиеся телефоны в качестве ключей и количество их
                               повторений в качестве значений.
            - number_of_repeating_phones (int), представляющее общее количество повторяющихся телефонов.
        """

        phone_key = 'Телефон'
        phones = DataAnalyzer.get_elem_from_list_of_dict_by_key(self.processed_data, phone_key)
        uniq_phones = list(set(phones))
        non_uniq = {}

        for phone in uniq_phones:
            count = phones.count(phone)
            if count > 1:
                non_uniq[phone] = count

        number_of_repeating_phones = len(non_uniq)

        return non_uniq, number_of_repeating_phones

    def get_count_births_by_year(self) -> list:
        """
        Рассчитывает количество рождений по годам из обработанных данных и возвращает словарь,
        где ключами являются годы рождения, а значениями - количество рождений в каждом году.
        :return: (dict) Словарь, где ключами являются годы рождения, а значениями - количество рождений в каждом году.
        """

        year_of_birth_key = 'День рождения'
        birthdays = DataAnalyzer.get_elem_from_list_of_dict_by_key(self.processed_data, year_of_birth_key)
        years_of_birth = DataAnalyzer.get_year_from_date(birthdays)
        years_of_birth_uniq = list(set(years_of_birth))
        births_by_year = {}

        for year in years_of_birth_uniq:
            count = years_of_birth.count(year)
            births_by_year[year] = count

        return births_by_year

    @staticmethod
    def get_gender(analyzed_data: str) -> str:
        """
            Определяет пол на основе анализа данных.
        :param analyzed_data: (str) Анализируемые данные, которые содержат информацию об отчестве или имени.
        :return: (str) Определенный пол на основе анализа данных. Возможные значения: 'Муж' (мужской пол), 'Жен' (женский пол),
               'Не определен' (пол не может быть определен на основе данных).
        """
        last_letter_of_middle_name = (analyzed_data[-2:]).strip().lower()

        if last_letter_of_middle_name in ['ич', 'лы']:
            return 'Муж'
        elif last_letter_of_middle_name in ['на', 'зы']:
            return 'Жен'
        else:
            return 'Не определен'






