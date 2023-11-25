from flask import Blueprint
import cx_Oracle
import json

models = Blueprint('models', __name__)

class Oracle():
    def __init__(self):
        self.un = 'SYSTEM'
        self.cs = '127.0.0.1:1521/XE'
        self.pw = 'root'
        self.connection = None
        self.sql = None

    def user_login(self,nm_usuario):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        validation = False
        #new_nm_usuario = nm_usuario.upper()
        sql = (f"SELECT NM_USUARIO FROM USERS WHERE NM_USUARIO = '{nm_usuario}'")
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    if row:
                        validation = True
                        return validation
                    else:
                        validation = False
                        return validation
            except cx_Oracle.Error as error:
                print('Erro ao executar funcao:', error)
                return None
        