import tkinter as tk
from tkinter import ttk,messagebox
from model.comunidades_dao import crear_tabla, borrar_tabla,Comunidad,eliminar_Com,guardar_Comunidad, listar_Com, editar_Com,buscar_repre_Com
def barra_menu_com(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='COMUNIDADES', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Comunidad',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Comunidad',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Comunidad',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Com(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        self.id_Com_Selected=None
        self.campos_Comunidad()
        self.deshabilitar_campos_com()
        self.tabla_comunidades()
        #seccion..
    #funciones comunidades
    def campos_Comunidad(self):
        #creo Labels
        self.label_nombreCom= tk.Label(self, text='Nombre: ', fg='black')
        self.label_nombreCom.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombreCom.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_etniaCom= tk.Label(self, text='Etnia: ', fg='black')
        self.label_etniaCom.config(font=('Times New Roman', 12, 'bold'))
        self.label_etniaCom.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_repreCom= tk.Label(self, text='Representante: ', fg='black')
        self.label_repreCom.config(font=('Times New Roman', 12, 'bold'))
        self.label_repreCom.grid(row=3,column=0, padx=10, pady=7)
        #campos entrada
        self.recoger_nombre= tk.StringVar()
        self.entry_nombreCom=tk.Entry(self,textvariable=self.recoger_nombre)
        self.entry_nombreCom.config(width=30,font=('Times New Roman', 12))
        self.entry_nombreCom.grid(row=1, column=1, padx=10, pady=7,columnspan=2)
        
        self.recoger_etnia= tk.StringVar()
        self.entry_etniaCom=tk.Entry(self, textvariable=self.recoger_etnia)
        self.entry_etniaCom.config(width=30,font=('Times New Roman', 12))
        self.entry_etniaCom.grid(row=2, column=1, padx=10, pady=7,columnspan=2)
        
        self.recoger_repre= tk.StringVar()
        self.entry_repreCom=tk.Entry(self, textvariable=self.recoger_repre)
        self.entry_repreCom.config(width=30,font=('Times New Roman', 12))
        self.entry_repreCom.grid(row=3, column=1, padx=10, pady=7,columnspan=2)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_com)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_com)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=4, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_com)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=4, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_com(self):
        self.recoger_nombre.set('')
        self.recoger_etnia.set('')
        self.recoger_repre.set('')
     
        self.entry_nombreCom.config(state='normal')
        self.entry_etniaCom.config(state='normal')
        self.entry_repreCom.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_com(self):
        self.id_Com_Selected=None
        self.recoger_nombre.set('')
        self.recoger_etnia.set('')
        self.recoger_repre.set('')
        
        self.entry_nombreCom.config(state='disabled')
        self.entry_etniaCom.config(state='disabled')
        self.entry_repreCom.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_com(self):
        comunidad= Comunidad(
            Nombre=self.recoger_nombre.get(),
            Etnia=self.recoger_etnia.get(),
            Representante=self.recoger_repre.get()
        )
        if self.id_Com_Selected==None:
            guardar_Comunidad(comunidad)
        else:
            editar_Com(comunidad, self.id_Com_Selected)
        self.tabla_comunidades()
        self.deshabilitar_campos_com()
    def tabla_comunidades(self):
        self.lista_Com= listar_Com()
        
        self.tabla_Com= ttk.Treeview(self,column=('Codigo', 'Nombre', 'Etnia'))
        self.tabla_Com.grid(row=5, column=0, columnspan=3, sticky='nse')
        #scrollbar
        self.scroll_Com= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Com.yview)
        self.scroll_Com.grid(row=4,column=4,sticky='nse')
        self.tabla_Com.config(yscrollcommand=self.scroll_Com.set)
        #textos columnas
        self.tabla_Com.heading('#0',text='CODIGO')
        self.tabla_Com.heading('#1',text='NOMBRE')
        self.tabla_Com.heading('#2',text='ETNIA')
        self.tabla_Com.heading('#3',text='REPRESENTANTE')
        ##iterar lista
        for p in self.lista_Com:
            self.tabla_Com.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Com)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=6, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Com)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=6, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Representante',command=self.buscar_datos_Com)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=6, column=0,padx=10, pady=7)
    def editar_Com(self):
        try:
            self.id_Com_Selected=self.tabla_Com.item(self.tabla_Com.selection())['text']
            self.nombre_Com_Selected=self.tabla_Com.item(
                self.tabla_Com.selection())['values'][0]
            self.Etnia_Com_Selected=self.tabla_Com.item(
                self.tabla_Com.selection())['values'][1]
            self.Repre_Com_Selected=self.tabla_Com.item(
                self.tabla_Com.selection())['values'][2]
            self.habilitar_campos_com()
            self.entry_nombreCom.insert(0,self.nombre_Com_Selected)
            self.entry_etniaCom.insert(0,self.Etnia_Com_Selected)
            self.entry_repreCom.insert(0,self.Repre_Com_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_Com(self):
        try:
            self.id_Com_Selected=self.tabla_Com.item(self.tabla_Com.selection())['text']
            eliminar_Com(self.id_Com_Selected)
            self.tabla_comunidades()
            self.id_Com_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
    def buscar_datos_Com(self):
        self.Repre_Com_Selected_Buscar=self.tabla_Com.item(
                self.tabla_Com.selection())['values'][2]
        try:
            self.lista_repre= buscar_repre_Com(self.Repre_Com_Selected_Buscar)
            message=f"""REPRESENTANTE: ----\n ID: {self.lista_repre[0]} - {self.lista_repre[1]} {self.lista_repre[2]}\nTELEFONO: {self.lista_repre[3]}  \nSEXO:{self.lista_repre[4]}\nCIUDAD: {self.lista_repre[5]} \nDIRECCIÓN: {self.lista_repre[6]}-{self.lista_repre[7]}-{self.lista_repre[8]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Sellecione una tupla!!!"
            messagebox.showerror(titulo, mensaje)
            