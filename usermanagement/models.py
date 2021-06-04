from django.db import models
from .validations import checkNull, emailValidation, phoneNumberValidation

# Create your models here.

class createUser(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, default="", validators=[checkNull])
    mailid = models.CharField(max_length=50, default="", validators=[emailValidation], unique=True)
    phoneNumber = models.CharField(max_length=10, default = "", validators=[phoneNumberValidation], unique=True)
