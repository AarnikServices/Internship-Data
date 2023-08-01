from rest_framework import serializers


GENDER_CHOICE = [('Male','Male'),('Female','Female'),('Other','Other')]
class user_data_serializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.CharField()
    vehicle = serializers.CharField()