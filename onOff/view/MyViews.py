#!C:\Python\python.exe
import mysql.connector

import sys
sys.path.append("C:/xampp/htdocs/IT123P/model/")

from MyQueries import *



class MyView1(): 

    def __init__(self,results):    
        self.results = results 
    
    def viewAll(self):
        
        print("<html>")
        print("<body>")
        print("<center>")
        print("<h1>My Sample SEMI-MVC</h1>")
       
        print("<form action='/IT123P/controller/MyController.py' method='post'>")
        print("Enter name: <input type='text' name ='name'>")
        print("<input type ='submit' name ='search' value = 'SEARCH'/>")
        print("</form>")
        
        print("<table border='1'>")
        print("<tr>")
        print("<th>StudID</th>")
        print("<th>Name</th>")
        print("<th>Course</th>")
        print("<th>Address</th>")
        print("</tr>")
        
      
 
        for row in self.results:
          print("<tr>")
          print("<td>" ,row["StudID"], "</td>")
          print("<td>" ,row["StudName"], "</td>")
          print("<td>" ,row["Course"], "</td>")
          print("<td>" ,row["Age"], "</td>")
          print("</tr>")
           
        
        print("</table>")
        print("</body>")
        print("</center>")
        print("</html>")
 

class MyView2(): 
    def __init__(self,results):    
        self.results = results 
    def viewSearched(self):
        
        print("<html>")
        print("<body>")
        print("<center>")
        print("<h1>My Sample SEMI-MVC</h1>")
       
        print("<form action='/IT123P/controller/MyController.py' method='post'>")
        print("Enter name: <input type='text' name ='name'>")
        print("<input type ='submit' name ='search' value = 'SEARCH'/>")
        print("</form>")
        
        print("<table border='1'>")
        print("<tr>")
        print("<th>StudID</th>")
        print("<th>Name</th>")
        print("<th>Course</th>")
        print("<th>Address</th>")
        print("</tr>")
       
 
        for row in self.results:
          print("<tr>")
          print("<td>" ,row["StudID"], "</td>")
          print("<td>" ,row["StudName"], "</td>")
          print("<td>" ,row["Course"], "</td>")
          print("<td>" ,row["Age"], "</td>")
          print("</tr>")
            
        
        print("</table>")
        print("</body>")
        print("</center>")
        print("</html>")
 

 



