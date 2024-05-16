#!C:\Users\rjesc\AppData\Local\Programs\Python\Python312\python.exe

import cgi

class AddRecordView(object):
    def viewADDRecordDesign(self):
        print()
        print("""
        <html>
              <head>
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                <title>My Form</title>
              </head>
              
              <body>
               
               <div class="row">
                  
                  <div class="col-sm-12" style="background-color:#3d5c44">
                      <h1 style="display:inline-block;color: white;">ADD RECORD</h1>
                  </div>
              
                  <div class="col-sm-6" style="background-color:#c3cbd9; padding: 2em">
                   
                        <form action='/laser-visitor-counter-IoT-NodeMCU-RFID/MVC/controller/Controller.py' method='post'>
                        
                            <label>Visitor ID:</label>
                            <input type="text" class="form-control" name="visitor_ID" placeholder="Type Visitor ID">
                            
                            <label>Time:</label>				
                            <input type="text" class="form-control" name="time" placeholder="Type Time">
                            
                            <label>Date:</label>				
                            <input type="text" class="form-control" name="date" placeholder="Type Date">
                            
                            </br>				
                            <input type="submit" class="btn btn-primary" name="send" value="Send">	
                            <input type="submit" class="btn btn-primary" name="back" value="BACK HOME">
                        
                        </form> 
                                           
                         
                  </div>
                  
                  <div class="col-sm-6" style="background-color:#4d45ba;"> 
                      <p style="text-align:justify; font-family:Arial; font-size: 34px; color: white;"> 
                         This is a sample Form for input text, Option, Button 
                         using class design from Bootstrap wakokok
                      </p>
                  </div>
                  
                  <div class="col-sm-12" style="background-color:#556470;"> 
                      some text here .footer mo siguro
                  </div>
                  
               </div>
               
              </body>
            </html>
            """)
