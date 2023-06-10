
#mysql host,user,pasdword data
#...............s3
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'hari9028',
    
)

# prepare a curser object
#...............s4
cursorObject = dataBase.cursor()

#Create a database
#..............s5
cursorObject.execute("CREATE DATABASE harico")

print("All Done!")


