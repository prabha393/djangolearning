from django.db import models

class UserInfo(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    address = models.TextField(max_length=120)
