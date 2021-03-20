import pymysql

class Socios:
    def abrir():

    bbdd= pymysql.connect( host= "localhost", user= "root", passwd="", db= "ejemplo1")ef

    def insetar_datos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "INSERT INTO SOCIOS ( id, nombre, SEXO)\
            values( '(0)','(1)','(2)')".format(self.entrynumerodesocio.get(),self.entrynombre.get(),"H" )

            try:
                cursor.execute(sql)
                bbdd.commit()
                messagebox.showinfo(message = "registro exitoso", title = "Aviso")
            except:
                bbdd.rollback()
                messagebox.showinfo(message= "No registrado", title = "Aviso"

                bbdd.close()



    # cursor= bbdd.cursor()
 
    # cursor.execute("CREATE TABLE Socios (id int, NOMBRE VARCHAR(50), NUMERO_DE_SOCIO VARCHAR(2))")

    # cursor.execute ("ALTER TABLE Socios ADD COLUMN SEXO VARCHAR(1)")

    