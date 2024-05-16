#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector

import sys
sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
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

# this is the class to add a record as performed by MyAddRecordBootstrap                
class MyAddRecord():  
    def __init__(self, visitor_id, time, date):    
        self.visitor_id = visitor_id  
        self.time = time
        self.date = date   

    def addRec(self): 
        conn = Connection("localhost", "root", "", "visitor")
        mydb = conn.connect()
        mycursor = mydb.cursor()
        sql = "INSERT INTO counter (visitor_ID, time, date) VALUES (%s, %s, %s)"
        values = (self.visitor_id, self.time, self.date)
        mycursor.execute(sql, values)
        mydb.commit()
        result = mycursor.rowcount, "Record Added!"  
        return result
