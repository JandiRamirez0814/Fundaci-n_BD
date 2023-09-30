from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE fundacion.Niñosbd (
  ID_nin INT NOT NULL AUTO_INCREMENT,
  nombre_nin varchar(20)not null,
  apellidos_nin varchar(20)not null,
  edad_nin int CHECK(edad_nin between 0 and 18) not null,
  genero_nin VARCHAR(1)not null,
  com_nin INT not null,
  primary key(Id_nin),
  UNIQUE INDEX `id_nin_UNIQUE` (id_nin ASC) VISIBLE,
  INDEX `id_com_idx` (`com_nin` ASC) VISIBLE,
  CONSTRAINT `id_com`
    FOREIGN KEY (`com_nin`)
    REFERENCES `fundacion`.`comunidadesbd` (`id_com`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;
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
    sql='DROP TABLE niñosbd'
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
        
class Niño:
    def __init__(self, Nombre, Apellidos,Edad, Genero, Comunidad):
        self.Nombre=Nombre
        self.Apellidos=Apellidos
        self.Edad=Edad
        self.Genero=Genero
        self.Comunidad=Comunidad
    def __str__(self):
        return f'Niño({self.Nombre},{self.Apellidos},{self.Edad},{self.Genero},{self.Comunidad})'
    
def guardar_Niño(niño):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`niñosbd` (`nombre_nin`, `apellidos_nin`, `edad_nin`, `genero_nin`, `com_nin`) VALUES ('{niño.Nombre}', '{niño.Apellidos}', '{niño.Edad}', '{niño.Genero}', '{niño.Comunidad}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Niño():
    conexion= ConexionBD()
    lista_niños=[]
    sql="""SELECT *
FROM niñosbd"""
    try:
        conexion.cursor.execute(sql)
        lista_niños=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_niños
def editar_Niño(niño, id_niño):
    conexion= ConexionBD()
    sql=f"""UPDATE `fundacion`.`niñosbd` SET `nombre_nin` = '{niño.Nombre}', `apellidos_nin` = '{niño.Apellidos}', `edad_nin` = '{niño.Edad}', `genero_nin` = '{niño.Genero}', `com_nin` = '{niño.Comunidad}' WHERE id_nin = '{id_niño}';"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Niño(id_niño):
    conexion= ConexionBD()
    sql=f"""DELETE FROM niñosbd WHERE id_proy={id_niño}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)
        
def buscar_com_niño(id_com):
    conexion=ConexionBD()
    lista_coms=[]
    sql=f"""SELECT * FROM comunidadesbd WHERE id_com ='{id_com}'"""
    try:
        conexion.cursor.execute(sql)
        lista_coms=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_coms