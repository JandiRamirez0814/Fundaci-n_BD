import tkinter as tk
from tkinter import ttk,messagebox
from model.proyectos_dao import crear_tabla, borrar_tabla,Proyecto,eliminar_Proy,guardar_Proyecto, listar_Proy, editar_Proy,buscar_resp_proy
def barra_menu_proy(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='PROYECTOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Proyectos',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Proyectos',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Proyectos',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Proy(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        self.id_Proy_Selected=None
        self.campos_Proyecto()
        self.deshabilitar_campos_proy()
        self.tabla_proyectos()
        #seccion..
    #funciones comunidades
    def campos_Proyecto(self):
        #creo Labels
        self.label_tituloProy= tk.Label(self, text='Titulo: ', fg='black')
        self.label_tituloProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_tituloProy.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_descripcionProy= tk.Label(self, text='Descripcion: ', fg='black')
        self.label_descripcionProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_descripcionProy.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_temaProy= tk.Label(self, text='Tema: ', fg='black')
        self.label_temaProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_temaProy.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_AlcanceProy= tk.Label(self, text='Alcance: ', fg='black')
        self.label_AlcanceProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_AlcanceProy.grid(row=4,column=0, padx=10, pady=7)
        
        self.label_presupuestoProy= tk.Label(self, text='Presupuesto: ', fg='black')
        self.label_presupuestoProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_presupuestoProy.grid(row=1,column=2, padx=10, pady=7)
        
        self.label_inicioProy= tk.Label(self, text='Inicio: ', fg='black')
        self.label_inicioProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_inicioProy.grid(row=2,column=2, padx=10, pady=7)
        
        self.label_FinProy= tk.Label(self, text='Fin: ', fg='black')
        self.label_FinProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_FinProy.grid(row=3,column=2, padx=10, pady=7)
        
        self.label_responsableProy= tk.Label(self, text='Responsable: ', fg='black')
        self.label_responsableProy.config(font=('Times New Roman', 12, 'bold'))
        self.label_responsableProy.grid(row=4,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_titulo= tk.StringVar()
        self.entry_tituloProy=tk.Entry(self,textvariable=self.recoger_titulo)
        self.entry_tituloProy.config(width=30,font=('Times New Roman', 12))
        self.entry_tituloProy.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_descripcion= tk.StringVar()
        self.entry_descripcionProy=tk.Entry(self, textvariable=self.recoger_descripcion)
        self.entry_descripcionProy.config(width=30,font=('Times New Roman', 12))
        self.entry_descripcionProy.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_tema= tk.StringVar()
        self.entry_temaProy=tk.Entry(self, textvariable=self.recoger_tema)
        self.entry_temaProy.config(width=30,font=('Times New Roman', 12))
        self.entry_temaProy.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_alcance= tk.StringVar()
        self.entry_alcanceProy=tk.Entry(self, textvariable=self.recoger_alcance)
        self.entry_alcanceProy.config(width=30,font=('Times New Roman', 12))
        self.entry_alcanceProy.grid(row=4, column=1, padx=10, pady=7)
        
        self.recoger_presupuesto= tk.StringVar()
        self.entry_presupuestoProy=tk.Entry(self, textvariable=self.recoger_presupuesto)
        self.entry_presupuestoProy.config(width=30,font=('Times New Roman', 12))
        self.entry_presupuestoProy.grid(row=1, column=3, padx=10, pady=7)
        
        self.recoger_inicio= tk.StringVar()
        self.entry_inicioProy=tk.Entry(self, textvariable=self.recoger_inicio)
        self.entry_inicioProy.config(width=30,font=('Times New Roman', 12))
        self.entry_inicioProy.grid(row=2, column=3, padx=10, pady=7)
        
        self.recoger_fin= tk.StringVar()
        self.entry_finProy=tk.Entry(self, textvariable=self.recoger_fin)
        self.entry_finProy.config(width=30,font=('Times New Roman', 12))
        self.entry_finProy.grid(row=3, column=3, padx=10, pady=7)
        
        self.recoger_responsable= tk.StringVar()
        self.entry_responsableProy=tk.Entry(self, textvariable=self.recoger_responsable)
        self.entry_responsableProy.config(width=30,font=('Times New Roman', 12))
        self.entry_responsableProy.grid(row=4, column=3, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_proy)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=5, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_proy)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=5, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_proy)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=5, column=2,padx=10, pady=7)
        
        #habilitar campos
    def habilitar_campos_proy(self):
        self.recoger_titulo.set('')
        self.recoger_descripcion.set('')
        self.recoger_tema.set('')
        self.recoger_alcance.set('')
        self.recoger_presupuesto.set('')
        self.recoger_inicio.set('')
        self.recoger_fin.set('')
        self.recoger_responsable.set('')
     
        self.entry_tituloProy.config(state='normal')
        self.entry_descripcionProy.config(state='normal')
        self.entry_temaProy.config(state='normal')
        self.entry_alcanceProy.config(state='normal')
        self.entry_presupuestoProy.config(state='normal')
        self.entry_inicioProy.config(state='normal')
        self.entry_finProy.config(state='normal')
        self.entry_responsableProy.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_proy(self):
        self.id_Proy_Selected=None
        self.recoger_titulo.set('')
        self.recoger_descripcion.set('')
        self.recoger_tema.set('')
        self.recoger_alcance.set('')
        self.recoger_presupuesto.set('')
        self.recoger_inicio.set('')
        self.recoger_fin.set('')
        self.recoger_responsable.set('')
     
        self.entry_tituloProy.config(state='disabled')
        self.entry_descripcionProy.config(state='disabled')
        self.entry_temaProy.config(state='disabled')
        self.entry_alcanceProy.config(state='disabled')
        self.entry_presupuestoProy.config(state='disabled')
        self.entry_inicioProy.config(state='disabled')
        self.entry_finProy.config(state='disabled')
        self.entry_responsableProy.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_proy(self):
        proyecto= Proyecto(
            Titulo=self.recoger_titulo.get(),
            Descripcion=self.recoger_descripcion.get(),
            Tema=self.recoger_tema.get(),
            Alcance=self.recoger_alcance.get(),
            Presupuesto=self.recoger_presupuesto.get(),
            Inicio=self.recoger_inicio.get(),
            Fin=self.recoger_fin.get(),
            Responsable=self.recoger_responsable.get()
        )
        if self.id_Proy_Selected==None:
            guardar_Proyecto(proyecto)
        else:
            editar_Proy(proyecto, self.id_Proy_Selected)
        self.tabla_proyectos()
        self.deshabilitar_campos_proy()
    def tabla_proyectos(self):
        self.lista_Proy= listar_Proy()
        
        self.tabla_Proy= ttk.Treeview(self,columns=('Titulo', 'Descripcion','Tema','Alcance','Presupuesto','Inicio','Fin','Responsable'))
        self.tabla_Proy.grid(row=6, column=0 ,columnspan=5)
        self.tabla_Proy.column('#0', width=100)
        self.tabla_Proy.column('Titulo', width=120)
        self.tabla_Proy.column('Descripcion', width=120)
        self.tabla_Proy.column('Tema', width=120)
        self.tabla_Proy.column('Alcance', width=100)
        self.tabla_Proy.column('Presupuesto', width=120)
        self.tabla_Proy.column('Inicio', width=150)
        self.tabla_Proy.column('Fin', width=120)
        self.tabla_Proy.column('Responsable', width=120)
        #scrollbar
        self.scroll_Proy= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Proy.yview)
        self.scroll_Proy.grid(row=6,column=4,sticky='nse')
        self.tabla_Proy.config(yscrollcommand=self.scroll_Proy.set)
        #textos columnas
        self.tabla_Proy.heading('#0',text='CODIGO')
        self.tabla_Proy.heading('#1',text='TITULO')
        self.tabla_Proy.heading('#2',text='DESCRIPCION')
        self.tabla_Proy.heading('#3',text='TEMA')
        self.tabla_Proy.heading('#4',text='ALCANCE')
        self.tabla_Proy.heading('#5',text='PRESUPUESTO')
        self.tabla_Proy.heading('#6',text='INICIO')
        self.tabla_Proy.heading('#7',text='FIN')
        self.tabla_Proy.heading('#8',text='RESPONSABLE')

        ##iterar lista
        for p in self.lista_Proy:
            self.tabla_Proy.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5],p[6],p[7],p[8]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Proy)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=8, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Proy)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Responsable',command=self.buscar_datos_Proy)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=8, column=0,padx=10, pady=7)
    def editar_Proy(self):
        try:
            self.id_Proy_Selected=self.tabla_Proy.item(self.tabla_Proy.selection())['text']
            self.Titulo_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][0]
            self.Descripcion_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][1]
            self.Tema_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][2]
            self.Alcance_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][3]
            self.Presupuesto_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][4]
            self.Inicio_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][5]
            self.Fin_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][6]
            self.Responsable_Proy_Selected=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][7]
            self.habilitar_campos_proy()
            self.entry_tituloProy.insert(0,self.Titulo_Proy_Selected)
            self.entry_descripcionProy.insert(0,self.Descripcion_Proy_Selected)
            self.entry_temaProy.insert(0,self.Tema_Proy_Selected)
            self.entry_alcanceProy.insert(0,self.Alcance_Proy_Selected)
            self.entry_presupuestoProy.insert(0,self.Presupuesto_Proy_Selected)
            self.entry_inicioProy.insert(0,self.Inicio_Proy_Selected)
            self.entry_finProy.insert(0,self.Fin_Proy_Selected)
            self.entry_responsableProy.insert(0,self.Responsable_Proy_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_Proy(self):
        try:
            self.id_Proy_Selected=self.tabla_Proy.item(self.tabla_Proy.selection())['text']
            eliminar_Proy(self.id_Proy_Selected)
            self.tabla_proyectos()
            self.id_Proy_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
            
    def buscar_datos_Proy(self):
        self.id_resp_Selected_Buscar=self.tabla_Proy.item(
                self.tabla_Proy.selection())['values'][7]
        try:
            self.lista_resp= buscar_resp_proy(self.id_resp_Selected_Buscar)
            message=f"""RESPONSABLE: ----\nID: {self.lista_resp[0]} --{self.lista_resp[1]} {self.lista_resp[2]}\nSEXO: {self.lista_resp[3]}\nTELEFONO: {self.lista_resp[4]}\nSALARIO:{self.lista_resp[5]}\nCARGO: {self.lista_resp[6]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Sellecione una tupla!!!"
            messagebox.showerror(titulo, mensaje)
            