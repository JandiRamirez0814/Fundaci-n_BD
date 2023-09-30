from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE `fundacion`.`objetivosproyectosbd` (
  `id_po` INT NOT NULL AUTO_INCREMENT,
  `proyecto_po` INT NOT NULL,
  `objetivo_po` INT NOT NULL,
  `cumplimiento_po`INT CHECK(cumplimiento_po between 0 and 100) NOT NULL,
  PRIMARY KEY (`id_po`),
  UNIQUE INDEX `id_po_UNIQUE` (`id_po` ASC) VISIBLE,
  INDEX `proyectopo_idx` (`proyecto_po` ASC) VISIBLE,
  INDEX `objetivospo_idx` (`objetivo_po` ASC) VISIBLE,
  CONSTRAINT `proyectopo`
    FOREIGN KEY (`proyecto_po`)
    REFERENCES `fundacion`.`proyectosbd` (`ID_Proy`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `objetivospo`
    FOREIGN KEY (`objetivo_po`)
    REFERENCES `fundacion`.`objetivosbd` (`id_obj`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);'''
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
    sql='DROP TABLE objetivosproyectosbd'
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
        
class ProObj:
    def __init__(self, Proyecto, Objetivo,Cumplimiento):
        self.Proyecto=Proyecto
        self.Objetivo=Objetivo
        self.Cumplimiento=Cumplimiento

    def __str__(self):
        return f'ProObj({self.Proyecto},{self.Objetivo},{self.Cumplimiento})'
    
def guardar_ProObj(proobj):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`objetivosproyectosbd` (`proyecto_po`, `objetivo_po`,`cumplimiento_po`) VALUES ('{proobj.Proyecto}', '{proobj.Objetivo}','{proobj.Cumplimiento}') ;"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos\n o el representante no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_ProObj():
    conexion= ConexionBD()
    lista_ProObj=[]
    sql="""SELECT *
FROM objetivosproyectosbd;"""
    try:
        conexion.cursor.execute(sql)
        lista_ProObj=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_ProObj
def editar_ProObj(proobj, id_proobj):
    conexion= ConexionBD()
    sql=f"""UPDATE objetivosproyectosbd
set proyecto_po='{proobj.Proyecto}', objetivo_po='{proobj.Objetivo}',cumplimiento_po='{proobj.Cumplimiento}'
where id_po={id_proobj};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_ProObj(id_proobj):
    conexion= ConexionBD()
    sql=f"""DELETE FROM objetivosproyectosbd WHERE id_po={id_proobj}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def buscar_proyecto(id_pro):
    conexion=ConexionBD()
    lista_proyecto=[]
    sql=f"""SELECT * FROM proyectosbd WHERE id_proy ='{id_pro}'"""
    try:
        conexion.cursor.execute(sql)
        lista_proyecto=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_proyecto
def buscar_objetivo(id_obj):
    conexion=ConexionBD()
    lista_profesional=[]
    sql=f"""SELECT * FROM objetivosbd WHERE id_obj ='{id_obj}'"""
    try:
        conexion.cursor.execute(sql)
        lista_profesional=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_profesional