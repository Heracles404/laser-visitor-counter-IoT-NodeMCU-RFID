#!C:\Python\python.exe
import mysql.connector

import sys
sys.path.append("D:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
from Connection import Connection

# this is the class to get ALL records
class MyQuery1():   
    def showAll(self): 
        conn = Connection("localhost", "root", "", "visitor")
        mydb = conn.connect()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM counter")
        myresult = mycursor.fetchall()
        return myresult

# this is the class to search a record given a posted value of visitor_ID              
class MyQuery2():   
    def __init__(self, visitor_id):    
        self.visitor_id = visitor_id               

    def searchN(self): 
        conn = Connection("localhost", "root", "", "visitor")
        mydb = conn.connect()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM counter WHERE visitor_ID = %s", (self.visitor_id,))
        myresult = mycursor.fetchall()
        return myresult
    
class MyClearDatabase():
    def clearAll(self):
        conn = Connection("localhost", "root", "", "visitor")
        mydb = conn.connect()
        mycursor = mydb.cursor()
        sql = "TRUNCATE TABLE counter"
        mycursor.execute(sql)
        mydb.commit()

        #result = mycursor.rowcount, "All Records Deleted!"
        #return result
