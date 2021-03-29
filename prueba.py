import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import conexionbasedato as conec
from tkinter import scrolledtext as st


class formulario():
    def __init__(self):
        self.so= conec.Socios()
        self.w=tk.Tk()
        self.w.title("Formulario Club")
        self.w.geometry("600x500")
        self.engloba = ttk.Notebook(self.w)
        self.engloba.grid(row=0, column=0,padx=10, pady=10)
        self.crear_solapa_socio_cuota()
        self.crear_solapa_mostrarlistado()
        self.crear_Solapa_Buscar_Letra_Nombre()
        self.nombre_A_Buscar()
        self.w.mainloop()


    def crear_solapa_socio_cuota(self):
        self.pagina1=ttk.Frame(self.engloba)
        self.engloba.add(self.pagina1, text="Carga de socios")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Socio")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        

        self.label1=tk.Label(self.labelframe1, text= "Nombre")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.label2=tk.Label(self.labelframe1,text= "Cuota")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.carganombre= tk.StringVar()
        self.entrynombre=tk.Entry(self.labelframe1, textvariable= self.carganombre)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        
        self.cargacuota=tk.StringVar()
        self.entrycargacuota=tk.Entry(self.labelframe1, textvariable= self.cargacuota)
        self.entrycargacuota.grid (column=1, row=1, padx=4, pady=4)

        self.button1=ttk.Button(self.pagina1, text="confirmar", command= self.agregarSocioCuota)
        self.button1.grid(column=0, row=1, padx=4, pady=4)

    def crear_solapa_mostrarlistado(self):
        self.pagina2=ttk.Frame(self.engloba)
        self.engloba.add(self.pagina2, text= "Consultar Listado de socios")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="listado de socio")
        self.labelframe2.pack()

        self.boton1=ttk.Button(self.labelframe2, text="Ver listado completo", command=self.devolverlistado)
        self.boton1.pack()

        self.tabla = ttk.Treeview(self.labelframe2, columns = ("Nombre", "cuota"))
        self.tabla.pack()
        self.tabla.heading("#0",text= "Id")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("cuota", text = "cuota")
        
    def devolverlistado(self):
        a_borrar = self.tabla.get_children()
        for i in a_borrar:

            self.tabla.delete(i) 

        respuesta = self.so.mostrarlistadosocio()
        
        for i in respuesta:

            self.tabla.insert("", END, text= i[0], values = (i[1], i[2]))    
        
    def crear_Solapa_Buscar_Letra_Nombre(self):
        self.pagina3=ttk.Frame(self.engloba)
        self.engloba.add(self.pagina3, text= "Buscar Socio")
        self.labelframe3= LabelFrame(self.pagina3,text="Buscar por letra de nombre")
        # self.labelframe3.grid(column=0, row=0, padx=5, pady=10)       
        self.labelframe3.pack()
        self.label3= tk.Label(self.labelframe3, text=" Poner la primera letra del nombre del socio a buscar")
        # self.label3.grid(column=0, row=0, padx=4, pady=4)
        self.label3.pack()
        self.letra_nombre_a_buscar= tk.StringVar()
        self.entry_letra_nombre_a_buscar=tk.Entry(self.labelframe3, textvariable= self.letra_nombre_a_buscar)
    #     self.entry_letra_nombre_a_buscar.grid(column=1, row=0, padx=4, pady=4)
        self.entry_letra_nombre_a_buscar.pack()
        self.boton3=ttk.Button(self.labelframe3, text="Ver listado completo", command=self.nombre_A_Buscar)
        self.boton3.pack()

        
        def nombre_A_Buscar(self):
            pass
        #     lista = self.so.mostrarlistadosocio()
            # for i in lista:
            #     if i == self.letra_nombre_a_buscar:
            #         print(hola)


        
        
        
        # self.tabla2 = ttk.Treeview(self.labelframe3, columns = ("Nombre", "cuota"))
        # self.tabla2.pack()
        # self.tabla2.heading("#0",text= "Id")
        # self.tabla2.heading("Nombre", text="Nombre")
        # self.tabla2.heading("cuota", text = "cuota")


    # def fetchall(self):
    #     respuesta = self.so.mostrarlistadosocio()
    #     self.scrolledtext.delete('1.0', tk.END)

    #     for tupla in respuesta:
    #         #currentText = self.scrolledtext.get('1.0', tk.END)
    #         self.scrolledtext.insert( tk.END, '\nID:'+ str(tupla[0]) 
    #                                          +'\nNombre:' + tupla[1]
    #                                          +'\nCuota:'  + tupla[2]
    #                                          +'\n')
        





    def agregarSocioCuota(self):
        datos = (self.carganombre.get(), self.cargacuota.get())
        self.so.alta(datos)

        self.carganombre.set("")
        self.cargacuota.set("")




form1=formulario()

# tuplatest=(5, "dada" )
# form1.so.alta(tuplatest)

# tuplatest=(4, "tete" )
# form1.so.alta(tuplatest)

# tuplatest=(3, "yryr" )
# form1.so.alta(tuplatest)

# tuplatest=(2, "jgjg" )
# form1.so.alta(tuplatest)