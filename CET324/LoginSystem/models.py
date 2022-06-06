from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model): 
    sporttype=models.CharField(max_length=200)
    

class Profile(models.Model):      
   user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
   sport = models.ManyToManyField(Sport)


 
class Stream(models.Model): 
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)
    sportdetail=models.CharField(max_length=200)
    url=models.CharField(max_length=500)
    participants=models.CharField(max_length=500)
    

