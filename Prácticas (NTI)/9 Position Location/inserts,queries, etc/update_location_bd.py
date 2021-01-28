import mysql.connector
#import Ejercicio2

def etiqueta_ubicacion(n,mydb,msg):
    numReg = 3*n
    #cursor1 = mydb.cursor()
    #cursor1.execute("select max(id) from taglogs.tagmessages")
    #for x in cursor1:
    #    idReg = x[0]
    cursor2=mydb.cursor()
    cursor2.execute("\
        update taglogs.tagmessages set location = '" + msg + "' \
        where taglogs.tagmessages.date = str_to_date('2019-03-13','%Y-%m-%d') \
	    and taglogs.tagmessages.time >= cast(('11:50:00') as time(0)) and tag = 'EB03' \
        limit 60")
    mydb.commit()
    

mydb = mysql.connector.connect(
    host="148.205.37.150",
    user="team3",
    passwd="team3nti#",
    database = "taglogs"
)
#mycursor = mydb.cursor()
#n = Ejercicio2.main()
etiqueta_ubicacion(60/3,mydb,'F1')