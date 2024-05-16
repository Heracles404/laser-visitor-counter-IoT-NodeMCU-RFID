#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector
import sys
sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")

from Queries import *

class MyView1(): 
    def __init__(self, results):    
        self.results = results 
    
    def viewAll(self):
        print("<html>")
        print("<body>")
        print("<center>")
        print("<h1>Visitor Counter Data</h1>")
       
        print("<form action='/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/controller/Controller.py' method='post'>")
        print("Search visitor ID: <input type='text' name='visitor_id'>")
        print("<input type='submit' name='search' value='SEARCH'/>")

        print("</form>")
        
        print("<table border='1'>")
        print("<tr>")
        print("<th>#</th>")
        print("<th>Time</th>")
        print("<th>Date</th>")
        print("</tr>")
        
        for row in self.results:
            print("<tr>")
            print("<td>", row["visitor_ID"], "</td>")
            print("<td>", row["time"], "</td>")
            print("<td>", row["date"], "</td>")
            print("</tr>")
        
        print("</table>")
        print("</body>")
        print("</center>")
        print("</html>")

class MyView2(): 
    def __init__(self, results):    
        self.results = results 
    
    def viewSearched(self):
        print("<html>")
        print("<body>")
        print("<center>")
        print("<h1>Visitor Counter Data</h1>")
       
        print("<form action='/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/controller/Controller.py' method='post'>")
        print("Search visitor ID: <input type='text' name='visitor_id'>")
        print("<input type='submit' name='search' value='SEARCH'/>")

        print("</form>")
        
        print("<table border='1'>")
        print("<tr>")
        print("<th>#</th>")
        print("<th>Time</th>")
        print("<th>Date</th>")
        print("</tr>")
        
        for row in self.results:
            print("<tr>")
            print("<td>", row["visitor_ID"], "</td>")
            print("<td>", row["time"], "</td>")
            print("<td>", row["date"], "</td>")
            print("</tr>")
        
        print("</table>")
        print("</body>")
        print("</center>")
        print("</html>")
