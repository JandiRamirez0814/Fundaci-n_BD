import tkinter as tk
from tkinter import ttk,messagebox
from model.participantes_proyecto_dao import crear_tabla, borrar_tabla,PartiProy,eliminar_PartiProy,guardar_PartiProy, listar_PartiProy, editar_PartiProy,buscar_proyecto,buscar_profesional
def barra_menu_partiproy(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='PARTICIPANTES PROYECTOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Participantes-Proyectos',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Participantes-Proyectos',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Participantes-Proyectos',font=('Times New Roman', 12, 'bold'), command=root.destroy)

class Frame_PartiPro(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        self.id_PartiPro_Selected=None
        self.campos_PartiPro()
        self.deshabilitar_campos_partipro()
        self.tabla_PartiPro()
        #seccion..
    #funciones comunidades
    def campos_PartiPro(self):
        #creo Labels
        self.label_rolPartiPro= tk.Label(self, text='Rol: ', fg='black')
        self.label_rolPartiPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_rolPartiPro.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_tareaPartiPro= tk.Label(self, text='Tarea: ', fg='black')
        self.label_tareaPartiPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_tareaPartiPro.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_tiempoPartiPro= tk.Label(self, text='Tiempo: ', fg='black')
        self.label_tiempoPartiPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_tiempoPartiPro.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_profesionalPartiPro= tk.Label(self, text='Profesional: ', fg='black')
        self.label_profesionalPartiPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_profesionalPartiPro.grid(row=1,column=2, padx=10, pady=7)
        
        self.label_proyectoPartiPro= tk.Label(self, text='Proyecto: ', fg='black')
        self.label_proyectoPartiPro.config(font=('Times New Roman', 12, 'bold'))
        self.label_proyectoPartiPro.grid(row=2,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_rol= tk.StringVar()
        self.entry_rolPartiPro=tk.Entry(self,textvariable=self.recoger_rol)
        self.entry_rolPartiPro.config(width=30,font=('Times New Roman', 12))
        self.entry_rolPartiPro.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_tarea= tk.StringVar()
        self.entry_tareaPartiPro=tk.Entry(self, textvariable=self.recoger_tarea)
        self.entry_tareaPartiPro.config(width=30,font=('Times New Roman', 12))
        self.entry_tareaPartiPro.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_tiempo= tk.StringVar()
        self.entry_tiempoPartiPro=tk.Entry(self, textvariable=self.recoger_tiempo)
        self.entry_tiempoPartiPro.config(width=30,font=('Times New Roman', 12))
        self.entry_tiempoPartiPro.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_profesional= tk.StringVar()
        self.entry_profesionalPartiPro=tk.Entry(self, textvariable=self.recoger_profesional)
        self.entry_profesionalPartiPro.config(width=30,font=('Times New Roman', 12))
        self.entry_profesionalPartiPro.grid(row=1, column=3, padx=10, pady=7)
        
        self.recoger_proyecto= tk.StringVar()
        self.entry_proyectoPartiPro=tk.Entry(self, textvariable=self.recoger_proyecto)
        self.entry_proyectoPartiPro.config(width=30,font=('Times New Roman', 12))
        self.entry_proyectoPartiPro.grid(row=2, column=3, padx=10, pady=7)
        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_partipro)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_partipro)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=4, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_partipro)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=4, column=2,padx=10, pady=7)
        #habilitar campos
    def habilitar_campos_partipro(self):
        self.recoger_rol.set('')
        self.recoger_tarea.set('')
        self.recoger_tiempo.set('')
        self.recoger_profesional.set('')
        self.recoger_proyecto.set('')
     
        self.entry_rolPartiPro.config(state='normal')
        self.entry_tareaPartiPro.config(state='normal')
        self.entry_tiempoPartiPro.config(state='normal')
        self.entry_profesionalPartiPro.config(state='normal')
        self.entry_proyectoPartiPro.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_partipro(self):
        self.id_PartiPro_Selected=None
        self.recoger_rol.set('')
        self.recoger_tarea.set('')
        self.recoger_tiempo.set('')
        self.recoger_profesional.set('')
        self.recoger_proyecto.set('')
     
        self.entry_rolPartiPro.config(state='disabled')
        self.entry_tareaPartiPro.config(state='disabled')
        self.entry_tiempoPartiPro.config(state='disabled')
        self.entry_profesionalPartiPro.config(state='disabled')
        self.entry_proyectoPartiPro.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_partipro(self):
        partiproy= PartiProy(
            Rol=self.recoger_rol.get(),
            Tarea=self.recoger_tarea.get(),
            Tiempo=self.recoger_tiempo.get(),
            Profesional=self.recoger_profesional.get(),
            Proyecto=self.recoger_proyecto.get()
        )
        if self.id_PartiPro_Selected==None:
            guardar_PartiProy(partiproy)
        else:
            editar_PartiProy(partiproy, self.id_PartiPro_Selected)
        self.tabla_PartiPro()
        self.deshabilitar_campos_partipro()
    def tabla_PartiPro(self):
        self.lista_partiPro= listar_PartiProy()
        
        self.tabla_partipro= ttk.Treeview(self,column=('Codigo', 'Rol', 'Tarea','Tiempo','Profesional','Proyecto'))
        self.tabla_partipro.grid(row=5, column=0, columnspan=5, sticky='nse')
        self.tabla_partipro.column('#0', width=100)
        self.tabla_partipro.column('Rol', width=120)
        self.tabla_partipro.column('Tarea', width=120)
        self.tabla_partipro.column('Tiempo', width=100)
        self.tabla_partipro.column('Profesional', width=120)
        self.tabla_partipro.column('Proyecto', width=120)
        #scrollbar
        self.scroll_PartiPro= ttk.Scrollbar(self, orient='vertical', command=self.tabla_partipro.yview)
        self.scroll_PartiPro.grid(row=4,column=6,sticky='nse')
        self.tabla_partipro.config(yscrollcommand=self.scroll_PartiPro.set)
        #textos columnas
        self.tabla_partipro.heading('#0',text='CODIGO')
        self.tabla_partipro.heading('#1',text='ROL')
        self.tabla_partipro.heading('#2',text='TAREA')
        self.tabla_partipro.heading('#3',text='TIEMPO')
        self.tabla_partipro.heading('#4',text='PROFESIONAL')
        self.tabla_partipro.heading('#5',text='PROYECTO')
        ##iterar lista
        for p in self.lista_partiPro:
            self.tabla_partipro.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_partipro)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=6, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_partipro)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=6, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Llaves',command=self.buscar_datos_partipro)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=6, column=0,padx=10, pady=7)
    def editar_partipro(self):
        try:
            self.id_PartiPro_Selected=self.tabla_partipro.item(self.tabla_partipro.selection())['text']
            self.rol_PartiPro_Selected=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][0]
            self.tarea_PartiPro_Selected=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][1]
            self.tiempo_PartiPro_Selected=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][2]
            self.profesional_PartiPro_Selected=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][3]
            self.proycto_PartiPro_Selected=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][4]
            self.habilitar_campos_partipro()
            self.entry_rolPartiPro.insert(0,self.rol_PartiPro_Selected)
            self.entry_tareaPartiPro.insert(0,self.tarea_PartiPro_Selected)
            self.entry_tiempoPartiPro.insert(0,self.tiempo_PartiPro_Selected)
            self.entry_profesionalPartiPro.insert(0,self.profesional_PartiPro_Selected)
            self.entry_proyectoPartiPro.insert(0,self.proycto_PartiPro_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)
