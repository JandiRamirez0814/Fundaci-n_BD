from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE `fundacion`.`representantesbd` (
  `id_Repre` INT NOT NULL AUTO_INCREMENT,
  `nombres_repre` VARCHAR(15) NOT NULL,
  `apellidos_repre` VARCHAR(15) NOT NULL,
  `tel_repre` VARCHAR(10) NOT NULL,
  `sexo_Repre` VARCHAR(1) NOT NULL,
  `dir_ciudad_repre` VARCHAR(15) NOT NULL,
  `dir_barrio_repre` VARCHAR(15) NOT NULL,
  `dir_casa_Repre` VARCHAR(15) NOT NULL,
  `dir_calle_repre` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id_Repre`),
  UNIQUE INDEX `id_Repre_UNIQUE` (`id_Repre` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
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
    sql='DROP TABLE RepresentantesBD'
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
        
class Representante:
    def __init__(self, Nombre, Apellido,Telefono, Sexo, Ciudad, Barrio, Casa, Calle):
        self.Nombre= Nombre
        self.Apellido=Apellido
        self.Telefono=Telefono
        self.Sexo=Sexo
        self.Ciudad=Ciudad
        self.Barrio=Barrio
        self.Casa=Casa
        self.Calle=Calle
    def __str__(self):
        return f'Comunidad({self.Nombre},{self.Apellido},{self.Telefono},{self.Sexo},{self.Ciudad},{self.Barrio},{self.Casa},{self.Calle})'
    
def guardar_Representante(representante):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`representantesbd` (`nombres_repre`, `apellidos_repre`, `tel_repre`, `sexo_Repre`, `dir_ciudad_repre`, `dir_barrio_repre`, `dir_casa_Repre`, `dir_calle_repre`) VALUES ('{representante.Nombre}', '{representante.Apellido}', '{representante.Telefono}', '{representante.Sexo}', '{representante.Ciudad}', '{representante.Barrio}', '{representante.Casa}', '{representante.Calle}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Repre():
    conexion= ConexionBD()
    lista_representantes=[]
    sql="""SELECT *
FROM representantesbd"""
    try:
        conexion.cursor.execute(sql)
        lista_representantes=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_representantes
def editar_Repre(representante, id_repre):
    conexion= ConexionBD()
    sql=f"""UPDATE representantesbd
set Nombres_repre='{representante.Nombre}', Apellidos_repre='{representante.Apellido}', tel_Repre='{representante.Telefono}',sexo_repre='{representante.Sexo}',dir_ciudad_repre='{representante.Ciudad}',dir_barrio_repre='{representante.Barrio}', dir_casa_repre='{representante.Casa}', dir_calle_repre='{representante.Calle}'
where id_repre={id_repre};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Repre(id_repre):
    conexion= ConexionBD()
    sql=f"""DELETE FROM representantesbd WHERE Id_repre={id_repre}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)