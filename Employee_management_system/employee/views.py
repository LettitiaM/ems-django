# Lettitia Mokubung
# November 2023 
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from pymongo import MongoClient

# Create your views here.
#Connecting to database
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
db = client.letti
collection = db['Employee'] 

#Inserting values
def add(request):
     
     if request.method == "POST":
      
           
             Employee_details = {
                 'Employee_name': request.POST['emp_name'],
                 'Employee_surname':request.POST['emp_sur'],
                 'Employee_position':request.POST['emp_pos'],
                 'Date_hired':request.POST['Date_hired']
             } 
            
             
             
             try:
                db.collection.insert_one(Employee_details)
                return render(request, 'employee.html')
             except:
                result = 0
             
             
     return render(request, 'Add.html')

#Viewing details
def employee_details(request):
 if request.method == "GET":
    c = []
    # d = collection.find()
    for x in db.collection.find():
        c.append(x)
    context = {'employee_data_list': c}
    print(c)

        
 template = loader.get_template('employee.html')
 return HttpResponse(template.render(context, request))


