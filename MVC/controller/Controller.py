#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

print("Content-Type: text/html")
print()
import cgi
import sys

form = cgi.FieldStorage()

# so these are data we posted from index 
getALL = form.getvalue("ALL")
searchVisitorID = form.getvalue("visitor_id")
clearDatabase = form.getvalue("clear")
clearSearch = form.getvalue("clear_search")

postedVisitorID = form.getvalue("visitor_ID")
postedTime = form.getvalue("time")
postedDate = form.getvalue("date")

if str(getALL) != "None":

    # controller asks model to show all records
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyQuery1

    query1 = MyQuery1()
    results = query1.showAll()

    # controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from DisplayData import MyView1

    view1 = MyView1(results)
    view1.viewAll()

if str(searchVisitorID) != "None":

    # controller asks model to show all records
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyQuery2

    query2 = MyQuery2(searchVisitorID)
    results = query2.searchN()

    # controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from DisplayData import MyView2

    view1 = MyView2(results)
    view1.viewSearched()

    # Controller updates the view with data obtained from the model
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from DisplayData import MyView4

    view3 = MyView4(results)
    view3.viewSearched()

elif str(clearSearch) != "None":  
    # controller asks model to show all records
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyQuery1

    query1 = MyQuery1()
    results = query1.showAll()

    # controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from DisplayData import MyView1

    view1 = MyView1(results)
    view1.viewAll()

if str(clearDatabase) != "None":

    # controller asks model to clear the database
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyClearDatabase

    clear_db = MyClearDatabase()
    result = clear_db.clearAll()
    print(result)

    # controller updates the view back to show all records
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyQuery1

    query1 = MyQuery1()
    results = query1.showAll()

    # controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from DisplayData import MyView1

    view1 = MyView1(results)
    view1.viewAll()

    