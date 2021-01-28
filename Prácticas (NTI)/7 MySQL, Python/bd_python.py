import mysql.connector

mydb = mysql.connector.connect(
  host="148.205.37.150",
  user="team3",
  passwd="team3nti#",
  database = "meterlogs"
)
mycursor = mydb.cursor()

#mycursor.execute("SELECT date,time,kwh from logs")

mycursor.execute("select time,date,kwh \
from meterlogs.logs \
where meterlogs.logs.date = str_to_date('2019-02-26','%Y-%m-%d')\
	and meterlogs.logs.time between cast(('21:00:00') as time(0))\
    and cast(('22:00:00') as time(0))")

for x in mycursor:
  print(x)