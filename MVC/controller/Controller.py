#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

print("Content-Type: text/html")
print()
import cgi
import sys

form = cgi.FieldStorage()

# so these are data we posted from index 
getALL = form.getvalue("ALL")
searchVisitorID = form.getvalue("visitor_id")
addRecordfromIndex = form.getvalue("ADD")
clearDatabase = form.getvalue("clear")


# so these are data we posted from HTML Design MyAddRecordBoostrap
addRecordfromBootStrapDesign = form.getvalue("send")
backHomefromBootStrapDesign = form.getvalue("back")

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

if str(addRecordfromIndex) != "None":

    # controller updates the view of addRecord
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from AddRecord import MyAddRecordView
    view1 = MyAddRecordView()
    view1.viewADDRecordDesign()

if str(addRecordfromBootStrapDesign) != "None":

    # controller asks model to perform add record
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/model")
    from Queries import MyAddRecord

    myaddrec = MyAddRecord(postedVisitorID, postedTime, postedDate)
    result = myaddrec.addRec()
    print(result)

    # controller updates the view back to addRecord
    sys.path.append("C:/xampp/htdocs/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/view")
    from AddRecord import AddRecordView

    view1 = AddRecordView()
    view1.viewADDRecordDesign()

if str(backHomefromBootStrapDesign) != "None":

    # controller asks updates design back to index or main
    redirectURL = "http://localhost/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/index.html"
    print('<script type="text/javascript">window.location ="' + redirectURL + '";</script>')

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