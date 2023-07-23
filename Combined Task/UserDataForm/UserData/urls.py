from django.contrib import admin
from django.urls import path,include
from UserData import views

app_name = 'MemberData'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('form',views.form,name = 'form'),
    path('member-list',views.member_list,name = 'Member_List'),
    path('member/<member_id>',views.display_member,name = 'Display_Member'),
]
