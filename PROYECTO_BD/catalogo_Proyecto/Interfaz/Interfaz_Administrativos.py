import tkinter as tk
from tkinter import ttk,messagebox
from model.administrativos_dao import crear_tabla, borrar_tabla,Administrativo,eliminar_Admi,guardar_Administrativo, listar_Admi, editar_Admi
def barra_menu_admi(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='ADMINISTRATIVOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Administrativo',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Administrativo',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Administrativo',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Admi(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        self.id_Admi_Selected=None
        self.campos_Administrativos()
        self.deshabilitar_campos_admi()
        self.tabla_administrativos()
        #seccion..
    #funciones comunidades
    def campos_Administrativos(self):
        #creo Labels
        self.label_nombreAdmi= tk.Label(self, text='Nombre: ', fg='black')
        self.label_nombreAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombreAdmi.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_appelidoAdmi= tk.Label(self, text='Apellido: ', fg='black')
        self.label_appelidoAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_appelidoAdmi.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_sexoAdmi= tk.Label(self, text='Sexo: ', fg='black')
        self.label_sexoAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_sexoAdmi.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_telefonoAdmi= tk.Label(self, text='Telefono: ', fg='black')
        self.label_telefonoAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_telefonoAdmi.grid(row=4,column=0, padx=10, pady=7)
        
        self.label_salarioAdmi= tk.Label(self, text='Salario: ', fg='black')
        self.label_salarioAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_salarioAdmi.grid(row=1,column=2, padx=10, pady=7)
        
        self.label_cargoAdmi= tk.Label(self, text='Cargo: ', fg='black')
        self.label_cargoAdmi.config(font=('Times New Roman', 12, 'bold'))
        self.label_cargoAdmi.grid(row=2,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_nombre= tk.StringVar()
        self.entry_nombreAdmi=tk.Entry(self,textvariable=self.recoger_nombre)
        self.entry_nombreAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_nombreAdmi.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_appelido= tk.StringVar()
        self.entry_appellidoAdmi=tk.Entry(self, textvariable=self.recoger_appelido)
        self.entry_appellidoAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_appellidoAdmi.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_sexo= tk.StringVar()
        self.entry_sexoAdmi=tk.Entry(self, textvariable=self.recoger_sexo)
        self.entry_sexoAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_sexoAdmi.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_telefono= tk.StringVar()
        self.entry_telefonoAdmi=tk.Entry(self, textvariable=self.recoger_telefono)
        self.entry_telefonoAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_telefonoAdmi.grid(row=4, column=1, padx=10, pady=7)
        
        self.recoger_salario= tk.StringVar()
        self.entry_salarioAdmi=tk.Entry(self, textvariable=self.recoger_salario)
        self.entry_salarioAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_salarioAdmi.grid(row=1, column=4, padx=10, pady=7)
        
        self.recoger_cargo= tk.StringVar()
        self.entry_cargoAdmi=tk.Entry(self, textvariable=self.recoger_cargo)
        self.entry_cargoAdmi.config(width=30,font=('Times New Roman', 12))
        self.entry_cargoAdmi.grid(row=2, column=4, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_admi)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=5, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_admi)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=5, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_admi)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=5, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_admi(self):
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_sexo.set('')
        self.recoger_telefono.set('')
        self.recoger_salario.set('')
        self.recoger_cargo.set('')
     
        self.entry_nombreAdmi.config(state='normal')
        self.entry_appellidoAdmi.config(state='normal')
        self.entry_sexoAdmi.config(state='normal')
        self.entry_telefonoAdmi.config(state='normal')
        self.entry_salarioAdmi.config(state='normal')
        self.entry_cargoAdmi.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_admi(self):
        self.id_Repre_Selected=None
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_sexo.set('')
        self.recoger_telefono.set('')
        self.recoger_salario.set('')
        self.recoger_cargo.set('')
        
        self.entry_nombreAdmi.config(state='disabled')
        self.entry_appellidoAdmi.config(state='disabled')
        self.entry_sexoAdmi.config(state='disabled')
        self.entry_telefonoAdmi.config(state='disabled')
        self.entry_salarioAdmi.config(state='disabled')
        self.entry_cargoAdmi.config(state='disabled')
           
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_admi(self):
        administrativo= Administrativo(
            Nombre=self.recoger_nombre.get(),
            Apellido=self.recoger_appelido.get(),
            Sexo=self.recoger_sexo.get(),
            Telefono=self.recoger_telefono.get(),
            Salario=self.recoger_salario.get(),
            Cargo=self.recoger_cargo.get()
        )
        if self.id_Admi_Selected==None:
            guardar_Administrativo(administrativo)
        else:
            editar_Admi(administrativo, self.id_Admi_Selected)
        self.tabla_administrativos()
        self.deshabilitar_campos_admi()
    def tabla_administrativos(self):
        self.lista_Admi= listar_Admi()
        
        self.tabla_Admi= ttk.Treeview(self,columns=('Nombre', 'Apellido','Sexo','Telefono','Salario','Cargo'))
        self.tabla_Admi.grid(row=6, column=0 ,columnspan=5)
        self.tabla_Admi.column('#0', width=100)
        self.tabla_Admi.column('Nombre', width=120)
        self.tabla_Admi.column('Apellido', width=120)
        self.tabla_Admi.column('Sexo', width=50)
        self.tabla_Admi.column('Telefono', width=120)
        self.tabla_Admi.column('Salario', width=150)
        self.tabla_Admi.column('Cargo', width=150)
        #scrollbar
        self.scroll_Admi= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Admi.yview)
        self.scroll_Admi.grid(row=6,column=4,sticky='nse')
        self.tabla_Admi.config(yscrollcommand=self.scroll_Admi.set)
        #textos columnas
        self.tabla_Admi.heading('#0',text='CODIGO')
        self.tabla_Admi.heading('#1',text='NOMBRE')
        self.tabla_Admi.heading('#2',text='APELLIDO')
        self.tabla_Admi.heading('#3',text='SEXO')
        self.tabla_Admi.heading('#4',text='TELEFONO')
        self.tabla_Admi.heading('#5',text='SALARIO')
        self.tabla_Admi.heading('#6',text='CARGO')
        ##iterar lista
        for p in self.lista_Admi:
            self.tabla_Admi.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5],p[6]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Admi)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=8, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Admi)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=2,padx=10, pady=7)
    def editar_Admi(self):
        try:
            self.id_Admi_Selected=self.tabla_Admi.item(self.tabla_Admi.selection())['text']
            self.Nombre_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][0]
            self.Apellido_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][1]
            self.Sexo_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][2]
            self.Telefono_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][3]
            self.Salario_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][4]
            self.Cargo_Admi_Selected=self.tabla_Admi.item(
                self.tabla_Admi.selection())['values'][5]
            self.habilitar_campos_admi()
            self.entry_nombreAdmi.insert(0,self.Nombre_Admi_Selected)
            self.entry_appellidoAdmi.insert(0,self.Apellido_Admi_Selected)
            self.entry_sexoAdmi.insert(0,self.Sexo_Admi_Selected)
            self.entry_telefonoAdmi.insert(0,self.Telefono_Admi_Selected)
            self.entry_salarioAdmi.insert(0,self.Salario_Admi_Selected)
            self.entry_cargoAdmi.insert(0, self.Cargo_Admi_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_Admi(self):
        try:
            self.id_Admi_Selected=self.tabla_Admi.item(self.tabla_Admi.selection())['text']
            eliminar_Admi(self.id_Admi_Selected)
            self.tabla_administrativos()
            self.id_Admi_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)