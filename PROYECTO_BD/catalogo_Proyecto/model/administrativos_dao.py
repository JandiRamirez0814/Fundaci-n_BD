from model.conexion_DB import ConexionBD
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionBD()
    sql='''
    CREATE TABLE fundacion.administrativosbd (
  Id_emp INT NOT NULL AUTO_INCREMENT,
  Nombres_emp VARCHAR(20)not null,
  Apellidos_emp varchar(20)not null,
  sexo_emp varchar(1)not null,
  telefono_emp varchar(10)not null,
  salario_emp numeric(10,2)not null,
  cargo_emp varchar(40)not null,
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
    sql='DROP TABLE administrativosbd'
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
        
class Administrativo:
    def __init__(self, Nombre, Apellido,Sexo, Telefono, Salario,Cargo):
        self.Nombre= Nombre
        self.Apellido=Apellido
        self.Sexo=Sexo
        self.Telefono=Telefono
        self.Salario=Salario
        self.Cargo=Cargo
    def __str__(self):
        return f'Administrativo({self.Nombre},{self.Apellido},{self.Sexo},{self.Telefono},{self.Salario},{self.Cargo})'
    
def guardar_Administrativo(empleado):
    conexion= ConexionBD()
    sql=f"""INSERT INTO `fundacion`.`administrativosbd` (`Nombres_emp`, `Apellidos_emp`, `sexo_emp`, `telefono_emp`, `salario_emp`,`cargo_emp`) VALUES ('{empleado.Nombre}', '{empleado.Apellido}', '{empleado.Sexo}', '{empleado.Telefono}', '{empleado.Salario}','{empleado.Cargo}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Insercion Fallida "
        mensaje="La tabla no existe en la base de datos"
        messagebox.showerror(titulo, mensaje)
def listar_Admi():
    conexion= ConexionBD()
    lista_administrativos=[]
    sql="""SELECT *
FROM administrativosbd;"""
    try:
        conexion.cursor.execute(sql)
        lista_administrativos=conexion.cursor.fetchall()
        conexion.cerrar_BD()
    except:
        titulo="Conexion al registro: "
        mensaje= "Tabla no leida"
        messagebox.showerror(titulo, mensaje)
    return lista_administrativos
def editar_Admi(empleado, id_Admin):
    conexion= ConexionBD()
    sql=f"""UPDATE administrativosbd
set Nombres_emp='{empleado.Nombre}', Apellidos_emp='{empleado.Apellido}', sexo_emp='{empleado.Sexo}',telefono_emp='{empleado.Telefono}',salario_emp='{empleado.Salario}',cargo_emp='{empleado.Cargo}'
where id_emp={id_Admin};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
    except:
        titulo="Modificacion Fallida "
        mensaje="El registro no pudo ser \n modificado en la base de datos"
        messagebox.showerror(titulo, mensaje)
def eliminar_Admi(id_admin):
    conexion= ConexionBD()
    sql=f"""DELETE FROM administrativosbd WHERE Id_emp={id_admin};"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_BD()
        
    except:
        titulo="Eliminacion Fallida "
        mensaje="El registro no pudo ser \n eliminado en la base de datos"
        messagebox.showerror(titulo, mensaje)