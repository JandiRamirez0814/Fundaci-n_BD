import tkinter as tk

from Interfaz.Interfaz_Representantes import barra_menu_repre,Frame_Repre
from Interfaz.Interfaz_Comunidades import barra_menu_com,Frame_Com
from Interfaz.Interfaz_Profesionales import barra_menu_pro,Frame_Pro
from Interfaz.Interfaz_Administrativos import barra_menu_admi,Frame_Admi
from Interfaz.Interfaz_Proyectos import barra_menu_proy,Frame_Proy
from Interfaz.Interfaz_Ninos import barra_menu_niño,Frame_Niño
from Interfaz.Interfaz_ParticipantesProyecto import barra_menu_partiproy,Frame_PartiPro
from Interfaz.Interfaz_ComunidadesBeneficiadas import barra_menu_comben,Frame_ComBen
from Interfaz.Interfaz_Objetivos import barra_menu_objetivo,Frame_Obj
from Interfaz.Interfaz_ProyectosObjetivos import barra_menu_proobj,Frame_ProObj
from Interfaz.vista1 import barra_menu_vista1,Frame_Vista1
from Interfaz.vista2 import barra_menu_vista2,Frame_Vista2



def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu= barra_menu, width=300, height=300)
    """creo menus"""
    menu_in= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='MENU PRINCIPAL', menu = menu_in)
    menu_in.add_command(label='Salir',font=('Times New Roman', 12, 'bold'), command=root.destroy)
    
class Frame_Principal(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=600, height=320)
        self.root=root
        self.pack()
        self.campos_Principal()
    def campos_Principal(self):
        #labels
        self.label_1= tk.Label(self, text='TABLAS: ', fg='black')
        self.label_1.config(font=('Times New Roman', 12, 'bold'))
        self.label_1.grid(row=0,column=0, padx=10, pady=7)
        
        self.label_2= tk.Label(self, text='CONSULTAS: ', fg='black')
        self.label_2.config(font=('Times New Roman', 12, 'bold'))
        self.label_2.grid(row=5,column=0, padx=10, pady=7)
        #creo botones
        self.boton_Comunidad=tk.Button(self, text='COMUNIDAD', command=llamar_Comunidad)
        self.boton_Comunidad.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Comunidad.grid(row=1, column=0,padx=10, pady=7)
        
        self.boton_Representate=tk.Button(self, text='REPRESENTANTE', command=llamar_Representante)
        self.boton_Representate.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Representate.grid(row=2, column=0,padx=10, pady=7)
        
        self.boton_Niño=tk.Button(self, text='NIÑO', command=llamar_Niño)
        self.boton_Niño.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Niño.grid(row=3, column=0,padx=10, pady=7)
        
        self.boton_Proyecto=tk.Button(self, text='PROYECTO', command=llamar_Proyecto)
        self.boton_Proyecto.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Proyecto.grid(row=1, column=1,padx=10, pady=7)
        
        self.boton_Objetivo=tk.Button(self, text='OBJETIVO', command=llamar_Objetivo)
        self.boton_Objetivo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Objetivo.grid(row=2, column=1,padx=10, pady=7)
        
        self.boton_ProProy=tk.Button(self, text='PRO-ACTIVOS', command=llamar_PartiPro)
        self.boton_ProProy.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_ProProy.grid(row=3, column=1,padx=10, pady=7)
        
        self.boton_Profesional=tk.Button(self, text='PROFESIONAL', command=llamar_Profesional)
        self.boton_Profesional.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Profesional.grid(row=1, column=2,padx=10, pady=7)
        
        self.boton_Administrativo=tk.Button(self, text='ADMINISTRATIVO', command=llamar_Administrativo)
        self.boton_Administrativo.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_Administrativo.grid(row=2, column=2,padx=10, pady=7)
        
        self.boton_ComBen=tk.Button(self, text='CO-BENEFICIADA', command=llamar_ComBen)
        self.boton_ComBen.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_ComBen.grid(row=3, column=2,padx=10, pady=7)
        
        self.boton_ProObj=tk.Button(self, text='PRO-OBJETIVOS', command=llamar_ProObj)
        self.boton_ProObj.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='green', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_ProObj.grid(row=4, column=0,padx=10, pady=7)
        
        self.boton_VISTA1=tk.Button(self, text='PORCENTAJE-PRO',command=llamar_vista1)
        self.boton_VISTA1.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_VISTA1.grid(row=6, column=0,padx=10, pady=7)
        
        self.boton_VISTA2=tk.Button(self, text='CANT-NIÑOS',command=llamar_vista2)
        self.boton_VISTA2.config(width=15, font=('Times New Roman', 12, 'bold'),
                                fg='white', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_VISTA2.grid(row=6, column=1,padx=10, pady=7)
        

def llamar_Comunidad():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_com(root1)
    app= Frame_Com(root=root1)
    app.mainloop()
    
def llamar_Representante():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_repre(root1)
    app= Frame_Repre(root=root1)
    app.mainloop()

def llamar_Profesional():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_pro(root1)
    app= Frame_Pro(root=root1)
    app.mainloop()
    
def llamar_Administrativo():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_admi(root1)
    app= Frame_Admi(root=root1)
    app.mainloop()
    
def llamar_Proyecto():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_proy(root1)
    app= Frame_Proy(root=root1)
    app.mainloop()

def llamar_Niño():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_niño(root1)
    app= Frame_Niño(root=root1)
    app.mainloop()
    
def llamar_PartiPro():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_partiproy(root1)
    app= Frame_PartiPro(root=root1)
    app.mainloop()
    
def llamar_ComBen():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_comben(root1)
    app= Frame_ComBen(root=root1)
    app.mainloop()
    
def llamar_Objetivo():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_objetivo(root1)
    app= Frame_Obj(root=root1)
    app.mainloop()
    
def llamar_ProObj():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_proobj(root1)
    app= Frame_ProObj(root=root1)
    app.mainloop()
    
def llamar_vista1():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_vista1(root1)
    app= Frame_Vista1(root=root1)
    app.config(bg='green')
    app.mainloop()

def llamar_vista2():
    root1= tk.Toplevel()
    root1.title("Base de datos: Fundacion ")
    root1.iconbitmap('iconos/iconoP.ico')
    
    barra_menu_vista2(root1)
    app= Frame_Vista2(root=root1)
    app.config(bg='green')
    app.mainloop()