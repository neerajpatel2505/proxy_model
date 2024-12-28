from django.contrib import admin
from .models import *
# Register your models here.

# proxy inheritence
@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','address','branch','fees']

@admin.register(ProxyBaseInfo)
class ProxyBaseInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','address','branch','fees']