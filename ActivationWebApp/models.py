from django.db import models

# Create your models here.

class Keys(models.Model):
    Key = models.CharField(max_length=20)