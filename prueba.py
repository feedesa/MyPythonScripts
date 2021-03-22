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
        # # self.listado_completo_socio()
        self.crear_solapa_socio()
        # self.w.mainloop()


    def crear_solapa_socio(self):
        self.pagina1=ttk.Frame(self.engloba)
        self.engloba.add(self.pagina1, text="Carga de socios")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Socio")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        

        self.label1=tk.Label(self.labelframe1, text= "Nombre")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.label2=tk.Label(self.labelframe1,text= "numero de socio")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.carganombre= tk.StringVar()
        self.entrynombre=tk.Entry(self.labelframe1, textvariable= self.carganombre)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        
        self.carganrosocio=tk.StringVar()
        self.entrynumerodesocio=tk.Entry(self.labelframe1, textvariable= self.carganrosocio)
        self.entrynumerodesocio.grid (column=1, row=1, padx=4, pady=4)

        self.button1=ttk.Button(self.pagina1, text="confirmar", command= self.agregarSocio)
        self.button1.grid(column=0, row=1, padx=4, pady=4)


#     def crear_solapa_consultasocio(self):
#         self.pagina2=ttk.Frame(self.engloba)
#         self.engloba.add(self.pagina2, text= "consulta de socio")
#         self.labelframe2=ttk.LabelFrame(self.pagina2, text="Socio")
#         self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

#         self.labelCS=tk.Label(self.labelframe2, text="numero de socio")
#         self.labelCS.grid(column=0, row=0, padx=4, pady=4)



#         self.labelCS1=tk.Label(self.labelframe2,text= "pago de couta")
#         self.labelCS1.grid(column=0, row=1, padx=4, pady=4)


#         self.numerodesocio= tk.StringVar()
#         self.entrynumerosocio=tk.Entry(self.labelframe2, textvariable= self.numerodesocio)
#         self.entrynumerosocio.grid(column=1, row=0, padx=4, pady=4)

#         self.pagocuota=tk.StringVar()
#         self.entrypagocuota=tk.Entry(self.labelframe2, textvariable= self.pagocuota)
#         self.entrypagocuota.grid (column=1, row=1, padx=4, pady=4)

#         self.button2=ttk.Button(self.pagina2, text="buscar")
#         self.button2.grid(column=0, row=1, padx=4, pady=4)


#     def listado_completo_socio(self):
#         self.pagina3=ttk.Frame(self.engloba)
#         self.engloba.add(self.pagina3, text= "listado de socio")

#         self.labelframe3=ttk.LabelFrame(self.pagina3, text="Socio")
#         self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

#         self.labellcs = tk.Label(self.labelframe3, text="listado completo de socios")
#         self.labellcs.grid(column=0, row=0, padx=5, pady=10)

    def agregarSocio():
        datos = (self.entrynumerosocio.get(), self.entrynombre.get())
        self.so.alta(datos)

        messagebox.showinfo("informacion", "los datos fueron cargados")
        self.cargasocio.set("")
        self.carganombre.set("")



        



tuplatest=(9, "tereso" )
app=formulario()
app.so.alta(tuplatest)

tuplatest=(5, "dada" )
app.so.alta(tuplatest)

tuplatest=(4, "tete" )
app.so.alta(tuplatest)

tuplatest=(3, "yryr" )
app.so.alta(tuplatest)

tuplatest=(2, "jgjg" )
app.so.alta(tuplatest)