from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from bson.objectid import ObjectId

members_data =settings.DB['user_data']

def index(request):
    return render(request,'MemberData/index.html')

def form(request):
    submitted = False
    if request.method == "POST" :
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        gender = request.POST.get('gender',"")
        vehicle = request.POST.getlist('vehicle',"")
        
        members_data.insert_one({"name":name,'email':email,'address':address,'gender':gender,'vehicle':vehicle})

        return HttpResponseRedirect("form?submitted=True")
    
    else:
        if 'submitted' in request.GET:
            submitted = True


    return render(request,'MemberData/form.html',{"submitted":submitted})

def member_list(request):
    context = members_data.find()
    return render(request,'MemberData/MemberList.html',{'members_list':context})

def display_member(request,member_id):
    member = members_data.find_one({'_id':ObjectId(member_id)})
    return render(request,'MemberData/DisplayMember.html',{'member':member})