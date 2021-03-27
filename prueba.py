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

        self.boton1=ttk.Button(self.labelframe2, text="Ver listado completo", command=self.fetchall)
        self.boton1.pack()

        self.scrolledtext= st.ScrolledText(self.labelframe2,width=50, height=10)
        self.scrolledtext.pack()
    
    def fetchall(self):

        respuesta=self.so.mostrarlistadosocio()
        self.scrolledtext.delete('1.0', tk.END)
        self.scrolledtext.insert('1.0', respuesta)

        
        # listado=self.so.mostrarlistadosocio()
        # for fila in listado:
        #     self.scrolledtext1.insert(tk.END, "id:"+str(fila[0])+"\nnombre:"+str(fila)[1]+"\ncuota:"+str(fila[2])+"\n\n")



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