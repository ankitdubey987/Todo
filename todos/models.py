from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def getCount(self):
        return self.objects.all().count()