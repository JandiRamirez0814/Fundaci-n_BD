import tkinter as tk
from tkinter import ttk,messagebox
from model.proyectos_objetivos_dao import crear_tabla, borrar_tabla,ProObj,eliminar_ProObj,guardar_ProObj, listar_ProObj, editar_ProObj,buscar_proyecto,buscar_objetivo
def barra_menu_proobj(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='OBJETIVOS PROYECTOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Objetivos-Proyectos',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Objetivos-Proyectos',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Objetivos-Proyectos',font=('Times New Roman', 12, 'bold'), command=root.destroy)

class Frame_ProObj(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        self.id_ProObj_Selected=None
        self.campos_ProObj()
        self.deshabilitar_campos_proobj()
        self.tabla_proObj()
        #seccion..
    #funciones comunidades
    def campos_ProObj(self):
        #creo Labels
        self.label_proyectoProObj= tk.Label(self, text='Proyecto: ', fg='black')
        self.label_proyectoProObj.config(font=('Times New Roman', 12, 'bold'))
        self.label_proyectoProObj.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_objetivoProObj= tk.Label(self, text='Objetivo: ', fg='black')
        self.label_objetivoProObj.config(font=('Times New Roman', 12, 'bold'))
        self.label_objetivoProObj.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_cumplimientoProObj= tk.Label(self, text='Cumplimento: ', fg='black')
        self.label_cumplimientoProObj.config(font=('Times New Roman', 12, 'bold'))
        self.label_cumplimientoProObj.grid(row=3,column=0, padx=10, pady=7)
        #campos entrada
        self.recoger_proyecto= tk.StringVar()
        self.entry_proyectoProObj=tk.Entry(self,textvariable=self.recoger_proyecto)
        self.entry_proyectoProObj.config(width=30,font=('Times New Roman', 12))
        self.entry_proyectoProObj.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_objetivo= tk.StringVar()
        self.entry_objetivoProObj=tk.Entry(self, textvariable=self.recoger_objetivo)
        self.entry_objetivoProObj.config(width=30,font=('Times New Roman', 12))
        self.entry_objetivoProObj.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_cumpliento= tk.StringVar()
        self.entry_cumplimientoProObj=tk.Entry(self, textvariable=self.recoger_cumpliento)
        self.entry_cumplimientoProObj.config(width=30,font=('Times New Roman', 12))
        self.entry_cumplimientoProObj.grid(row=3, column=1, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_proobj)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_proobj)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=4, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_proobj)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=4, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_proobj(self):
        self.recoger_proyecto.set('')
        self.recoger_objetivo.set('')
        self.recoger_cumpliento.set('')
     
        self.entry_proyectoProObj.config(state='normal')
        self.entry_objetivoProObj.config(state='normal')
        self.entry_cumplimientoProObj.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_proobj(self):
        self.id_ProObj_Selected=None
        self.recoger_proyecto.set('')
        self.recoger_objetivo.set('')
        self.recoger_cumpliento.set('')

     
        self.entry_proyectoProObj.config(state='disabled')
        self.entry_objetivoProObj.config(state='disabled')
        self.entry_cumplimientoProObj.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_proobj(self):
        proobj= ProObj(
            Proyecto=self.recoger_proyecto.get(),
            Objetivo=self.recoger_objetivo.get(),
            Cumplimiento=self.recoger_cumpliento.get()
        )
        if self.id_ProObj_Selected==None:
            guardar_ProObj(proobj)
        else:
            editar_ProObj(proobj, self.id_ProObj_Selected)
        self.tabla_proObj()
        self.deshabilitar_campos_proobj()
    def tabla_proObj(self):
        self.lista_proobj= listar_ProObj()
        
        self.tabla_ProObj= ttk.Treeview(self,column=('Codigo', 'Proyecto', 'Objetivo','Cumplimiento'))
        self.tabla_ProObj.grid(row=5, column=0, columnspan=5, sticky='nse')
        self.tabla_ProObj.column('#0', width=100)
        self.tabla_ProObj.column('Proyecto', width=120)
        self.tabla_ProObj.column('Objetivo', width=120)
        self.tabla_ProObj.column('Cumplimiento', width=120)
        #scrollbar
        self.scroll_ProObj= ttk.Scrollbar(self, orient='vertical', command=self.tabla_ProObj.yview)
        self.scroll_ProObj.grid(row=4,column=6,sticky='nse')
        self.tabla_ProObj.config(yscrollcommand=self.scroll_ProObj.set)
        #textos columnas
        self.tabla_ProObj.heading('#0',text='CODIGO')
        self.tabla_ProObj.heading('#1',text='PROYECTO')
        self.tabla_ProObj.heading('#2',text='OBJETIVO')
        self.tabla_ProObj.heading('#3',text='CUMPLIMIENTO')
        ##iterar lista
        for p in self.lista_proobj:
            self.tabla_ProObj.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_proobj)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=6, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_proobj)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=6, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Llaves',command=self.buscar_datos_proobj)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=6, column=0,padx=10, pady=7)
    def editar_proobj(self):
        try:
            self.id_PartiPro_Selected=self.tabla_ProObj.item(self.tabla_ProObj.selection())['text']
            self.proyecto_ProObj_Selected=self.tabla_ProObj.item(
                self.tabla_ProObj.selection())['values'][0]
            self.objetivo_ProObj_Selected=self.tabla_ProObj.item(
                self.tabla_ProObj.selection())['values'][1]
            self.cumplimiento_ProObj_Selected=self.tabla_ProObj.item(
                self.tabla_ProObj.selection())['values'][2]
            self.habilitar_campos_proobj()
            self.entry_proyectoProObj.insert(0,self.proyecto_ProObj_Selected)
            self.entry_objetivoProObj.insert(0,self.objetivo_ProObj_Selected)
            self.entry_cumplimientoProObj.insert(0,self.cumplimiento_ProObj_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_proobj(self):
        try:
            self.id_ProObj_Selected=self.tabla_ProObj.item(self.tabla_ProObj.selection())['text']
            eliminar_ProObj(self.id_ProObj_Selected)
            self.tabla_proObj()
            self.id_ProObj_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
    def buscar_datos_proobj(self):
        self.kay1_Selected_Buscar=self.tabla_ProObj.item(
                self.tabla_ProObj.selection())['values'][1]
        self.kay2_Selected_Buscar=self.tabla_ProObj.item(
                self.tabla_ProObj.selection())['values'][0]
        try:
            self.lista_Objet= buscar_objetivo(self.kay1_Selected_Buscar)
            self.lista_proy=buscar_proyecto(self.kay2_Selected_Buscar)
            message=f"""PROYECTO: ----\n {self.lista_proy[0]} --{self.lista_proy[1]}\nDESCRIPCIÓN: {self.lista_proy[2]}\nTEMA: {self.lista_proy[3]}\nALCANCE: {self.lista_proy[4]}\nPRESUPUESTO: {self.lista_proy[5]}\nINICIO: {self.lista_proy[6]} -- FIN: {self.lista_proy[7]}\nREPRESENTANTE: {self.lista_proy[8]}\n\nOBJETIVO: -----\nID:{self.lista_Objet[0]} \nDESCRIPCIÓN: {self.lista_Objet[1]}\nTIPO: {self.lista_Objet[2]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Sellecione una tupla!!!"
            messagebox.showerror(titulo, mensaje)