import pymysql
from tkinter import messagebox

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
        sql = "INSERT INTO Socios (NOMBRE, CUOTAPAGA)\
            values('{}','{}')".format(datos[0],datos[1])
        print (sql)

        
        cursor.execute(sql)
        bbdd.commit()
        messagebox.showinfo(message = "registro exitoso", title = "Aviso")
        # except:
        #     bbdd.rollback()
        #     messagebox.showinfo(message= "No registrado", title = "Aviso" )

        bbdd.close()

    def mostrarlistadosocio(self):
        bbdd= self.abrir()
        cursor=bbdd.cursor()
        sql="SELECT * FROM socios"
        
        cursor.execute(sql)
        print(sql)
        datoslistadocompleto= cursor.fetchall()
        bbdd.commit()
        print(datoslistadocompleto)
        bbdd.close()
        for lista in datoslistadocompleto:
            print(lista)
        return lista







    # def editarTabla(self, a_editar):

    #     bbdd= pymysql.connect( host= "localhost", user= "root", passwd="", db= "ejemplo1")


    #     cursor= bbdd.cursor()

    #     sql="ALTER TABLE SOCIOS AUTO_INCREMENT = 1"
        
    #     bbdd.commit()

    #     cursor.execute(sql)

    #     print(sql)

    #     bbdd.close()
        






    
    
    
    
    
    #     sql = "INSERT INTO SOCIOS (nombre, sexo )\
    #         values( '{}','{}')".format(datos[0],datos[1] )
    #     print (sql)
    #     #sql="insert into articulos(descripcion, precio) values (%s,%s)"
    #     try:
    #         cursor.execute(sql)
    #         bbdd.commit()
    #         #messagebox.showinfo(message = "registro exitoso", title = "Aviso")
    #     except:
    #         bbdd.rollback()
    #         #messagebox.showinfo(message= "No registrado", title = "Aviso" )

    #     bbdd.close()


# bbdd= pymysql.connect( host= "localhost", user= "root", passwd="", db= "ejemplo1")


# cursor= bbdd.cursor()
 
# cursor.execute("DELETE FROM SOCIOS WHERE ID= 3")
    

# bbdd.commit()
# bbdd.close()








# bbdd= pymysql.connect( host= "localhost", user= "root", passwd="", db= "ejemplo1")


# cursor= bbdd.cursor()
 
# cursor.execute("ALTER TABLE SOCIOS AUTO_INCREMENT = 1")
    
# # "CREATE TABLE Socios (id INT PRIMARY KEY AUTO_INCREMENT, NOMBRE VARCHAR(50), CUOTAPAGA VARCHAR(2))")

# bbdd.commit()
# bbdd.close()

