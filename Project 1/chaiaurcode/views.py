from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello , This is the homepage of chaiaurcode project.")

# def about(request):
#     return HttpResponse("Hello , This is the about page of chaiaurcode project.")

# def contact(request):
#     return HttpResponse("Hello , This is the contact page of chaiaurcode project.")



def home(request):
    return render(request,'websites/index.html')

def about(request):
    return render(request,'websites/about.html')

def contact(request):
    return render(request,'websites/contact.html')