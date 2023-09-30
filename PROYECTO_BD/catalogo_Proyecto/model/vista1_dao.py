from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
CREATE VIEW `vista1` AS(
SELECT P.ID_PROY, P.TITULO_PROY, AVG(OP.CUMPLIMIENTO_PO)
FROM PROYECTOSBD P INNER JOIN OBJETIVOSPROYECTOSBD OP ON P.ID_PROY=OP.PROYECTO_PO
INNER JOIN OBJETIVOSBD O ON OP.OBJETIVO_PO=O.ID_OBJ
GROUP BY P.ID_PROY);

    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        titulo="Crear Tabla"
        mensaje="Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo="Crear Tabla"
        mensaje="La tabla ya existe en la base de datos"
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion=ConexionBD()
    sql='DROP VIEW vista1'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        titulo="Borrar Tabla"
        mensaje="Se borro la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo="Borrar Tabla"
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
    
def listar_Vista1():
    conexion= ConexionBD()
    lista_vista1=[]
    sql="""SELECT *
FROM vista1"""
    try:
        conexion.cursor.execute(sql)
        lista_vista1=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_vista1
