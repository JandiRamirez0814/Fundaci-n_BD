from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
CREATE TABLE `fundacion`.`comunidadesbd` (
  `id_com` INT NOT NULL AUTO_INCREMENT,
  `nombre_com` VARCHAR(45) NOT NULL,
  `etnia_com` VARCHAR(45) NOT NULL,
  `repre_com` INT NOT NULL,
  PRIMARY KEY (`id_com`),
  UNIQUE INDEX `id_com_UNIQUE` (`id_com` ASC) VISIBLE,
  UNIQUE INDEX `repre_com_UNIQUE` (`repre_com` ASC) VISIBLE,
  CONSTRAINT `representanteid`
    FOREIGN KEY (`repre_com`)
    REFERENCES `fundacion`.`representantesbd` (`id_Repre`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);

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
    sql='DROP TABLE ComunidadesBD'
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
        
class Comunidad:
    def __init__(self, Nombre, Etnia,Representante):
        self.Nombre= Nombre
        self.Etnia=Etnia
        self.Representante=Representante
    def __str__(self):
        return f'Comunidad({self.Nombre},{self.Etnia},{self.Representante})'
    
def guardar_Comunidad(comunidad):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`comunidadesbd` (`Nombre_Com`, `Etnia_Com`, `Repre_Com`) VALUES ('{comunidad.Nombre}', '{comunidad.Etnia}','{comunidad.Representante}') ;"""
    #print(sql)
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos\n o el representante no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Com():
    conexion= ConexionBD()
    lista_comunidades=[]
    sql="""SELECT *
FROM comunidadesbd"""
    try:
        conexion.cursor.execute(sql)
        lista_comunidades=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_comunidades
def editar_Com(comunidad, id_comunidad):
    conexion= ConexionBD()
    sql=f"""UPDATE comunidadesbd
set Nombre_Com='{comunidad.Nombre}', Etnia_Com='{comunidad.Etnia}', Repre_Com='{comunidad.Representante}'
where id_com={id_comunidad};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Com(id_comunidad):
    conexion= ConexionBD()
    sql=f"""DELETE FROM comunidadesbd WHERE Id_Com={id_comunidad}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def buscar_repre_Com(id_repre):
    conexion=ConexionBD()
    lista_repre=[]
    sql=f"""SELECT * FROM representantesbd WHERE id_repre ='{id_repre}'"""
    try:
        conexion.cursor.execute(sql)
        lista_repre=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_repre