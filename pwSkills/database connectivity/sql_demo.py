import mysql.connector as connector

mydb = connector.connect(
    host="localhost",
    user="root",
    password="69420",
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor :
    print(x)