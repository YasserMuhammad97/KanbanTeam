from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=200,default='')
    describtion = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200,default='')
    phone = models.IntegerField(default=0)

class Contact_Us(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000 , default='')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)