from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE fundacion.profesionalesbd (
  Id_emp INT NOT NULL AUTO_INCREMENT,
  Nombres_emp VARCHAR(20)not null,
  Apellidos_emp varchar(20)not null,
  sexo_emp varchar(1)not null,
  telefono_emp varchar(10)not null,
  salario_emp numeric(10,2)not null,
  especia_emp varchar(40)not null,
  primary key(Id_emp),
  UNIQUE INDEX `id_emp_UNIQUE` (Id_emp ASC) VISIBLE)
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
    sql='DROP TABLE profesionalesbd'
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
        
class Profesional:
    def __init__(self, Nombre, Apellido,Sexo, Telefono, Salario,Especializacion):
        self.Nombre= Nombre
        self.Apellido=Apellido
        self.Sexo=Sexo
        self.Telefono=Telefono
        self.Salario=Salario
        self.Especializacion=Especializacion
    def __str__(self):
        return f'Profesional({self.Nombre},{self.Apellido},{self.Sexo},{self.Telefono},{self.Salario},{self.Especializacion})'
    
def guardar_Profesional(empleado):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`profesionalesbd` (`Nombres_emp`, `Apellidos_emp`, `sexo_emp`, `telefono_emp`, `salario_emp`,`especia_emp`) VALUES ('{empleado.Nombre}', '{empleado.Apellido}', '{empleado.Sexo}', '{empleado.Telefono}', '{empleado.Salario}', '{empleado.Especializacion}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Pro():
    conexion= ConexionBD()
    lista_profesionales=[]
    sql="""SELECT *
FROM `profesionalesbd`"""
    try:
        conexion.cursor.execute(sql)
        lista_profesionales=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_profesionales
def editar_Pro(empleado, id_pro):
    conexion= ConexionBD()
    sql2=f"""UPDATE profesionalesbd
set Nombres_emp='{empleado.Nombre}', Apellidos_emp='{empleado.Apellido}', sexo_emp='{empleado.Sexo}',telefono_emp='{empleado.Telefono}',salario_emp='{empleado.Salario}',especia_emp='{empleado.Especializacion}'
where id_emp={id_pro};"""
    try:
        conexion.cursor.execute(sql2)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Pro(id_pro):
    conexion= ConexionBD()
    sql=f"""DELETE FROM profesionalesbd WHERE Id_emp={id_pro};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)