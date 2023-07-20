from django import forms
from django.forms import ModelForm
from .models import users_data

GENDER_CHOICE = [('Male','Male'),('Female','Female'),('Other','Other')]
VEHICLE = [('Bike','Bike'),('car','car'),('Bus','Bus'),('Train','Train'),('Metro','Metro')]

class users_data_form(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    transport = forms.MultipleChoiceField(choices=VEHICLE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = users_data
        fields = "__all__"