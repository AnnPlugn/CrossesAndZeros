import os


class NameDB:
    def __init__(self):
        self._name_db = input("Введите имя базы данных: ")
        self._name_tb = input("Введите имя таблицы: ")
        return

    def get_name_db(self):
        return self._name_db

    def get_name_tb(self):
        return self._name_tb


os.system('cls' if os.name == 'nt' else 'clear')
namedb = NameDB()
