#!C:\Users\Jiro\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector

class Connection():   
       
        def __init__(self, host, user, pwd,dbase):    
                self.host = host
                self.user = user
                self.pwd = pwd
                self.dbase = dbase
                
        def connect(self): 
                mydb = mysql.connector.connect(host=self.host,user=self.user,passwd=self.pwd,database=self.dbase)
                return mydb