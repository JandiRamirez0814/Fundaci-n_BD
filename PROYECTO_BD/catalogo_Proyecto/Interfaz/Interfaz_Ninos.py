import tkinter as tk
from tkinter import ttk,messagebox
from model.ninos_dao import crear_tabla, borrar_tabla,Niño,eliminar_Niño,guardar_Niño, listar_Niño, editar_Niño,buscar_com_niño
def barra_menu_niño(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='NIÑOS', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Tabla Niño',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Tabla Niño',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Tabla Niño',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Niño(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        self.id_Niño_Selected=None
        self.campos_Niño()
        self.deshabilitar_campos_niño()
        self.tabla_niños()
        #seccion..
    #funciones comunidades
    def campos_Niño(self):
        #creo Labels
        self.label_nombreNiño= tk.Label(self, text='Nombre: ', fg='black')
        self.label_nombreNiño.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombreNiño.grid(row=1,column=0, padx=10, pady=7)
        
        self.label_apellidoNiño= tk.Label(self, text='Apellido: ', fg='black')
        self.label_apellidoNiño.config(font=('Times New Roman', 12, 'bold'))
        self.label_apellidoNiño.grid(row=2,column=0, padx=10, pady=7)
        
        self.label_edadNiño= tk.Label(self, text='Edad: ', fg='black')
        self.label_edadNiño.config(font=('Times New Roman', 12, 'bold'))
        self.label_edadNiño.grid(row=3,column=0, padx=10, pady=7)
        
        self.label_generoNiño= tk.Label(self, text='Genero: ', fg='black')
        self.label_generoNiño.config(font=('Times New Roman', 12, 'bold'))
        self.label_generoNiño.grid(row=4,column=0, padx=10, pady=7)
        
        self.label_comunidadNiño= tk.Label(self, text='Comunidad: ', fg='black')
        self.label_comunidadNiño.config(font=('Times New Roman', 12, 'bold'))
        self.label_comunidadNiño.grid(row=1,column=2, padx=10, pady=7)
        #campos entrada
        self.recoger_nombre= tk.StringVar()
        self.entry_nombreNiño=tk.Entry(self,textvariable=self.recoger_nombre)
        self.entry_nombreNiño.config(width=30,font=('Times New Roman', 12))
        self.entry_nombreNiño.grid(row=1, column=1, padx=10, pady=7)
        
        self.recoger_apellido= tk.StringVar()
        self.entry_apellidoNiño=tk.Entry(self, textvariable=self.recoger_apellido)
        self.entry_apellidoNiño.config(width=30,font=('Times New Roman', 12))
        self.entry_apellidoNiño.grid(row=2, column=1, padx=10, pady=7)
        
        self.recoger_edad= tk.StringVar()
        self.entry_edadNiño=tk.Entry(self, textvariable=self.recoger_edad)
        self.entry_edadNiño.config(width=30,font=('Times New Roman', 12))
        self.entry_edadNiño.grid(row=3, column=1, padx=10, pady=7)
        
        self.recoger_genero= tk.StringVar()
        self.entry_generoNiño=tk.Entry(self, textvariable=self.recoger_genero)
        self.entry_generoNiño.config(width=30,font=('Times New Roman', 12))
        self.entry_generoNiño.grid(row=4, column=1, padx=10, pady=7)
        
        self.recoger_comunidad= tk.StringVar()
        self.entry_comunidadNiño=tk.Entry(self, textvariable=self.recoger_comunidad)
        self.entry_comunidadNiño.config(width=30,font=('Times New Roman', 12))
        self.entry_comunidadNiño.grid(row=1, column=4, padx=10, pady=7)

        #botones
        self.boton_Nuevo=tk.Button(self, text='Nuevo', command=self.habilitar_campos_niño)
        self.boton_Nuevo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=5, column=0,padx=10, pady=7)
        
        self.boton_Guardar=tk.Button(self, text='Guardar', command=self.guardar_datos_niño)
        self.boton_Guardar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Guardar.grid(row=5, column=1,padx=10, pady=7)
        
        self.boton_Cancelar=tk.Button(self, text='Cancelar',command=self.deshabilitar_campos_niño)
        self.boton_Cancelar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Cancelar.grid(row=5, column=2,padx=10, pady=7)
        
        #habilitar campos
    def habilitar_campos_niño(self):
        self.recoger_nombre.set('')
        self.recoger_apellido.set('')
        self.recoger_edad.set('')
        self.recoger_genero.set('')
        self.recoger_comunidad.set('')
     
        self.entry_nombreNiño.config(state='normal')
        self.entry_apellidoNiño.config(state='normal')
        self.entry_edadNiño.config(state='normal')
        self.entry_generoNiño.config(state='normal')
        self.entry_comunidadNiño.config(state='normal')
            
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')
    def deshabilitar_campos_niño(self):
        self.id_Niño_Selected=None
        self.recoger_nombre.set('')
        self.recoger_apellido.set('')
        self.recoger_edad.set('')
        self.recoger_genero.set('')
        self.recoger_comunidad.set('')
     
        self.entry_nombreNiño.config(state='disabled')
        self.entry_apellidoNiño.config(state='disabled')
        self.entry_edadNiño.config(state='disabled')
        self.entry_generoNiño.config(state='disabled')
        self.entry_comunidadNiño.config(state='disabled')
            
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')
    def guardar_datos_niño(self):
        niño= Niño(
            Nombre=self.recoger_nombre.get(),
            Apellidos=self.recoger_apellido.get(),
            Edad=self.recoger_edad.get(),
            Genero=self.recoger_genero.get(),
            Comunidad=self.recoger_comunidad.get()
        )
        if self.id_Niño_Selected==None:
            guardar_Niño(niño)
        else:
            editar_Niño(niño, self.id_Niño_Selected)
        self.tabla_niños()
        self.deshabilitar_campos_niño()
    def tabla_niños(self):
        self.lista_nin= listar_Niño()
        
        self.tabla_Niño= ttk.Treeview(self,columns=('Nombre', 'Apellido','Edad','Genero','Comunidad'))
        self.tabla_Niño.grid(row=6, column=0 ,columnspan=5)
        self.tabla_Niño.column('#0', width=100)
        self.tabla_Niño.column('Nombre', width=120)
        self.tabla_Niño.column('Apellido', width=120)
        self.tabla_Niño.column('Edad', width=100)
        self.tabla_Niño.column('Genero', width=120)
        self.tabla_Niño.column('Comunidad', width=150)
        #scrollbar
        self.scroll_Niño= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Niño.yview)
        self.scroll_Niño.grid(row=6,column=4,sticky='nse')
        self.tabla_Niño.config(yscrollcommand=self.scroll_Niño.set)
        #textos columnas
        self.tabla_Niño.heading('#0',text='CODIGO')
        self.tabla_Niño.heading('#1',text='NOMBRE')
        self.tabla_Niño.heading('#2',text='APELLIDO')
        self.tabla_Niño.heading('#3',text='EDAD')
        self.tabla_Niño.heading('#4',text='GENERO')
        self.tabla_Niño.heading('#5',text='COMUNIDAD')

        ##iterar lista
        for p in self.lista_nin:
            self.tabla_Niño.insert('',0, text=p[0],
                                  values= (p[1], p[2],p[3],p[4],p[5]))
        #otros botones
        self.boton_Editar=tk.Button(self, text='Editar', command=self.editar_Niño)
        self.boton_Editar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_Editar.grid(row=8, column=1,padx=10, pady=7)
        
        self.boton_Eliminar=tk.Button(self, text='Eliminar',command=self.eliminar_datos_Niño)
        self.boton_Eliminar.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_Eliminar.grid(row=8, column=2,padx=10, pady=7)
        
        self.boton_BuscarKey=tk.Button(self, text='Comunidad',command=self.buscar_datos_Niño)
        self.boton_BuscarKey.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_BuscarKey.grid(row=8, column=0,padx=10, pady=7)
    def editar_Niño(self):
        try:
            self.id_Niño_Selected=self.tabla_Niño.item(self.tabla_Niño.selection())['text']
            self.Nombre_Niño_Selected=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][0]
            self.Apellidos_Niño_Selected=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][1]
            self.Edad_Niño_Selected=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][2]
            self.Genero_Niño_Selected=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][3]
            self.Comunidad_Niño_Selected=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][4]
            self.habilitar_campos_niño()
            self.entry_nombreNiño.insert(0,self.Nombre_Niño_Selected)
            self.entry_apellidoNiño.insert(0,self.Apellidos_Niño_Selected)
            self.entry_edadNiño.insert(0,self.Edad_Niño_Selected)
            self.entry_generoNiño.insert(0,self.Genero_Niño_Selected)
            self.entry_comunidadNiño.insert(0,self.Comunidad_Niño_Selected)
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n modificado en la base de datos"
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos_Niño(self):
        try:
            self.id_Niño_Selected=self.tabla_Niño.item(self.tabla_Niño.selection())['text']
            eliminar_Niño(self.id_Niño_Selected)
            self.tabla_niños()
            self.id_Niño_Selected=None
        except:
            titulo="Modificacion Fallida "
            mensaje="El registro no pudo ser \n eliminado en la base de datos"
            messagebox.showerror(titulo, mensaje)
            
    def buscar_datos_Niño(self):
        self.id_com_Selected_Buscar=self.tabla_Niño.item(
                self.tabla_Niño.selection())['values'][4]
        try:
            self.lista_com= buscar_com_niño(self.id_com_Selected_Buscar)
            message=f"""COMUNIDAD: ----\nID: {self.lista_com[0]} --{self.lista_com[1]} \nETNIA: {self.lista_com[2]}\nREPRESENTANTE: {self.lista_com[3]}"""
            titulo="Busqueda: "
            messagebox.showinfo(titulo, message)
        except:
            titulo="Conexion al registro: "
            mensaje= "Sellecione una tupla!!!"
            messagebox.showerror(titulo, mensaje)