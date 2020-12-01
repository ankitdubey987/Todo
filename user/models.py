from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('F','FEMALE'),
        ('M','MALE'),
        ('T','TRANSGENDER'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_image = models.ImageField(upload_to='profile/')
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField( max_length=50,null=True)
    gender = models.CharField(max_length=45,choices=GENDER,null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=8,null=True)

    def __str__(self):
        return (self.first_name+' '+self.last_name+' '+self.user.username)

    def getProfileURL(self):
        if self.profile_image is not None:
            return self.profile_image.url
        return '/static/user_profile.jpg'