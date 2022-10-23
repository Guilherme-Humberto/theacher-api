import mysql.connector
from src.config.database import config


class Connection:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = mysql.connector.connect(**config)
        self._cursor = self._connection.cursor(dictionary=True)

        isConnected = self._connection.is_connected()

        if isConnected: print('Conectado ao mysql')
        else: print('Erro ao conectar o mysql')

    def close(self):
        if not self._connection == None:
            self._connection.close()
            self._cursor.close()
            print('Conexão encerrada')

    def query(self, sql, *args):
        if args: self._cursor.execute(sql, *args)
        else: self._cursor.execute(sql)
        return self._cursor
    
    def commit(self):
        return self._connection.commit()
            