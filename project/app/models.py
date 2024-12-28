from django.db import models
from datetime import date,datetime

# Proxy model inheritence
class BaseInfo(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length = 50)              
    fees = models.IntegerField()
    
    class Meta:
        db_table = 'MainModel'
        ordering = ['id']
        # verbose_name = "My Custom Model"
        verbose_name_plural = "My Custom Model"     # Human readable table name without s

class ProxyBaseInfo(BaseInfo):
    class Meta:
        proxy = True
        ordering = ['name']
        verbose_name = "MyProxyModel"               # Human readable table name with s