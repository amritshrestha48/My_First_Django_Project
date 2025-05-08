from django.http import HttpResponse
from django.shortcuts import render

import datetime
def home(request):
    isActive = True
    if request.method == "POST":
        check = request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True

    date = datetime.datetime.now()
    #isActive = True
    name = "Learning Django"
    list_of_programs = [
        'WAP to check even of odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascal triangle',
    ]
    student = {
        "student_name": "Amrit Shrestha",
        "student_college": "NCIT College",
        "student_city": "Kathmandu",
    }
    #print("test function is called from view")
    # return HttpResponse("<h1> Hello, This is index page </h1>" + str(date))
    data = {
        "date": date,
        "isActive": isActive,
        "name": name,
        "list_of_programs": list_of_programs,
        "student_data": student,
    }

    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1> Hello, This is about page </h1>")
    return render(request,"about.html",{})
def services(request):
    #return HttpResponse("<h1> Hello, This is a services page </h1>")
    return render(request,"services.html",{})



 