#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector
import sys
sys.path.append("D:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")

from Queries import *

class MyView1: 
    def __init__(self, results):    
        self.results = results 
    
    def viewAll(self):
        print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Visitor Counter Data</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #e0f7fa;
                }
                .container {
                    text-align: center;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    margin-bottom: 20px;
                    color: #00796b;
                }
                form {
                    margin-bottom: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: center;
                }
                th {
                    background-color: #00796b;
                    color: white;
                }
                td {
                    background-color: #e0f7fa;
                }
                input[type="text"] {
                    padding: 10px;
                    margin-right: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
                input[type="submit"], input[type="button"] {
                    padding: 10px 15px;
                    border: none;
                    border-radius: 5px;
                    color: white;
                    cursor: pointer;
                }
                input[type="submit"].search {
                    background-color: #00796b;
                }
                input[type="submit"].reset {
                    background-color: #648c11    ;
                }
                input[type="button"].home {
                    background-color: #388e3c;
                }
                input[type="submit"].clear {
                    background-color: #00796b;
                }
                input[type="submit"]:hover, input[type="button"]:hover {
                    opacity: 0.9;
                }
            </style>
            <script>
                function confirmReset() {
                    return confirm('Are you sure you want to reset?');
                }
                function goHome() {
                    window.location.href = 'http://localhost/laser-visitor-counter-IoT-NodeMCU-RFID/'; 
                }
            </script>
        </head>
        <body>
            <div class="container">
                <h1>Visitor Counter Data</h1>
                <form action='/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/controller/Controller.py' method='post'>
                    <label for='visitor_id'>Search by Visitor Number: </label>
                    <input type='text' id='visitor_id' name='visitor_id'>            
                    <input type='submit' class='search' name='search' value='SEARCH'/>
                    <input type='submit' class='clear' name='clear_search' value='CLEAR'/>
                    <input type='submit' class='reset' name='clear' value='DELETE' onclick='return confirmReset()'/>
                </form>
                <table>
                    <tr>
                        <th>#</th>
                        <th>Time</th>
                        <th>Date</th>
                    </tr>""")
        
        for row in self.results:
            print(f"""
                    <tr>
                        <td>{row["visitor_ID"]}</td>
                        <td>{row["time"]}</td>
                        <td>{row["date"]}</td>
                    </tr>""")
        
        print("""
                </table>
            <br></br>
            <input type='button' class='home' value='HOME' onclick='goHome()'/>      
            </div>
        
        </body>
        </html>""")

class MyView2: 
    def __init__(self, results):    
        self.results = results 
    
    def viewSearched(self):
        print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Visitor Counter Data</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #e0f7fa;
                }
                .container {
                    text-align: center;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    margin-bottom: 20px;
                    color: #00796b;
                }
                form {
                    margin-bottom: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: center;
                }
                th {
                    background-color: #00796b;
                    color: white;
                }
                td {
                    background-color: #e0f7fa;
                }
                input[type="text"] {
                    padding: 10px;
                    margin-right: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
                input[type="submit"], input[type="button"] {
                    padding: 10px 15px;
                    border: none;
                    border-radius: 5px;
                    color: white;
                    cursor: pointer;
                }
                input[type="submit"].search {
                    background-color: #00796b;
                }
                input[type="submit"].reset {
                    background-color: #648c11    ;
                }
                input[type="button"].home {
                    background-color: #388e3c;
                }
                input[type="submit"].clear {
                    background-color: #00796b;
                }
                input[type="submit"]:hover, input[type="button"]:hover {
                    opacity: 0.9;
                }
            </style>
            <script>
                function confirmReset() {
                    return confirm('Are you sure you want to reset?');
                }
                function goHome() {
                    window.location.href = 'http://localhost/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/'; 
                }
            </script>
        </head>
        <body>
            <div class="container">
                <h1>Visitor Counter Data</h1>
                <form action='/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/controller/Controller.py' method='post'>
                    <label for='visitor_id'>Search by Visitor Number: </label>
                    <input type='text' id='visitor_id' name='visitor_id'>            
                    <input type='submit' class='search' name='search' value='SEARCH'/>
                    <input type='submit' class='clear' name='clear_search' value='CLEAR'/>
                    <input type='submit' class='reset' name='clear' value='DELETE' onclick='return confirmReset()'/>
                </form>
                <table>
                    <tr>
                        <th>#</th>
                        <th>Time</th>
                        <th>Date</th>
                    </tr>""")
        
        for row in self.results:
            print(f"""
                    <tr>
                        <td>{row["visitor_ID"]}</td>
                        <td>{row["time"]}</td>
                        <td>{row["date"]}</td>
                    </tr>""")
        
        print("""
                </table>
            <br></br>
            <input type='button' class='home' value='HOME' onclick='goHome()'/>
            </div>       
        </body>
        </html>""")
