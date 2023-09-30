import tkinter as tk

from Interfaz.Interfaz_Tablas import Frame_Principal,barra_menu

def main():
    root= tk.Tk()
    root.title("Base de datos: Fundacion ")
    root.iconbitmap('iconos/iconoP.ico')
    root.resizable(0,0)
    barra_menu(root)
    
    app= Frame_Principal(root=root)
    app.mainloop()

if __name__=='__main__':
    main()
    