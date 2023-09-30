from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
CREATE  VIEW `vista2` AS(
SELECT C.ID_COM, C.NOMBRE_COM, COUNT(N.ID_NIN)
FROM COMUNIDADESBD C INNER JOIN NIÑOSBD N ON C.ID_COM=N.COM_NIN
GROUP BY C.ID_COM
);

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
    sql='DROP VIEW vista2'
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
    
def listar_Vista2():
    conexion= ConexionBD()
    lista_vista2=[]
    sql="""SELECT *
FROM vista2"""
    try:
        conexion.cursor.execute(sql)
        lista_vista2=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_vista2
