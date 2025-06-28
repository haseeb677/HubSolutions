from django.shortcuts import render
from django.http import HttpResponse

def courseDetails(request, course_id):
    return HttpResponse(course_id)

def about(request):
    return HttpResponse("This is the about page.")

def home(request):
    return HttpResponse("Welcome to the home page.")

# data={
#     'title': 'HubSolutions New Home Page',
#     'bdata': 'This is the body of the home page.',
#     'clist': ['Python', 'Django', 'JavaScript', 'HTML', 'CSS'],
#     'numbers':[30,40,50,60,20,10,5],

#     'Student_Details':[
#         {
#             'name': 'John Doe',
#             'age': 20,
#             'course': 'Python'
#         },
#         {
#             'name': 'Jane Smith',
#             'age': 22,
#             'course': 'Django'
#         },
#     ]

# }

def index2(request):
    return render(request, "index2.html")  # Assuming you have a index2.html template in your templates directory
def about(request):
    return render(request, "about.html")  # Assuming you have an about.html template in your templates directory

def shop(request):
    return render(request, "shop.html")  # Assuming you have a shop.html template in your templates 
def calculate(request):
    return render(request, "calculate.html")  # Assuming you have a calculate.html template in your templates directory
def header(request):
    return render(request, "header.html")  # Assuming you have a header.html template in your templates directory
def footer(request):
    return render(request, "footer.html")  # Assuming you have a footer.html template in your templates directory
def marksheet(request):
    return render(request,"marksheet.html")