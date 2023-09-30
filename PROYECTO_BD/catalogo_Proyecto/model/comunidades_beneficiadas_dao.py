from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE `fundacion`.`comunidadesbeneficiadasbd` (
  `id_cb` INT NOT NULL AUTO_INCREMENT,
  `comunidad_cb` INT NOT NULL,
  `proyecto_cb` INT NOT NULL,
  PRIMARY KEY (`id_cb`),
  UNIQUE INDEX `id_cb_UNIQUE` (`id_cb` ASC) VISIBLE,
  INDEX `comunidadcosa_idx` (`comunidad_cb` ASC) VISIBLE,
  INDEX `proyectocosa_idx` (`proyecto_cb` ASC) VISIBLE,
  CONSTRAINT `comunidad12`
    FOREIGN KEY (`comunidad_cb`)
    REFERENCES `fundacion`.`comunidadesbd` (`id_Com`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `proyecto12`
    FOREIGN KEY (`proyecto_cb`)
    REFERENCES `fundacion`.`proyectosbd` (`ID_Proy`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;'''
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
    sql='DROP TABLE comunidadesbeneficiadasbd'
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
        
class ComBen:
    def __init__(self, Comunidad, Proyecto):
        self.Comunidad= Comunidad
        self.Proyecto=Proyecto

    def __str__(self):
        return f'ComBen({self.Comunidad},{self.Proyecto})'
    
def guardar_ComBen(comben):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`comunidadesbeneficiadasbd` (`comunidad_cb`, `proyecto_cb`) VALUES ('{comben.Comunidad}', '{comben.Proyecto}') ;"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos\n o el representante no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_ComBen():
    conexion= ConexionBD()
    lista_comben=[]
    sql="""SELECT *
FROM comunidadesbeneficiadasbd;"""
    try:
        conexion.cursor.execute(sql)
        lista_comben=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_comben
def editar_ComBen(comben, id_comben):
    conexion= ConexionBD()
    sql=f"""UPDATE comunidadesbeneficiadasbd
set comunidad_cb='{comben.Comunidad}', proyecto_cb='{comben.Proyecto}'
where id_cb={id_comben};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_ComBen(id_comben):
    conexion= ConexionBD()
    sql=f"""DELETE FROM comunidadesbeneficiadasbd WHERE id_cb={id_comben}"""
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
def buscar_comunidad(id_com):
    conexion=ConexionBD()
    lista_comunidad=[]
    sql=f"""SELECT * FROM comunidadesbd WHERE id_com ='{id_com}'"""
    try:
        conexion.cursor.execute(sql)
        lista_comunidad=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_comunidad