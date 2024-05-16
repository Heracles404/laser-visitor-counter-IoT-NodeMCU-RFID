#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector
import sys
sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")

from Queries import *

class MyView1(): 
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
                    background-color: #f4f4f4;
                }
                .container {
                    text-align: center;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    margin-bottom: 20px;
                }
                form {
                    margin-bottom: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid #000;
                }
                th, td {
                    padding: 10px;
                    text-align: center;
                }
                input[type="text"] {
                    padding: 5px;
                    margin-right: 10px;
                }
                input[type="submit"] {
                    padding: 5px 10px;
                    border: none;
                    border-radius: 5px;
                    background-color: #007BFF;
                    color: white;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                input[type="button"] {
                    padding: 5px 10px;
                    border: none;
                    border-radius: 5px;
                    background-color: #28a745;
                    color: white;
                    cursor: pointer;
                }
                input[type="button"]:hover {
                    background-color: #218838;
                }
            </style>
            <script>
                function confirmReset() {
                    return confirm('Are you sure you want to reset the form?');
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
                    <label for='visitor_id'>Search Visitor Number: </label>
                    <input type='text' id='visitor_id' name='visitor_id'>
                    <input type='submit' name='search' value='SEARCH'/>
                    <input type='submit' name='clear' value='RESET' onclick='return confirmReset()'/>
                    <input type='button' value='HOME' onclick='goHome()'/>
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
            </div>
        </body>
        </html>""")

class MyView2(): 
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
                    background-color: #f4f4f4;
                }
                .container {
                    text-align: center;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    margin-bottom: 20px;
                }
                form {
                    margin-bottom: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid #000;
                }
                th, td {
                    padding: 10px;
                    text-align: center;
                }
                input[type="text"] {
                    padding: 5px;
                    margin-right: 10px;
                }
                input[type="submit"] {
                    padding: 5px 10px;
                    border: none;
                    border-radius: 5px;
                    background-color: #007BFF;
                    color: white;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                input[type="button"] {
                    padding: 5px 10px;
                    border: none;
                    border-radius: 5px;
                    background-color: #28a745;
                    color: white;
                    cursor: pointer;
                }
                input[type="button"]:hover {
                    background-color: #218838;
                }
            </style>
            <script>
                function confirmReset() {
                    return confirm('Are you sure you want to reset the form?');
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
                    <label for='visitor_id'>Search Visitor Number: </label>
                    <input type='text' id='visitor_id' name='visitor_id'>
                    <input type='submit' name='search' value='SEARCH'/>
                    <input type='submit' name='clear' value='RESET' onclick='return confirmReset()'/>
                    <input type='button' value='HOME' onclick='goHome()'/>
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
            </div>
        </body>
        </html>""")
