from django.db import models


class About(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True,default="")
    work_status=models.CharField(max_length=50,blank=True,null=True,default="")
    description=models.TextField(max_length=300, blank=True,null=True,default="")
    updated_date=models.DateTimeField(auto_now=True,blank=True)
    created_date=models.DateTimeField(auto_now=True,blank=True)
