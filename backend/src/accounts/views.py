from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer
    
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    
