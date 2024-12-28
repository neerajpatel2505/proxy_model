from django.shortcuts import render
from .models import BaseInfo,ProxyBaseInfo

# Create your views here.
def home(request):
    base_data = BaseInfo.objects.all()
    print("Base_data = ",base_data.values())

    proxy_data = ProxyBaseInfo.objects.all()
    print("proxy_data = ",proxy_data.values())