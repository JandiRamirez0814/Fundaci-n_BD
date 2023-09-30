import tkinter as tk
from tkinter import ttk,messagebox
from model.representantes_dao import crear_tabla, borrar_tabla,Representante,eliminar_Repre,guardar_Representante, listar_Repre, editar_Repre
def barra_menu_repre(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='REPRESENTANTES', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Representante',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Representante',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Representante',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Repre(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        self.id_Repre_Selected=None
        self.campos_Representante()
        self.deshabilitar_campos_repre()
        self.tabla_representantes()
        #seccion..
    #funciones comunidades
    def campos_Representante(self):
        #creo Labels
        self.label_nombreRepre= tk.Label(self, text='Nombre: ', fg='black')
        self.label_nombreRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombreRepre.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_appelidoRepre= tk.Label(self, text='Apellido: ', fg='black')
        self.label_appelidoRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_appelidoRepre.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_telefonoRepre= tk.Label(self, text='Telefono: ', fg='black')
        self.label_telefonoRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_telefonoRepre.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_sexoRepre= tk.Label(self, text='Sexo: ', fg='black')
        self.label_sexoRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_sexoRepre.grid(row=4,column=0, padx=10, pady=7)
        
        self.label_ciudadRepre= tk.Label(self, text='Ciudad: ', fg='black')
        self.label_ciudadRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_ciudadRepre.grid(row=1,column=2, padx=10, pady=7)
        
        self.label_barrionoRepre= tk.Label(self, text='Barrio: ', fg='black')
        self.label_barrionoRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_barrionoRepre.grid(row=2,column=2, padx=10, pady=7)
        
        self.label_casaRepre= tk.Label(self, text='Casa: ', fg='black')
        self.label_casaRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_casaRepre.grid(row=3,column=2, padx=10, pady=7)
        
        self.label_calleRepre= tk.Label(self, text='Calle: ', fg='black')
        self.label_calleRepre.config(font=('Times New Roman', 12, 'bold'))
        self.label_calleRepre.grid(row=4,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_nombre= tk.StringVar()
        self.entry_nombreRepre=tk.Entry(self,textvariable=self.recoger_nombre)
        self.entry_nombreRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_nombreRepre.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_appelido= tk.StringVar()
        self.entry_appellidoRepre=tk.Entry(self, textvariable=self.recoger_appelido)
        self.entry_appellidoRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_appellidoRepre.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_telefono= tk.StringVar()
        self.entry_telefonoRepre=tk.Entry(self, textvariable=self.recoger_telefono)
        self.entry_telefonoRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_telefonoRepre.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_sexo= tk.StringVar()
        self.entry_sexoRepre=tk.Entry(self, textvariable=self.recoger_sexo)
        self.entry_sexoRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_sexoRepre.grid(row=4, column=1, padx=10, pady=7)
        
        self.recoger_ciudad= tk.StringVar()
        self.entry_ciudadRepre=tk.Entry(self, textvariable=self.recoger_ciudad)
        self.entry_ciudadRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_ciudadRepre.grid(row=1, column=4, padx=10, pady=7)
        
        self.recoger_barrio= tk.StringVar()
        self.entry_barrioRepre=tk.Entry(self, textvariable=self.recoger_barrio)
        self.entry_barrioRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_barrioRepre.grid(row=2, column=4, padx=10, pady=7)
        
        self.recoger_casa= tk.StringVar()
        self.entry_casaRepre=tk.Entry(self, textvariable=self.recoger_casa)
        self.entry_casaRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_casaRepre.grid(row=3, column=4, padx=10, pady=7)
        
        self.recoger_calle= tk.StringVar()
        self.entry_calleRepre=tk.Entry(self, textvariable=self.recoger_calle)
        self.entry_calleRepre.config(width=30,font=('Times New Roman', 12))
        self.entry_calleRepre.grid(row=4, column=4, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_repre)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=5, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_repre)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=5, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_repre)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=5, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_repre(self):
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_telefono.set('')
        self.recoger_sexo.set('')
        self.recoger_ciudad.set('')
        self.recoger_barrio.set('')
        self.recoger_casa.set('')
        self.recoger_calle.set('')
     
        self.entry_nombreRepre.config(state='normal')
        self.entry_appellidoRepre.config(state='normal')
        self.entry_telefonoRepre.config(state='normal')
        self.entry_sexoRepre.config(state='normal')
        self.entry_ciudadRepre.config(state='normal')
        self.entry_barrioRepre.config(state='normal')
        self.entry_casaRepre.config(state='normal')
        self.entry_calleRepre.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_repre(self):
        self.id_Repre_Selected=None
        self.recoger_nombre.set('')
        self.recoger_appelido.set('')
        self.recoger_telefono.set('')
        self.recoger_sexo.set('')
        self.recoger_ciudad.set('')
        self.recoger_barrio.set('')
        self.recoger_casa.set('')
        self.recoger_calle.set('')
        
        self.entry_nombreRepre.config(state='disabled')
        self.entry_appellidoRepre.config(state='disabled')
        self.entry_telefonoRepre.config(state='disabled')
        self.entry_sexoRepre.config(state='disabled')
        self.entry_ciudadRepre.config(state='disabled')
        self.entry_barrioRepre.config(state='disabled')
        self.entry_casaRepre.config(state='disabled')
        self.entry_calleRepre.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_repre(self):
        representante= Representante(
            Nombre=self.recoger_nombre.get(),
            Apellido=self.recoger_appelido.get(),
            Telefono=self.recoger_telefono.get(),
            Sexo=self.recoger_sexo.get(),
            Ciudad=self.recoger_ciudad.get(),
            Barrio=self.recoger_barrio.get(),
            Casa=self.recoger_casa.get(),
            Calle=self.recoger_calle.get()
        )
        if self.id_Repre_Selected==None:
            guardar_Representante(representante)
        else:
            editar_Repre(representante, self.id_Repre_Selected)
        self.tabla_representantes()
        self.deshabilitar_campos_repre()
    def tabla_representantes(self):
        self.lista_Rep= listar_Repre()
        
        self.tabla_Repre= ttk.Treeview(self,columns=('Nombre', 'Apellido','Telefono','Sexo','Ciudad','Barrio','Casa','Calle'))
        self.tabla_Repre.grid(row=6, column=0 ,columnspan=5)
        self.tabla_Repre.column('#0', width=100)
        self.tabla_Repre.column('Nombre', width=100)
        self.tabla_Repre.column('Apellido', width=120)
        self.tabla_Repre.column('Telefono', width=120)
        self.tabla_Repre.column('Sexo', width=40)
        self.tabla_Repre.column('Ciudad', width=100)
        self.tabla_Repre.column('Barrio', width=120)
        self.tabla_Repre.column('Casa', width=60)
        self.tabla_Repre.column('Calle', width=60)
        #scrollbar
        self.scroll_Repre= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Repre.yview)
        self.scroll_Repre.grid(row=6,column=4,sticky='nse')
        self.tabla_Repre.config(yscrollcommand=self.scroll_Repre.set)
        #textos columnas
        self.tabla_Repre.heading('#0',text='CODIGO')
        self.tabla_Repre.heading('#1',text='NOMBRE')
        self.tabla_Repre.heading('#2',text='APELLIDO')
        self.tabla_Repre.heading('#3',text='TELEFONO')
        self.tabla_Repre.heading('#4',text='SEXO')
        self.tabla_Repre.heading('#5',text='CIUDAD')
        self.tabla_Repre.heading('#6',text='BARRIO')
        self.tabla_Repre.heading('#7',text='CASA')
        self.tabla_Repre.heading('#8',text='CALLE')
        ##iterar lista
        for p in self.lista_Rep:
            self.tabla_Repre.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5],p[6],p[7],p[8]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Repre)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=8, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Repre)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=2,padx=10, pady=7)
    def editar_Repre(self):
        try:
            self.id_Repre_Selected=self.tabla_Repre.item(self.tabla_Repre.selection())['text']
            self.Nombre_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][0]
            self.Apellido_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][1]
            self.Telefono_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][2]
            self.Sexo_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][3]
            self.Ciudad_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][4]
            self.Barrio_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][5]
            self.Casa_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][6]
            self.Calle_Repre_Selected=self.tabla_Repre.item(
                self.tabla_Repre.selection())['values'][7]
            self.habilitar_campos_repre()
            self.entry_nombreRepre.insert(0,self.Nombre_Repre_Selected)
            self.entry_appellidoRepre.insert(0,self.Apellido_Repre_Selected)
            self.entry_telefonoRepre.insert(0,self.Telefono_Repre_Selected)
            self.entry_sexoRepre.insert(0,self.Sexo_Repre_Selected)
            self.entry_ciudadRepre.insert(0,self.Ciudad_Repre_Selected)
            self.entry_barrioRepre.insert(0,self.Barrio_Repre_Selected)
            self.entry_casaRepre.insert(0,self.Casa_Repre_Selected)
            self.entry_calleRepre.insert(0,self.Calle_Repre_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_Repre(self):
        try:
            self.id_Repre_Selected=self.tabla_Repre.item(self.tabla_Repre.selection())['text']
            eliminar_Repre(self.id_Repre_Selected)
            self.tabla_representantes()
            self.id_Repre_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)