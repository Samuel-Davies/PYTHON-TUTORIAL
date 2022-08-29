# first import the connector

import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root" , passwd = "yours1234", database = "yours",auth_plugin='mysql_native_password')

#fetching all the values in the database
mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
    print(i)