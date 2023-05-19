from file_manager import FileManager

LIST_OF_DELIMITERS = [',', ';', ':', '\t']
DELIMITER_LINE = '\n'


class FileSaver(FileManager):
    @staticmethod
    def save_file(saving_data: list, file_name: str) -> None:
        """
            Сохраняет данные из списка словарей в файл.
        :param saving_data: (list) Список словарей, содержащих данные для сохранения.
        :param file_name: (str) Имя файла, в который нужно сохранить данные.
        :return: None
        """
        list_without_dict = []

        for line in range(len(saving_data)):
            saving_data_str = ', '.join(
                f'{key}: {value}' for key, value in saving_data[line].items())
            list_without_dict.append(saving_data_str)

        saving_data_str = DELIMITER_LINE.join(list_without_dict)

        with open(file_name, 'w') as f:
            f.write(saving_data_str)

