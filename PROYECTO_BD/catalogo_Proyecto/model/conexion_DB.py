import pymysql

class ConexionBD:
    def __init__(self):
        self.conexion= pymysql.connect(
            host='localhost',
            user='root',
            password='12345',
            db='fundacion'
        )
        self.cursor=self.conexion.cursor()
        
    def cerrar_BD(self):
        self.conexion.commit()
        self.conexion.close()