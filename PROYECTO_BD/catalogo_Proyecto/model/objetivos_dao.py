from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE `fundacion`.`objetivosbd` (
  `id_obj` INT NOT NULL AUTO_INCREMENT,
  `descripcion_obj` VARCHAR(45) NOT NULL,
  `tipo_obj` VARCHAR(45)NOT NULL,
  UNIQUE INDEX `id_obj_UNIQUE` (`id_obj` ASC) VISIBLE,
  PRIMARY KEY (`id_obj`));'''
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
    sql='DROP TABLE objetivosbd'
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
        
class Objetivo:
    def __init__(self, Descripcion, Tipo):
        self.Descripcion= Descripcion
        self.Tipo=Tipo

    def __str__(self):
        return f'Objetivo({self.Descripcion},{self.Tipo})'
    
def guardar_Objetivo(objetivo):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`objetivosbd` (`descripcion_obj`, `tipo_obj`) VALUES ('{objetivo.Descripcion}', '{objetivo.Tipo}') ;"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos\n o el representante no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Objetivo():
    conexion= ConexionBD()
    lista_objetivo=[]
    sql="""SELECT *
FROM objetivosbd;"""
    try:
        conexion.cursor.execute(sql)
        lista_objetivo=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_objetivo
def editar_Objetivo(objetivo, id_obj):
    conexion= ConexionBD()
    sql=f"""UPDATE objetivosbd
set descripcion_obj='{objetivo.Descripcion}', tipo_obj='{objetivo.Tipo}'
where id_obj={id_obj};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Objetivo(id_obj):
    conexion= ConexionBD()
    sql=f"""DELETE FROM objetivosbd WHERE id_obj={id_obj}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)
