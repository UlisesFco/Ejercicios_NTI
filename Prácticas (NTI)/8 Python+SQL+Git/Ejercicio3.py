import mysql.connector
import Ejercicio2

def etiqueta_ubicacion(n,mydb,label):
    numReg = 3*n
    cursor1 = mydb.cursor()
    cursor1.execute("select max(id) from taglogs.tagmessages")
    for x in cursor1:
        idReg = x[0]
    cursor2=mydb.cursor()
    mensaje ='#Team3#'
    cursor2.execute("insert into taglogs.messagelogs \
        (location) values ('%s') \
        where id between %d and %d",mensaje,idReg-3*n,idReg)
    mydb.commit()
    

mydb = mysql.connector.connect(
    host="148.205.37.150",
    user="team3",
    passwd="team3nti#",
    database = "taglogs"
)
#mycursor = mydb.cursor()
n = main()
etiqueta_ubicacion(3,mycursor)