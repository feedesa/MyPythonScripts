import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import conexionbasedato as conec


class formulario():
    def __init__(self):
        self.so= conec.Socios()
        self.w=tk.Tk()
        self.w.title("Formulario Club")
        self.w.geometry("600x500")
        self.engloba = ttk.Notebook(self.w)
        self.engloba.grid(row=0, column=0,padx=10, pady=10)
        # self.crear_solapa_consultasocio()
        self.crear_solapa_socio_cuota()
        # # self.listado_completo_socio()
        # self.crear_solapa_cuota()
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

    # def crear_solapa_cuota(self):
    #     self.pagina2=ttk.Frame(self.engloba)
    #     self.engloba.add(self.pagina2, text= "Cuota")
    #     self.labelframe2=ttk.LabelFrame(self.pagina2, text="Socio")
    #     self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

    #     self.labelCS=tk.Label(self.labelframe2, text="Nombre de socio")
    #     self.labelCS.grid(column=0, row=0, padx=4, pady=4)



    #     self.labelCS1=tk.Label(self.labelframe2,text= "pago de cuota")
    #     self.labelCS1.grid(column=0, row=1, padx=4, pady=4)


    #     self.string_socio= tk.StringVar()
    #     self.entry_socio=tk.Entry(self.labelframe2, textvariable= self.string_socio)
    #     self.entry_socio.grid(column=1, row=0, padx=4, pady=4)

    #     self.pagocuota=tk.StringVar()
    #     self.entrypagocuota=tk.Entry(self.labelframe2, textvariable= self.pagocuota)
    #     self.entrypagocuota.grid (column=1, row=1, padx=4, pady=4)

    #     self.button2=ttk.Button(self.pagina2, text="buscar", command=self.agregarSocioCuota)
    #     self.button2.grid(column=0, row=1, padx=4, pady=4)




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