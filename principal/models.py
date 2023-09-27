
from django.db import models
from django.contrib.auth.models import User
 


# Create your models here.
class StudentForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length=50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField() # for creating file input  
    class Meta:  
        db_table = "student"