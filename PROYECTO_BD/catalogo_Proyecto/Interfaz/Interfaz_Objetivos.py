import tkinter as tk
from tkinter import ttk,messagebox
from model.objetivos_dao import crear_tabla, borrar_tabla,Objetivo,eliminar_Objetivo,guardar_Objetivo, listar_Objetivo, editar_Objetivo
def barra_menu_objetivo(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='OBJETIVOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Objetivos',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Objetivos',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Objetivos',font=('Times New Roman', 12, 'bold'), command=root.destroy)

class Frame_Obj(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        self.id_Obj_Selected=None
        self.campos_Objetivo()
        self.deshabilitar_campos_objetivos()
        self.tabla_objetivos()
        #seccion..
    #funciones comunidades
    def campos_Objetivo(self):
        #creo Labels
        self.label_descripcionObj= tk.Label(self, text='Descripcion: ', fg='black')
        self.label_descripcionObj.config(font=('Times New Roman', 12, 'bold'))
        self.label_descripcionObj.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_tipoObj= tk.Label(self, text='Tipo: ', fg='black')
        self.label_tipoObj.config(font=('Times New Roman', 12, 'bold'))
        self.label_tipoObj.grid(row=2,column=0, padx=10, pady=7)
        #campos entrada
        self.recoger_descripcion= tk.StringVar()
        self.entry_descripcionObj=tk.Entry(self,textvariable=self.recoger_descripcion)
        self.entry_descripcionObj.config(width=30,font=('Times New Roman', 12))
        self.entry_descripcionObj.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_tipo= tk.StringVar()
        self.entry_tipoObj=tk.Entry(self, textvariable=self.recoger_tipo)
        self.entry_tipoObj.config(width=30,font=('Times New Roman', 12))
        self.entry_tipoObj.grid(row=2, column=1, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_objetivos)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_objetivos)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=4, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_objetivos)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=4, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_objetivos(self):
        self.recoger_descripcion.set('')
        self.recoger_tipo.set('')
     
        self.entry_descripcionObj.config(state='normal')
        self.entry_tipoObj.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_objetivos(self):
        self.id_Obj_Selected=None
        self.recoger_descripcion.set('')
        self.recoger_tipo.set('')
     
        self.entry_descripcionObj.config(state='disabled')
        self.entry_tipoObj.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_objetivos(self):
        objetivo= Objetivo(
            Descripcion=self.recoger_descripcion.get(),
            Tipo=self.recoger_tipo.get()
        )
        if self.id_Obj_Selected==None:
            guardar_Objetivo(objetivo)
        else:
            editar_Objetivo(objetivo, self.id_Obj_Selected)
        self.tabla_objetivos()
        self.deshabilitar_campos_objetivos()
    def tabla_objetivos(self):
        self.lista_obj= listar_Objetivo()
        
        self.tabla_Obj= ttk.Treeview(self,column=('Codigo', 'Descripcion', 'Tipo'))
        self.tabla_Obj.grid(row=5, column=0, columnspan=3, sticky='nse')
        self.tabla_Obj.column('#0', width=100)
        self.tabla_Obj.column('Descripcion', width=120)
        self.tabla_Obj.column('Tipo', width=120)
        #scrollbar
        self.scroll_Obj= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Obj.yview)
        self.scroll_Obj.grid(row=4,column=4,sticky='nse')
        self.tabla_Obj.config(yscrollcommand=self.scroll_Obj.set)
        #textos columnas
        self.tabla_Obj.heading('#0',text='CODIGO')
        self.tabla_Obj.heading('#1',text='DESCRIPCION')
        self.tabla_Obj.heading('#2',text='TIPO')
        ##iterar lista
        for p in self.lista_obj:
            self.tabla_Obj.insert('',0, text=p[0],
                                  values= (p[1], p[2]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_objetivos)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=6, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_objetivos)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=6, column=2,padx=10, pady=7)
     
    def editar_objetivos(self):
        try:
            self.id_Obj_Selected=self.tabla_Obj.item(self.tabla_Obj.selection())['text']
            self.descripcion_Obj_Selected=self.tabla_Obj.item(
                self.tabla_Obj.selection())['values'][0]
            self.tipo_Obj_Selected=self.tabla_Obj.item(
                self.tabla_Obj.selection())['values'][1]
            self.habilitar_campos_objetivos()
            self.entry_descripcionObj.insert(0,self.descripcion_Obj_Selected)
            self.entry_tipoObj.insert(0,self.tipo_Obj_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_objetivos(self):
        try:
            self.id_Obj_Selected=self.tabla_Obj.item(self.tabla_Obj.selection())['text']
            eliminar_Objetivo(self.id_Obj_Selected)
            self.tabla_objetivos()
            self.id_Obj_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