#funcion comunidades
    def eliminar_datos_partipro(self):
        try:
            self.id_PartiPro_Selected=self.tabla_partipro.item(self.tabla_partipro.selection())['text']
            eliminar_PartiProy(self.id_PartiPro_Selected)
            self.tabla_PartiPro()
            self.id_PartiPro_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
    def buscar_datos_partipro(self):
        self.kay1_Selected_Buscar=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][3]
        self.kay2_Selected_Buscar=self.tabla_partipro.item(
                self.tabla_partipro.selection())['values'][4]
        try:
            self.lista_prof= buscar_profesional(self.kay1_Selected_Buscar)
            self.lista_proy=buscar_proyecto(self.kay2_Selected_Buscar)
            message=f"""PROFESIONAL: ----\nID: {self.lista_prof[0]} --{self.lista_prof[1]} {self.lista_prof[2]}\nSEXO: {self.lista_prof[3]} \nTELEFONO: {self.lista_prof[4]}\nSALARIO: {self.lista_prof[5]}\nESPECIALIZACIÓN: {self.lista_prof[6]}\n\nPROYECTO: ----\nID: {self.lista_proy[0]} --{self.lista_proy[1]} \nDESCRIPCIÓN: {self.lista_proy[2]}\nTEMA: {self.lista_proy[3]}\nALCANCE: {self.lista_proy[4]}\nPRESUPUESTO: {self.lista_proy[5]}\nINICIO: {self.lista_proy[6]} -- FIN: {self.lista_proy[7]}\nREPRESENTANTE: {self.lista_proy[8]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Sellecione una tupla!!!"
            messagebox.showerror(titulo, mensaje)