from file_manager import FileManager
import charset_normalizer
LIST_OF_DELIMITERS = [',', ';', ':', '\t']
DELIMITER_LINE = '\n'


class FileAnalyzer(FileManager):
    @staticmethod
    def coding_detection(file_for_detecting: str) -> str:
        """
            Определяет кодировку текстового файла.
        :param file_for_detecting: (str) Путь к файлу, для которого нужно определить кодировку.
        :return: (str) Кодировка файла.
        """
        with open(file_for_detecting, 'rb') as f:
            content = f.read()
        result = charset_normalizer.detect(content)
        return result['encoding']

    @staticmethod
    def delimiter_identify(data_for_identify) -> str:
        """
            Определяет разделитель для текстовых файлов.
        :param data_for_identify: (list) Список строк из файла, для которых нужно определить разделитель.
        :return: (str) Разделитель для файла.
        """
        for elem in LIST_OF_DELIMITERS:
            if elem in data_for_identify[0]:
                return elem
