from django.shortcuts import render
from .forms import users_data_form
from django.http import HttpResponseRedirect

def index(request):
    submitted = False
    if request.method == "POST" :
        form = users_data_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("?submitted=True")
    
    else:
        #hello
        form = users_data_form
        if 'submitted' in request.GET:
            submitted = True

    form = users_data_form
    return render(request,'MyApp/index.html',{"form":form,"submitted":submitted})

