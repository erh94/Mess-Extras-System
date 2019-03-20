from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.core.validators import MinValueValidator
# Create your models here.
from model_utils import Choices

hostels = Choices('H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','tansa','qip')

foodChoices = Choices('breakfast','lunch','snacks','dinner','milk','breakfast extra','lunch extras','dinner extras','extras')

class User(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # rollnumber = models.CharField(max_length=10,default='others',blank=False)
    hostel = models.CharField(max_length=5,blank=True,null=True)
    hostel_name = models.CharField(max_length=5,blank=True,null=True)
    room = models.CharField(max_length=5,blank=True,null=True)
    # datetime = models.DateTimeField(default=datetime.now) 


class GuestBookEntry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    hostel = models.CharField(max_length=5)
    extra = models.CharField(max_length=20,choices=foodChoices,default=foodChoices.extras)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    # token = models.CharField(max_length=1024)
    class Meta:
        ordering = ['-date']    
