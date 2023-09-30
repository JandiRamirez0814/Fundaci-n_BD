from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE `fundacion`.`participantesproyectobd` (
  `id_ppro` INT NOT NULL AUTO_INCREMENT,
  `rol_ppro` VARCHAR(45) NOT NULL,
  `tarea_ppro` VARCHAR(45) NOT NULL,
  `tiempo_ppro` DATETIME NOT NULL,
  `pro_ppro` INT NOT NULL,
  `proy_ppro` INT NOT NULL,
  PRIMARY KEY (`id_ppro`),
  UNIQUE INDEX `id_ppro_UNIQUE` (`id_ppro` ASC) VISIBLE,
  INDEX `profesional_idx` (`pro_ppro` ASC) VISIBLE,
  INDEX `proyecto_idx` (`proy_ppro` ASC) VISIBLE,
  CONSTRAINT `profesional`
    FOREIGN KEY (`pro_ppro`)
    REFERENCES `fundacion`.`profesionalesbd` (`Id_emp`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `proyecto`
    FOREIGN KEY (`proy_ppro`)
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
    sql='DROP TABLE participantesproyectobd'
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
        
class PartiProy:
    def __init__(self, Rol, Tarea,Tiempo,Profesional,Proyecto):
        self.Rol= Rol
        self.Tarea=Tarea
        self.Tiempo=Tiempo
        self.Profesional=Profesional
        self.Proyecto=Proyecto

    def __str__(self):
        return f'PartiProy({self.Rol},{self.Tarea},{self.Tiempo},{self.Profesional},{self.Proyecto})'
    
def guardar_PartiProy(partiproy):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`participantesproyectobd` (`rol_ppro`, `tarea_ppro`, `tiempo_ppro`,`pro_ppro`,`proy_ppro`) VALUES ('{partiproy.Rol}', '{partiproy.Tarea}','{partiproy.Tiempo}','{partiproy.Profesional}','{partiproy.Proyecto}') ;"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos\n o el representante no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_PartiProy():
    conexion= ConexionBD()
    lista_partiproy=[]
    sql="""SELECT *
FROM participantesproyectobd;"""
    try:
        conexion.cursor.execute(sql)
        lista_partiproy=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_partiproy
def editar_PartiProy(partiproy, id_partiproy):
    conexion= ConexionBD()
    sql=f"""UPDATE participantesproyectobd
set rol_ppro='{partiproy.Rol}', tarea_ppro='{partiproy.Tarea}', tiempo_ppro='{partiproy.Tiempo}',pro_ppro='{partiproy.Profesional}',proy_ppro='{partiproy.Proyecto}'
where id_ppro={id_partiproy};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        print(sql)
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_PartiProy(id_partiproy):
    conexion= ConexionBD()
    sql=f"""DELETE FROM participantesproyectobd WHERE Id_ppro={id_partiproy}"""
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
def buscar_profesional(id_pro):
    conexion=ConexionBD()
    lista_profesional=[]
    sql=f"""SELECT * FROM profesionalesbd WHERE id_emp ='{id_pro}'"""
    try:
        conexion.cursor.execute(sql)
        lista_profesional=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_profesional