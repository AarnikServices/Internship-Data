from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Myapp/index.html')
def About(request):
    return render(request,'MyApp/About.html')
def Contact(request):
    return render(request,"MyApp/Contact.html")
