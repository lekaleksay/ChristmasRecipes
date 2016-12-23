# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:
    #метод подключения к бд
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    #метод для получения строки
    def select(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT answer FROM answers WHERE id = ?', (rownum,)).fetchall()[0]

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()