from prettytable import PrettyTable


class Display:
    def __init__(self, obj_data_analyzer):
        self.data_analyzer = obj_data_analyzer

    def table_users_with_incorrect_phone_numbers(self, data):
        """
            Создает и выводит на экран таблицу с информацией о пользователях с некорректными номерами телефонов.
        :param data: список словарей, представляющих информацию о пользователях.
            Каждый словарь содержит ключи, соответствующие полям пользователя, и значения,
            представляющие значения этих полей.
        :return: None
        """
        table = PrettyTable()
        table.title = 'Люди с некорректными номерами'
        table.field_names = list(data[0].keys())

        for item in data:
            table.add_row(list(item.values()))
        table.align = 'l'

        print(table)

    def table_non_unique_phones(self):
        """
            Создает и выводит на экран таблицу с информацией о неуникальных номерах телефонов.
        :param self: ссылка на текущий экземпляр класса, в котором определен метод.
        :return: None

        """
        table = PrettyTable()
        table.title = 'Список неуникальных номеров'
        table.field_names = ['Номер телефона', 'Сколько раз встречается']
        data, count = self.data_analyzer.get_duplicate_phones()

        for key, value in data.items():
            table.add_row([key, value])
        table.align = 'l'

        table.add_row(['Всего повторяющихся номеров', count])

        print(table)

    def table_birth_year_count(self):
        """
            Создает и выводит на экран таблицу с информацией о количестве людей, родившихся в каждом году.
        :param self: ссылка на текущий экземпляр класса, в котором определен метод.
        :return: None
        """
        table = PrettyTable()
        table.title = 'Сколько людей в каком году родилось'
        table.field_names = ['Год', 'Количество людей']
        data = self.data_analyzer.get_count_births_by_year()

        for key, value in data.items():
            table.add_row([key, value])
        table.align = 'l'

        print(table)

    def table_lastname_duplicates(self):
        """
            Создает и выводит на экран таблицу с информацией о количестве однофамильцев.
        :param self: ссылка на текущий экземпляр класса, в котором определен метод.
        :return: None
        """
        table = PrettyTable()
        data = self.data_analyzer.get_count_of_duplicate_surnames()

        table.add_column('Количество однофамильцев', list([data]))
        table.align = 'l'

        print(table)
