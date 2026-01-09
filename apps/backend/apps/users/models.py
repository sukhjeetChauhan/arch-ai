from tkinter import CASCADE
from django.db import models
from apps.organisations.models import Organisation

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  org_Id = models.ForeignKey(Organisation, on_delete = models.CASCADE)
  sub = models.CharField(max_length = 70, null = True, blank = True)

