import tkinter as tk
from tkinter import ttk,messagebox
from model.vista1_dao import crear_tabla, borrar_tabla, listar_Vista1
def barra_menu_vista1(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_inicio= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='VISTA1', menu = menu_inicio)
    
    menu_inicio.add_command(label='Nuevo Nueva Vista1',font=('Times New Roman', 12, 'bold'), command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Nueva Vista1',font=('Times New Roman', 12, 'bold'),command=borrar_tabla)
    menu_inicio.add_command(label='Salir Nueva Vista1',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    """
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Ayuda')
    """
  
class Frame_Vista1(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        #root.resizable(0,0)
        self.pack()
        #self.config(bg='blue')
        #seccion comunidades
        #seccion..
        self.tabla_vista1()
    #funciones comunidades
        
    def tabla_vista1(self):
        self.lista_Vista= listar_Vista1()
        
        self.label_1= tk.Label(self, text='PORCENTAJES DE CUMPLIMIENTO: ' , fg='black')
        self.label_1.config(font=('Times New Roman', 12, 'bold'))
        self.label_1.grid(row=1,column=0, padx=10, pady=7)
        
        self.tabla_Vista= ttk.Treeview(self,column=('Codigo', 'Proyecto', 'Suma'))
        self.tabla_Vista.grid(row=5, column=0, columnspan=3, sticky='nse')
        self.tabla_Vista.column('#0', width=100)
        self.tabla_Vista.column('Proyecto', width=200)
        self.tabla_Vista.column('Suma', width=120)        
        #scrollbar
        self.scroll_Com= ttk.Scrollbar(self, orient='vertical', command=self.tabla_Vista.yview)
        self.scroll_Com.grid(row=4,column=4,sticky='nse')
        self.tabla_Vista.config(yscrollcommand=self.scroll_Com.set)
        #textos columnas
        self.tabla_Vista.heading('#0',text='CODIGO')
        self.tabla_Vista.heading('#1',text='PROYECTO')
        self.tabla_Vista.heading('#2',text='SUMA')
        ##iterar lista
        for p in self.lista_Vista:
            self.tabla_Vista.insert('',0, text=p[0],
                                  values= (p[1], p[2]))
    