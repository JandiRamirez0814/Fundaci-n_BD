from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE fundacion.Proyectosbd (
  ID_Proy INT NOT NULL AUTO_INCREMENT,
  Titulo_proy VARCHAR(50)not null,
  Descripcion_proy VARCHAR(100)not null,
  Tema_proy VARCHAR(100) not null,
  Alcance_proy VARCHAR(50)not null,
  Presupuesto_proy DECIMAL(10, 2)not null,
  FechaInicio DATE not null,
  FechaFin DATE not null,
  Responsable_proy INT not null,
  primary key(id_proy),
  UNIQUE INDEX `id_proy_UNIQUE` (id_proy ASC) VISIBLE,
  INDEX `id_emp_idx` (`Responsable_proy` ASC) VISIBLE,
  CONSTRAINT `id_emp`
    FOREIGN KEY (`Responsable_proy`)
    REFERENCES `fundacion`.`administrativosbd` (`id_emp`)
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
    sql='DROP TABLE proyectosbd'
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
        
class Proyecto:
    def __init__(self, Titulo, Descripcion,Tema,Alcance, Presupuesto, Inicio, Fin,Responsable):
        self.Titulo=Titulo
        self.Descripcion=Descripcion
        self.Tema=Tema
        self.Alcance=Alcance
        self.Presupuesto=Presupuesto
        self.Inicio=Inicio
        self.Fin=Fin
        self.Responsable=Responsable
    def __str__(self):
        return f'Proyecto({self.Titulo},{self.Descripcion},{self.Tema}{self.Alcance},{self.Presupuesto},{self.Inicio},{self.Fin},{self.Responsable})'
    
def guardar_Proyecto(proyecto):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`proyectosbd` (`Titulo_proy`, `Descripcion_proy`, `Tema_proy`,`Alcance_proy`, `Presupuesto_proy`, `FechaInicio`, `FechaFin`, `Responsable_proy`) VALUES ('{proyecto.Titulo}', '{proyecto.Descripcion}','{proyecto.Tema}', '{proyecto.Alcance}', '{proyecto.Presupuesto}', '{proyecto.Inicio}', '{proyecto.Fin}','{proyecto.Responsable}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Proy():
    conexion= ConexionBD()
    lista_proyectos=[]
    sql="""SELECT *
FROM proyectosbd"""
    try:
        conexion.cursor.execute(sql)
        lista_proyectos=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_proyectos
def editar_Proy(proyecto, id_proy):
    conexion= ConexionBD()
    sql=f"""UPDATE `fundacion`.`PROYECTOSBD` SET `Titulo_proy` = '{proyecto.Titulo}', `Descripcion_proy` = '{proyecto.Descripcion}', `Tema_proy` = '{proyecto.Tema}', `Alcance_proy` = '{proyecto.Alcance}', `Presupuesto_proy` = '{proyecto.Presupuesto}', `FechaInicio` = '{proyecto.Inicio}', `FechaFin` = '{proyecto.Fin}',`Responsable_proy`='{proyecto.Responsable}' WHERE ID_Proy = '{id_proy}';"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        print(sql)
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Proy(id_proy):
    conexion= ConexionBD()
    sql=f"""DELETE FROM proyectosbd WHERE id_proy={id_proy}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)
        
def buscar_resp_proy(id_resp):
    conexion=ConexionBD()
    lista_resp=[]
    sql=f"""SELECT * FROM administrativosbd WHERE id_emp ='{id_resp}'"""
    try:
        conexion.cursor.execute(sql)
        lista_resp=conexion.cursor.fetchone()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_resp