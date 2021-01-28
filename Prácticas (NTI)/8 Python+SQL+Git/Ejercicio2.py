import mysql.connector
import random
import datetime
import time
import sys

def main():
  mydb = mysql.connector.connect(
    host="148.205.37.150",
    user="team3",
    passwd="team3nti#",
    database = "taglogs")
  mycursor = mydb.cursor()
  n=int(sys.argv[1])
  for i in range(n):
    secuencia = random.randint(0,255)
    aux = str(datetime.datetime.now())
    fecha = aux.split(' ')
    rssiGenerado1 = random.randint(-100,-50)
    sentencia1 = "insert into taglogs.tagmessages (tag,node,sequence,date,time,rssi) values ('EB03','0002',"+str(secuencia)+",'"+fecha[0]+"','"+fecha[1][:8]+"','"+str(rssiGenerado1)+"')"
    print(sentencia1)
    mycursor.execute(sentencia1)
    rssiGenerado2 = random.randint(-100,-50)
    sentencia2 = "insert into taglogs.tagmessages (tag,node,sequence,date,time,rssi) values ('EB03','0005',"+str(secuencia)+",'"+fecha[0]+"','"+fecha[1][:8]+"','"+str(rssiGenerado2)+"')"
    print(sentencia2)
    mycursor.execute(sentencia2)
    rssiGenerado3 = random.randint(-100,-50)
    sentencia3 = "insert into taglogs.tagmessages (tag,node,sequence,date,time,rssi) values ('EB03','0014',"+str(secuencia)+",'"+fecha[0]+"','"+fecha[1][:8]+"','"+str(rssiGenerado3)+"')"
    print(sentencia3)
    mycursor.execute(sentencia3)
    mydb.commit()
    time.sleep(3)
  mycursor.close()
  mydb.close()
  return n

main()