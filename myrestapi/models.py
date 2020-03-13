from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=100);
    lastName = models.CharField(max_length=100);
    created_at = models.DateField();
    password = models.CharField(max_length=1000);
    updated_at = models.DateField();
    objects = models.manager;
    def __str__(self):
     return self.name;
