#!C:\Python\python.exe

import mysql.connector

import sys
sys.path.append("C:/xampp/htdocs/IT123P/model/")
from MyConnection import MyConnection


#this is the class to getALL record
class MyQuery1():   
       
        def showAll(self): 
                conn = MyConnection("localhost","root","","db")
                mydb=conn.connect()
                mycursor = mydb.cursor(dictionary=True)
                mycursor.execute("SELECT * FROM info")
                myresult = mycursor.fetchall()
                
                return myresult
#this is the class to search record given a posted value of name              
class MyQuery2():   
        def __init__(self,name):    
                self.name = name               
        def searchN(self): 
                
                conn = MyConnection("localhost","root","","db")
                mydb=conn.connect()
                mycursor = mydb.cursor(dictionary=True)
                mycursor.execute("SELECT * FROM info WHERE StudName='"+self.name+"'")
                myresult = mycursor.fetchall()
                return myresult
#this is the class to add record as performed by MyAddRecordBoostrap                
class MyAddRecord():  
  
        def __init__(self,studid,studname,degree,age):    
                self.studid = studid  
                self.studname = studname
                self.degree = degree
                self.age = age    
                
        def addRec(self): 
                conn = MyConnection("localhost","root","","db")
                mydb=conn.connect()
                mycursor = mydb.cursor()
                sql = "INSERT INTO info (StudID,StudName,Course,Age) VALUES ('"+ str(self.studid)+"','"+str(self.studname)+"','"+str(self.degree)+"','"+str(self.age)+"')"
                mycursor.execute(sql)
                mydb.commit()
                result=mycursor.rowcount, "Record Added!"  
                return result
               
                          
                
     
