from django.urls import path,include
from .views import ListUsers


from rest_framework import routers

app_name = 'api'

urlpatterns = [
    path('users/',ListUsers.as_view({'get':'list','post':'create'}),name='user_api')
]