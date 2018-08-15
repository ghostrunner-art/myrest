from django.db import models

# Create your models here.
class Que(models.Model):

    wenti = models.CharField(max_length=100,null=False,unique=True)
    daan1 = models.CharField(max_length=100,null=False,)
    daan2 = models.CharField(max_length=100,null=False,)
    daan3 = models.CharField(max_length=100,null=False,)
    daan4 = models.CharField(max_length=100,null=False,)

