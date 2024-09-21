from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    #AbstractUser already comes with several built-in fields like username, email, password, first_name, last_name
    FARMER = 'FARMER'
    CONSUMER = 'CONSUMER'
    USER_ROLES = [
        (FARMER, 'Farmer'),
        (CONSUMER, 'Consumer'),
    ]
    
    phone_number = PhoneNumberField(unique=True)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default=CONSUMER)
    
    def __str__(self):
        return self.username
    
class Farmer(models.Model):
    farmer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    farm_address = models.CharField(max_length=255)
    has_cold_store = models.BooleanField(default=False)
    description = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.farmer.username
    
    
