from file_manager import FileManager
from file_analyzer import FileAnalyzer
import urllib.request
import ssl
import os

LIST_OF_DELIMITERS = [',', ';', ':', '\t']
DELIMITER_LINE = '\n'


class FileDownloader(FileManager):

    def __init__(self, url_for_download: str):
        self.url = url_for_download
        self.name = 'file.csv'
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(self.url, self.name)

    def read_file(self):
        """
            Метод для чтения файла и удаления его после этого.
            :return: Содержимое файла в виде строки.
            :rtype: str
            """

        encod = FileAnalyzer.coding_detection(self.name)

        with open(self.name, 'r', encoding=encod) as f:
            file = f.read()

        if os.path.exists(self.name):
            os.remove(self.name)
        return file
