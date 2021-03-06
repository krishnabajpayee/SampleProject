from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profileImage=models.ImageField()
    gender=models.CharField(max_length=6,blank=False,null=False)
    contactNumber=models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.user.first_name + self.user.last_name

