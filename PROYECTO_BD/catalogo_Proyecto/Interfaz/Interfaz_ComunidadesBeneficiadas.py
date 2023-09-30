import tkinter as tk
from tkinter import ttk,messagebox
from model.comunidades_beneficiadas_dao import crear_tabla, borrar_tabla,ComBen,eliminar_ComBen,guardar_ComBen, listar_ComBen, editar_ComBen,buscar_proyecto,buscar_comunidad
def barra_menu_comben(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='COMUNIDADES BENEFICIADAS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Comunidades-Beneficiadas',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Comunidades-Beneficiadas',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Comunidades-Beneficiadas',font=('Times New Roman', 12, 'bold'), command=root.destroy)

class Frame_ComBen(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        self.id_ComBen_Selected=None
        self.campos_ComBen()
        self.deshabilitar_campos_comben()
        self.tabla_comben()
        #seccion..
    #funciones comunidades
    def campos_ComBen(self):
        #creo Labels
        self.label_comunidadComBen= tk.Label(self, text='Comunidad: ', fg='black')
        self.label_comunidadComBen.config(font=('Times New Roman', 12, 'bold'))
        self.label_comunidadComBen.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_proyectoComBen= tk.Label(self, text='Proyecto: ', fg='black')
        self.label_proyectoComBen.config(font=('Times New Roman', 12, 'bold'))
        self.label_proyectoComBen.grid(row=2,column=0, padx=10, pady=7)
        #campos entrada
        self.recoger_comunidad= tk.StringVar()
        self.entry_comunidadComBen=tk.Entry(self,textvariable=self.recoger_comunidad)
        self.entry_comunidadComBen.config(width=30,font=('Times New Roman', 12))
        self.entry_comunidadComBen.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_proyecto= tk.StringVar()
        self.entry_proyectoComBen=tk.Entry(self, textvariable=self.recoger_proyecto)
        self.entry_proyectoComBen.config(width=30,font=('Times New Roman', 12))
        self.entry_proyectoComBen.grid(row=2, column=1, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_comben)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_comben)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=4, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_comben)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=4, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_comben(self):
        self.recoger_comunidad.set('')
        self.recoger_proyecto.set('')
     
        self.entry_comunidadComBen.config(state='normal')
        self.entry_proyectoComBen.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_comben(self):
        self.id_ComBen_Selected=None
        self.recoger_comunidad.set('')
        self.recoger_proyecto.set('')
     
        self.entry_comunidadComBen.config(state='disabled')
        self.entry_proyectoComBen.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_comben(self):
        comben= ComBen(
            Comunidad=self.recoger_comunidad.get(),
            Proyecto=self.recoger_proyecto.get()
        )
        if self.id_ComBen_Selected==None:
            guardar_ComBen(comben)
        else:
            editar_ComBen(comben, self.id_ComBen_Selected)
        self.tabla_comben()
        self.deshabilitar_campos_comben()
    def tabla_comben(self):
        self.lista_comben= listar_ComBen()
        
        self.tabla_ComBen= ttk.Treeview(self,column=('Codigo', 'Comunidad', 'Proyecto'))
        self.tabla_ComBen.grid(row=5, column=0, columnspan=3, sticky='nse')
        self.tabla_ComBen.column('#0', width=100)
        self.tabla_ComBen.column('Comunidad', width=120)
        self.tabla_ComBen.column('Proyecto', width=120)
        #scrollbar
        self.scroll_ComBen= ttk.Scrollbar(self, orient='vertical', command=self.tabla_ComBen.yview)
        self.scroll_ComBen.grid(row=4,column=4,sticky='nse')
        self.tabla_ComBen.config(yscrollcommand=self.scroll_ComBen.set)
        #textos columnas
        self.tabla_ComBen.heading('#0',text='CODIGO')
        self.tabla_ComBen.heading('#1',text='COMUNIDAD')
        self.tabla_ComBen.heading('#2',text='PROYECTO')
        ##iterar lista
        for p in self.lista_comben:
            self.tabla_ComBen.insert('',0, text=p[0],
                                  values= (p[1], p[2]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_comben)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=6, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_comben)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=6, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Llaves',command=self.buscar_datos_comben)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=6, column=0,padx=10, pady=7)
    def editar_comben(self):
        try:
            self.id_ComBen_Selected=self.tabla_ComBen.item(self.tabla_ComBen.selection())['text']
            self.comunidad_ComBen_Selected=self.tabla_ComBen.item(
                self.tabla_ComBen.selection())['values'][0]
            self.proyecto_ComBen_Selected=self.tabla_ComBen.item(
                self.tabla_ComBen.selection())['values'][1]
            self.habilitar_campos_comben()
            self.entry_comunidadComBen.insert(0,self.comunidad_ComBen_Selected)
            self.entry_proyectoComBen.insert(0,self.proyecto_ComBen_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_comben(self):
        try:
            self.id_ComBen_Selected=self.tabla_ComBen.item(self.tabla_ComBen.selection())['text']
            eliminar_ComBen(self.id_ComBen_Selected)
            self.tabla_comben()
            self.id_ComBen_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
    def buscar_datos_comben(self):
        self.kay1_Selected_Buscar=self.tabla_ComBen.item(
                self.tabla_ComBen.selection())['values'][0]
        self.kay2_Selected_Buscar=self.tabla_ComBen.item(
                self.tabla_ComBen.selection())['values'][1]
        try:
            self.lista_com= buscar_comunidad(self.kay1_Selected_Buscar)
            self.lista_proy=buscar_proyecto(self.kay2_Selected_Buscar)
            message=f"""COMUNIDAD: ----\n ID: {self.lista_com[0]} --{self.lista_com[1]} \nETNIA: {self.lista_com[2]}\nREPRESENTANTE:{self.lista_com[3]}\n\nPROYECTO: ----\nID: {self.lista_proy[0]} --{self.lista_proy[1]} \nDESCRIPCIÓN: {self.lista_proy[2]}\nTEMA: {self.lista_proy[3]} \nALCANCE: {self.lista_proy[4]}\nPRESUPUESTO: {self.lista_proy[5]}\nINICIO: {self.lista_proy[6]}----- FIN: {self.lista_proy[7]}\nREPRESENTANTE: {self.lista_proy[8]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Seleccione una tupla!!!"
            messagebox.showerror(titulo, mensaje)