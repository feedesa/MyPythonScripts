import pymysql

class Socios():
    def abrir(self):
        bbdd= pymysql.connect( host= "localhost", user= "root", passwd="", db= "ejemplo1")
        return bbdd

    def alta(self,datos):
        '''
        datos[0]: id
        datos[1]: nombre
        '''
        bbdd=self.abrir()
        cursor=bbdd.cursor()
        sql = "INSERT INTO SOCIOS ( id, nombre)\
            values( '({})','{}')".format(datos[0],datos[1] )
        print (sql)
        #sql="insert into articulos(descripcion, precio) values (%s,%s)"
        try:
            cursor.execute(sql)
            bbdd.commit()
            #messagebox.showinfo(message = "registro exitoso", title = "Aviso")
        except:
            bbdd.rollback()
            #messagebox.showinfo(message= "No registrado", title = "Aviso" )

        bbdd.close()



    # cursor= bbdd.cursor()
 
    # cursor.execute("CREATE TABLE Socios (id int, NOMBRE VARCHAR(50), NUMERO_DE_SOCIO VARCHAR(2))")

    # cursor.execute ("ALTER TABLE Socios ADD COLUMN SEXO VARCHAR(1)")
