import tkinter as tk
from tkinter import ttk,messagebox
from model.profesionales_dao import crear_tabla, borrar_tabla,Profesional,eliminar_Pro,guardar_Profesional, listar_Pro, editar_Pro
def barra_menu_pro(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='PROFESIONALES', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Profesional',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Profesional',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Profesional',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Pro(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        self.id_Pro_Selected=None
        self.campos_Profesional()
        self.deshabilitar_campos_pro()
        self.tabla_profesionales()
        #seccion..
    #funciones comunidades
    def campos_Profesional(self):
        #creo Labels
        self.label_nombrePro= tk.Label(self, text='Nombre: ', fg='black')
        self.label_nombrePro.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombrePro.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_appelidoPro= tk.Label(self, text='Apellido: ', fg='black')
        self.label_appelidoPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_appelidoPro.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_sexoPro= tk.Label(self, text='Sexo: ', fg='black')
        self.label_sexoPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_sexoPro.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_telefonoPro= tk.Label(self, text='Telefono: ', fg='black')
        self.label_telefonoPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_telefonoPro.grid(row=4,column=0, padx=10, pady=7)
        
        self.label_salarioPro= tk.Label(self, text='Salario: ', fg='black')
        self.label_salarioPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_salarioPro.grid(row=1,column=2, padx=10, pady=7)
        
        self.label_especializacionPro= tk.Label(self, text='Especializacion: ', fg='black')
        self.label_especializacionPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_especializacionPro.grid(row=2,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_nombre= tk.StringVar()
        self.entry_nombrePro=tk.Entry(self,textvariable=self.recoger_nombre)
        self.entry_nombrePro.config(width=30,font=('Times New Roman', 12))
        self.entry_nombrePro.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_appelido= tk.StringVar()
        self.entry_appellidoPro=tk.Entry(self, textvariable=self.recoger_appelido)
        self.entry_appellidoPro.config(width=30,font=('Times New Roman', 12))
        self.entry_appellidoPro.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_sexo= tk.StringVar()
        self.entry_sexoPro=tk.Entry(self, textvariable=self.recoger_sexo)
        self.entry_sexoPro.config(width=30,font=('Times New Roman', 12))
        self.entry_sexoPro.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_telefono= tk.StringVar()
        self.entry_telefonoPro=tk.Entry(self, textvariable=self.recoger_telefono)
        self.entry_telefonoPro.config(width=30,font=('Times New Roman', 12))
        self.entry_telefonoPro.grid(row=4, column=1, padx=10, pady=7)
        
        self.recoger_salario= tk.StringVar()
        self.entry_salarioPro=tk.Entry(self, textvariable=self.recoger_salario)
        self.entry_salarioPro.config(width=30,font=('Times New Roman', 12))
        self.entry_salarioPro.grid(row=1, column=4, padx=10, pady=7)
        
        self.recoger_especializacion= tk.StringVar()
        self.entry_especializacionPro=tk.Entry(self, textvariable=self.recoger_especializacion)
        self.entry_especializacionPro.config(width=30,font=('Times New Roman', 12))
        self.entry_especializacionPro.grid(row=2, column=4, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_pro)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=5, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_pro)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=5, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_pro)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=5, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_pro(self):
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_sexo.set('')
        self.recoger_telefono.set('')
        self.recoger_salario.set('')
        self.recoger_especializacion.set('')
     
        self.entry_nombrePro.config(state='normal')
        self.entry_appellidoPro.config(state='normal')
        self.entry_sexoPro.config(state='normal')
        self.entry_telefonoPro.config(state='normal')
        self.entry_salarioPro.config(state='normal')
        self.entry_especializacionPro.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_pro(self):
        self.id_Repre_Selected=None
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_sexo.set('')
        self.recoger_telefono.set('')
        self.recoger_salario.set('')
        self.recoger_especializacion.set('')
        
        self.entry_nombrePro.config(state='disabled')
        self.entry_appellidoPro.config(state='disabled')
        self.entry_sexoPro.config(state='disabled')
        self.entry_telefonoPro.config(state='disabled')
        self.entry_salarioPro.config(state='disabled')
        self.entry_especializacionPro.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_pro(self):
        profesional= Profesional(
            Nombre=self.recoger_nombre.get(),
            Apellido=self.recoger_appelido.get(),
            Sexo=self.recoger_sexo.get(),
            Telefono=self.recoger_telefono.get(),
            Salario=self.recoger_salario.get(),
            Especializacion=self.recoger_especializacion.get()
        )
        if self.id_Pro_Selected==None:
            guardar_Profesional(profesional)
        else:
            editar_Pro(profesional, self.id_Pro_Selected)
        self.tabla_profesionales()
        self.deshabilitar_campos_pro()
    def tabla_profesionales(self):
        self.lista_Pro= listar_Pro()
        
        self.tabla_Pro= ttk.Treeview(self,columns=('Nombre', 'Apellido','Sexo','Telefono','Salario','Especializacion'))
        self.tabla_Pro.grid(row=6, column=0 ,columnspan=5)
        self.tabla_Pro.column('#0', width=100)
        self.tabla_Pro.column('Nombre', width=120)
        self.tabla_Pro.column('Apellido', width=120)
        self.tabla_Pro.column('Sexo', width=50)
        self.tabla_Pro.column('Telefono', width=120)
        self.tabla_Pro.column('Salario', width=150)
        self.tabla_Pro.column('Especializacion',width=120)
        #scrollbar
        self.scroll_Pro= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Pro.yview)
        self.scroll_Pro.grid(row=6,column=4,sticky='nse')
        self.tabla_Pro.config(yscrollcommand=self.scroll_Pro.set)
        #textos columnas
        self.tabla_Pro.heading('#0',text='CODIGO')
        self.tabla_Pro.heading('#1',text='NOMBRE')
        self.tabla_Pro.heading('#2',text='APELLIDO')
        self.tabla_Pro.heading('#3',text='SEXO')
        self.tabla_Pro.heading('#4',text='TELEFONO')
        self.tabla_Pro.heading('#5',text='SALARIO')
        self.tabla_Pro.heading('#6',text='ESPECIALIZACION')
        ##iterar lista
        for p in self.lista_Pro:
            self.tabla_Pro.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5],p[6]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Pro)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=8, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Pro)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=2,padx=10, pady=7)
    def editar_Pro(self):
        try:
            self.id_Pro_Selected=self.tabla_Pro.item(self.tabla_Pro.selection())['text']
            self.Nombre_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][0]
            self.Apellido_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][1]
            self.Sexo_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][2]
            self.Telefono_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][3]
            self.Salario_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][4]
            self.Especializacion_Pro_Selected=self.tabla_Pro.item(
                self.tabla_Pro.selection())['values'][5]
            self.habilitar_campos_pro()
            self.entry_nombrePro.insert(0,self.Nombre_Pro_Selected)
            self.entry_appellidoPro.insert(0,self.Apellido_Pro_Selected)
            self.entry_sexoPro.insert(0,self.Sexo_Pro_Selected)
            self.entry_telefonoPro.insert(0,self.Telefono_Pro_Selected)
            self.entry_salarioPro.insert(0,self.Salario_Pro_Selected)
            self.entry_especializacionPro.insert(0,self.Especializacion_Pro_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_Pro(self):
        try:
            self.id_Pro_Selected=self.tabla_Pro.item(self.tabla_Pro.selection())['text']
            eliminar_Pro(self.id_Pro_Selected)
            self.tabla_profesionales()
            self.id_Pro_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)