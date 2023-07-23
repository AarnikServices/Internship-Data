from django.db import models

class users_data(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    gender = models.CharField(max_length=10)
    transport = models.CharField(max_length=50)

    def __str__(self):
        return self.name
