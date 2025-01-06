from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class test(models.Model):
    U_Id = models.IntegerField(default=0)
    Title = models.CharField(max_length=20)
    Text = models.TextField(max_length=1000)

class test1(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)